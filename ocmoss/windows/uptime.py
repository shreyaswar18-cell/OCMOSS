"""
OCMOSS

Windows Uptime Module

Calculates the current Windows
uptime using the system boot time.
"""

from __future__ import annotations

from ocmoss.windows.boot_time import (
    BootTimeError,
    get_windows_boot_time,
)

from datetime import datetime


class UptimeError(Exception):
    """
    Raised when the Windows uptime
    cannot be calculated.
    """
    pass


def get_current_uptime() -> str:
    """
    Retrieve the current Windows uptime.

    Returns
    -------
    str
        Current Windows uptime.
    """

    try:
        boot_time = get_windows_boot_time()

        uptime = datetime.now() - boot_time

        total_seconds = int(uptime.total_seconds())

        days = total_seconds // 86400
        total_seconds %= 86400

        hours = total_seconds // 3600
        total_seconds %= 3600

        minutes = total_seconds // 60
        seconds = total_seconds % 60

        return (
            f"{days} Days "
            f"{hours} Hours "
            f"{minutes} Minutes "
            f"{seconds} Seconds"
        )

    except BootTimeError as error:
        raise UptimeError(
            "Unable to calculate Windows uptime."
        ) from error