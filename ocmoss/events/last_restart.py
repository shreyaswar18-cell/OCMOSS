"""
OCMOSS

E.1.04

Last Restart
"""

from datetime import datetime

from ocmoss.windows.restart import (
    RestartError,
    get_last_restart,
)


def run() -> None:
    """
    Execute the LastRestart event.
    """

    print("────────────────────────────")
    print("ID         : E.1.04")
    print("Name       : LastRestart")
    print()

    try:
        restart_time: datetime = get_last_restart()

        print(
            f"{'Restart Time':<18} : {restart_time.strftime('%d %B %Y %H:%M:%S')}"
        )
        print(f"{'Status':<18} : Success")

    except RestartError as error:
        print(f"{'Restart Time':<18} : Not Available")
        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")