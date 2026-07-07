"""
OCMOSS SDK

Windows Shutdown Module

This module is responsible for retrieving the
latest Windows shutdown time.
"""

from __future__ import annotations

import subprocess

from datetime import datetime


class ShutdownError(Exception):
    """
    Raised when the Windows shutdown time
    cannot be retrieved.
    """
    pass


def get_last_shutdown() -> datetime:
    """
    Retrieve the latest Windows shutdown time.
    """

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "(Get-WinEvent -FilterHashtable @{LogName='System'; Id=1074} -MaxEvents 1).TimeCreated.ToString('yyyy-MM-dd HH:mm:ss')",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        shutdown_time = result.stdout.strip()

        if not shutdown_time:
            raise ShutdownError(
                "Windows returned an empty shutdown time."
            )

        return datetime.strptime(
            shutdown_time,
            "%Y-%m-%d %H:%M:%S",
        )

    except subprocess.CalledProcessError as error:
        raise ShutdownError(
            error.stderr.strip()
            or "PowerShell command failed."
        ) from error

    except ValueError as error:
        raise ShutdownError(
            "Unable to parse the Windows shutdown time."
        ) from error