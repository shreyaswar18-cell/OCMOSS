"""
OCMOSS

E.1.03

Current Uptime
"""

from ocmoss.windows.uptime import (
    UptimeError,
    get_current_uptime,
)


def run() -> None:
    """
    Execute the CurrentUptime event.
    """

    print("────────────────────────────")
    print("ID         : E.1.03")
    print("Name       : CurrentUptime")
    print()

    try:
        uptime: str = get_current_uptime()

        print(f"{'Uptime':<18} : {uptime}")
        print(f"{'Status':<18} : Success")

    except UptimeError as error:
        print(f"{'Uptime':<18} : Not Available")
        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")