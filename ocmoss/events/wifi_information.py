"""
OCMOSS

N.3.04

WiFi Information
"""

from ocmoss.windows.wifi_information import (
    WiFiInformationError,
    get_wifi_information,
)


def run() -> None:
    """
    Execute the WiFiInformation event.
    """

    print("────────────────────────────")
    print("ID         : N.3.04")
    print("Name       : WiFiInformation")
    print()

    try:
        info = get_wifi_information()

        print(f"{'SSID':<18} : {info['ssid']}")
        print(f"{'Signal':<18} : {info['signal']}")
        print(f"{'Radio Type':<18} : {info['radio_type']}")
        print(
            f"{'Authentication':<18} : "
            f"{info['authentication']}"
        )
        print(f"{'Channel':<18} : {info['channel']}")
        print(f"{'Status':<18} : Success")

    except WiFiInformationError as error:

        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")