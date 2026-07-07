"""
OCMOSS SDK

Windows Power Source Module

Retrieves the latest Windows power
source change event.
"""

from __future__ import annotations

import subprocess

from datetime import datetime


class PowerSourceError(Exception):
    """
    Raised when the latest power source
    event cannot be retrieved.
    """
    pass


def get_last_power_source_change() -> datetime:
    """
    Retrieve the latest Windows power
    source change time.
    """

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "(Get-WinEvent -FilterHashtable @{LogName='System'; Id=105} -MaxEvents 1).TimeCreated.ToString('yyyy-MM-dd HH:mm:ss')",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        power_time = result.stdout.strip()

        if not power_time:
            raise PowerSourceError(
                "No power source change event found."
            )

        return datetime.strptime(
            power_time,
            "%Y-%m-%d %H:%M:%S",
        )

    except subprocess.CalledProcessError as error:
        raise PowerSourceError(
            error.stderr.strip()
            or "PowerShell command failed."
        ) from error

    except ValueError as error:
        raise PowerSourceError(
            "Unable to parse power source time."
        ) from error