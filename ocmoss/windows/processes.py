"""
OCMOSS

Windows Running Processes Module

This module retrieves all currently
running Windows processes.
"""

from __future__ import annotations

import csv
import io
import subprocess


class ProcessError(Exception):
    """
    Raised when running processes
    cannot be retrieved.
    """
    pass


def get_running_processes() -> list[dict]:
    """
    Retrieve all running Windows processes.

    Returns
    -------
    list[dict]
        Running process information.
    """

    try:
        result = subprocess.run(
            ["tasklist", "/FO", "CSV", "/NH"],
            capture_output=True,
            text=True,
            check=True,
        )

        reader = csv.reader(io.StringIO(result.stdout))

        processes: list[dict] = []

        for row in reader:

            if len(row) != 5:
                continue

            processes.append(
                {
                    "name": row[0],
                    "pid": int(row[1]),
                    "session": row[2],
                    "session_id": int(row[3]),
                    "memory": row[4],
                }
            )

        return processes

    except (
        subprocess.CalledProcessError,
        ValueError,
    ) as error:
        raise ProcessError(
            "Unable to retrieve running processes."
        ) from error