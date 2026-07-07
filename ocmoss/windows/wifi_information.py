"""
OCMOSS

Windows Wi-Fi Information Module

This module retrieves the
current Wi-Fi information.
"""

from __future__ import annotations

import subprocess


class WiFiInformationError(Exception):
    """
    Raised when Wi-Fi information
    cannot be retrieved.
    """
    pass


def get_wifi_information() -> dict[str, str]:
    """
    Retrieve current Wi-Fi information.

    Returns
    -------
    dict[str, str]
        Wi-Fi information.
    """

    try:
        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            check=True,
        )

        info: dict[str, str] = {}

        for line in result.stdout.splitlines():

            if ":" not in line:
                continue

            key, value = line.split(":", 1)

            info[key.strip()] = value.strip()

        return {
            "ssid": info.get("SSID", "Not Available"),
            "signal": info.get("Signal", "Not Available"),
            "radio_type": info.get(
                "Radio type",
                "Not Available",
            ),
            "authentication": info.get(
                "Authentication",
                "Not Available",
            ),
            "channel": info.get(
                "Channel",
                "Not Available",
            ),
        }

    except subprocess.CalledProcessError as error:

        raise WiFiInformationError(
            "Unable to retrieve Wi-Fi information."
        ) from error