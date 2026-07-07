"""
OCMOSS

E.1.06

Wake Up
"""

from datetime import datetime

from ocmoss.windows.wakeup import (
    WakeUpError,
    get_last_wakeup,
)


def run() -> None:
    """
    Execute the WakeUp event.
    """

    print("────────────────────────────")
    print("ID         : E.1.06")
    print("Name       : WakeUp")
    print()

    try:
        wakeup_time: datetime = get_last_wakeup()

        print(
            f"{'Wake Time':<18} : {wakeup_time.strftime('%d %B %Y %H:%M:%S')}"
        )
        print(f"{'Status':<18} : Success")

    except WakeUpError as error:
        print(f"{'Wake Time':<18} : Not Available")
        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")