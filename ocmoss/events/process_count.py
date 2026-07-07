"""
OCMOSS

P.2.02

Process Count
"""

from ocmoss.windows.process_count import (
    ProcessCountError,
    get_process_count,
)


def run() -> None:
    """
    Execute the ProcessCount event.
    """

    print("────────────────────────────")
    print("ID         : P.2.02")
    print("Name       : ProcessCount")
    print()

    try:
        process_count, application_count = (
            get_process_count()
        )

        print(
            f"{'Processes':<18} : "
            f"{process_count}"
        )

        print(
            f"{'Applications':<18} : "
            f"{application_count}"
        )

        print(
            f"{'Status':<18} : Success"
        )

    except ProcessCountError as error:

        print(
            f"{'Processes':<18} : Not Available"
        )

        print(
            f"{'Applications':<18} : Not Available"
        )

        print(
            f"{'Status':<18} : Failed"
        )

        print(
            f"{'Reason':<18} : {error}"
        )

    print("────────────────────────────")