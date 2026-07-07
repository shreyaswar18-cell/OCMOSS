"""
OCMOSS SDK

Windows Sleep Module

Retrieves the latest Windows sleep time.
"""

from __future__ import annotations

import subprocess

from datetime import datetime


class SleepError(Exception):
    """
    Raised when the latest sleep event
    cannot be retrieved.
    """
    pass


def get_last_sleep() -> datetime:
    """
    Retrieve the latest Windows sleep time.
    """

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "(Get-WinEvent -FilterHashtable @{LogName='System'; Id=42} -MaxEvents 1).TimeCreated.ToString('yyyy-MM-dd HH:mm:ss')",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        sleep_time = result.stdout.strip()

        if not sleep_time:
            raise SleepError(
                "No sleep event found."
            )

        return datetime.strptime(
            sleep_time,
            "%Y-%m-%d %H:%M:%S",
        )

    except subprocess.CalledProcessError as error:
        raise SleepError(
            error.stderr.strip()
            or "PowerShell command failed."
        ) from error

    except ValueError as error:
        raise SleepError(
            "Unable to parse sleep time."
        ) from error