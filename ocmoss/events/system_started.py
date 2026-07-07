"""
OCMOSS

E.1.01

System Started
"""

from datetime import datetime

from ocmoss.windows.boot_time import (
    BootTimeError,
    get_windows_boot_time,
)


def run() -> None:
    """
    Execute the SystemStarted event.
    """

    print("────────────────────────────")
    print("ID         : E.1.01")
    print("Name       : SystemStarted")
    print()

    try:
        boot_time: datetime = get_windows_boot_time()

        print(
            f"{'Boot Time':<18} : {boot_time.strftime('%d %B %Y %H:%M:%S')}"
        )
        print(f"{'Status':<18} : Success")

    except BootTimeError as error:
        print(f"{'Boot Time':<18} : Not Available")
        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")