"""
OCMOSS SDK

Windows WakeUp Module

Retrieves the latest Windows wake-up time.
"""

from __future__ import annotations

import subprocess

from datetime import datetime


class WakeUpError(Exception):
    """
    Raised when the latest wake-up event
    cannot be retrieved.
    """
    pass


def get_last_wakeup() -> datetime:
    """
    Retrieve the latest Windows wake-up time.
    """

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "(Get-WinEvent -FilterHashtable @{LogName='System'; ProviderName='Microsoft-Windows-Power-Troubleshooter'; Id=1} -MaxEvents 1).TimeCreated.ToString('yyyy-MM-dd HH:mm:ss')",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        wakeup_time = result.stdout.strip()

        if not wakeup_time:
            raise WakeUpError(
                "No wake-up event found."
            )

        return datetime.strptime(
            wakeup_time,
            "%Y-%m-%d %H:%M:%S",
        )

    except subprocess.CalledProcessError as error:
        raise WakeUpError(
            error.stderr.strip()
            or "PowerShell command failed."
        ) from error

    except ValueError as error:
        raise WakeUpError(
            "Unable to parse wake-up time."
        ) from error