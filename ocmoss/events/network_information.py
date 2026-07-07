"""
OCMOSS

N.3.01

Network Information
"""

from ocmoss.windows.network_information import (
    NetworkInformationError,
    get_network_information,
)


def run() -> None:
    """
    Execute the NetworkInformation event.
    """

    print("────────────────────────────")
    print("ID         : N.3.01")
    print("Name       : NetworkInformation")
    print()

    try:
        info = get_network_information()

        print(f"{'Computer Name':<18} : {info['computer_name']}")
        print(f"{'Host Name':<18} : {info['host_name']}")
        print(f"{'MAC Address':<18} : {info['mac_address']}")
        print(f"{'Connection Type':<18} : {info['connection_type']}")
        print(f"{'Adapter':<18} : {info['adapter']}")
        print(f"{'Status':<18} : Success")

    except NetworkInformationError as error:

        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")