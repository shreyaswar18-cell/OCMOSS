"""
OCMOSS

E.1.07

Power Source Changed
"""

from datetime import datetime

from ocmoss.windows.power_source import (
    PowerSourceError,
    get_last_power_source_change,
)


def run() -> None:
    """
    Execute the PowerSourceChanged event.
    """

    print("────────────────────────────")
    print("ID         : E.1.07")
    print("Name       : PowerSourceChanged")
    print()

    try:
        power_time: datetime = get_last_power_source_change()

        print(
            f"{'Event Time':<18} : {power_time.strftime('%d %B %Y %H:%M:%S')}"
        )
        print(f"{'Status':<18} : Success")

    except PowerSourceError as error:
        print(f"{'Event Time':<18} : Not Available")
        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")