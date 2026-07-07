"""
OCMOSS SDK

Windows Boot Time Module

This module is responsible for retrieving the Windows
operating system boot time using official Windows-supported
interfaces.

This module should NOT print anything to the terminal.
It only retrieves and returns boot time information.
"""

from __future__ import annotations

import subprocess

from datetime import datetime

class BootTimeError(Exception):
    """
    Raised when the Windows boot time
    cannot be retrieved.
    """
    pass


def get_windows_boot_time() -> datetime:
    """
    Retrieve the current Windows operating system
    boot time.

    Returns
    -------
    datetime
        Windows boot time.

    Raises
    ------
    BootTimeError
        If the boot time cannot be retrieved.
    """

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        "(Get-CimInstance -ClassName Win32_OperatingSystem).LastBootUpTime.ToString('yyyy-MM-dd HH:mm:ss')",
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        boot_time = result.stdout.strip()

        if not boot_time:
            raise BootTimeError(
                "Windows returned an empty boot time."
            )

        return datetime.strptime(
            boot_time,
            "%Y-%m-%d %H:%M:%S",
        )

    except subprocess.CalledProcessError as error:
        raise BootTimeError(
            error.stderr.strip()
            or "PowerShell command failed."
        ) from error

    except ValueError as error:
        raise BootTimeError(
            "Unable to parse the Windows boot time."
        ) from error

       