"""
OCMOSS SDK

Windows Restart Module

Retrieves the latest Windows restart time
from the Windows Event Log.
"""

from __future__ import annotations

import subprocess

from datetime import datetime


class RestartError(Exception):
    """
    Raised when the latest Windows restart
    cannot be retrieved.
    """
    pass


def get_last_restart() -> datetime:
    """
    Retrieve the latest Windows restart time.
    """

    command = [
        "powershell",
        "-NoProfile",
        "-Command",
        """
        $event = Get-WinEvent -FilterHashtable @{LogName='System'; Id=1074} -MaxEvents 20 |
        Where-Object {$_.Message -match 'Shutdown Type:\\s+restart'} |
        Select-Object -First 1

        if ($event) {
            $event.TimeCreated.ToString('yyyy-MM-dd HH:mm:ss')
        }
        """,
    ]

    try:
        result = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
        )

        restart_time = result.stdout.strip()

        if not restart_time:
            raise RestartError(
                "No restart event found."
            )

        return datetime.strptime(
            restart_time,
            "%Y-%m-%d %H:%M:%S",
        )

    except subprocess.CalledProcessError as error:
        raise RestartError(
            error.stderr.strip()
            or "PowerShell command failed."
        ) from error

    except ValueError as error:
        raise RestartError(
            "Unable to parse the restart time."
        ) from error