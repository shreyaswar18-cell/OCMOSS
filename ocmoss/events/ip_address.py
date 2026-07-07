"""
OCMOSS

N.3.03

IP Address
"""

from ocmoss.windows.ip_address import (
    IPAddressError,
    get_ip_address,
)


def run() -> None:
    """
    Execute the IPAddress event.
    """

    print("────────────────────────────")
    print("ID         : N.3.03")
    print("Name       : IPAddress")
    print()

    try:
        info = get_ip_address()

        print(
            f"{'Local IPv4':<18} : "
            f"{info['local_ip']}"
        )

        print(
            f"{'Status':<18} : Success"
        )

    except IPAddressError as error:

        print(
            f"{'Status':<18} : Failed"
        )

        print(
            f"{'Reason':<18} : {error}"
        )

    print("────────────────────────────")