"""
OCMOSS

E.1.02

Last Shutdown
"""

from datetime import datetime

from ocmoss.windows.shutdown import (
    ShutdownError,
    get_last_shutdown,
)


def run() -> None:
    """
    Execute the Last Shutdown event.
    """

    print("────────────────────────────")
    print("ID         : E.1.02")
    print("Name       : LastShutdown")
    print()

    try:
        shutdown_time: datetime = get_last_shutdown()

        print(
            f"{'Shutdown Time':<18} : {shutdown_time.strftime('%d %B %Y %H:%M:%S')}"
        )
        print(f"{'Status':<18} : Success")

    except ShutdownError as error:
        print(f"{'Shutdown Time':<18} : Not Available")
        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")