"""
OCMOSS

N.3.05

Saved WiFi Passwords
"""

from ocmoss.windows.wifi_password import (
    WiFiPasswordError,
    get_wifi_passwords,
)


def run() -> None:
    """
    Execute the SavedWiFiPasswords event.
    """

    print("────────────────────────────")
    print("ID         : N.3.05")
    print("Name       : SavedWiFiPasswords")
    print()

    try:
        profiles = get_wifi_passwords()

        for profile in profiles:

            print(f"SSID     : {profile['ssid']}")
            print(f"Password : {profile['password']}")
            print()

        print(f"{'Status':<18} : Success")

    except WiFiPasswordError as error:

        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")