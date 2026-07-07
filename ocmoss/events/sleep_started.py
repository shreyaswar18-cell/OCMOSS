"""
OCMOSS

E.1.05

Sleep Started
"""

from datetime import datetime

from ocmoss.windows.sleep import (
    SleepError,
    get_last_sleep,
)


def run() -> None:
    """
    Execute the SleepStarted event.
    """

    print("────────────────────────────")
    print("ID         : E.1.05")
    print("Name       : SleepStarted")
    print()

    try:
        sleep_time: datetime = get_last_sleep()

        print(
            f"{'Sleep Time':<18} : {sleep_time.strftime('%d %B %Y %H:%M:%S')}"
        )
        print(f"{'Status':<18} : Success")

    except SleepError as error:
        print(f"{'Sleep Time':<18} : Not Available")
        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")