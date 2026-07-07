"""
OCMOSS

N.3.02

Internet Status
"""

from ocmoss.windows.internet_status import (
    InternetStatusError,
    get_internet_status,
)


def run() -> None:
    """
    Execute the InternetStatus event.
    """

    print("────────────────────────────")
    print("ID         : N.3.02")
    print("Name       : InternetStatus")
    print()

    try:
        connected = get_internet_status()

        if connected:
            status = "Connected"
        else:
            status = "Disconnected"

        print(f"{'Internet':<18} : {status}")
        print(f"{'Status':<18} : Success")

    except InternetStatusError as error:

        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")