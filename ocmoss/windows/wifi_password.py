"""
OCMOSS

Windows Wi-Fi Password Module
"""

from __future__ import annotations

import subprocess
import re


class WiFiPasswordError(Exception):
    """
    Raised when Wi-Fi passwords
    cannot be retrieved.
    """
    pass


def get_wifi_passwords() -> list[dict[str, str]]:
    """
    Retrieve all saved Wi-Fi
    profiles and passwords.
    """

    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "profiles"],
            capture_output=True,
            text=True,
            check=True,
        )

        profiles = re.findall(
            r"All User Profile\s*:\s*(.*)",
            result.stdout,
        )

        wifi_profiles = []

        for profile in profiles:

            profile = profile.strip()

            detail = subprocess.run(
                [
                    "netsh",
                    "wlan",
                    "show",
                    "profile",
                    profile,
                    "key=clear",
                ],
                capture_output=True,
                text=True,
            )

            match = re.search(
                r"Key Content\s*:\s*(.*)",
                detail.stdout,
            )

            password = (
                match.group(1).strip()
                if match
                else "No Password"
            )

            wifi_profiles.append(
                {
                    "ssid": profile,
                    "password": password,
                }
            )

        return wifi_profiles

    except subprocess.CalledProcessError as error:

        raise WiFiPasswordError(
            "Unable to retrieve Wi-Fi passwords."
        ) from error