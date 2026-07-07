"""
OCMOSS

Windows Network Information Module

This module retrieves basic
Windows network information.
"""

from __future__ import annotations

import socket
import subprocess
import uuid


class NetworkInformationError(Exception):
    """
    Raised when network information
    cannot be retrieved.
    """
    pass


def get_network_information() -> dict[str, str]:
    """
    Retrieve Windows network information.

    Returns
    -------
    dict[str, str]
        Network information.
    """

    try:
        hostname = socket.gethostname()

        mac = ":".join(
            f"{(uuid.getnode() >> shift) & 0xFF:02X}"
            for shift in range(40, -1, -8)
        )

        result = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True,
            text=True,
            check=True,
        )

        adapter = "Not Available"
        connection = "Ethernet"

        for line in result.stdout.splitlines():

            if line.strip().startswith("Name"):

                adapter = line.split(":", 1)[1].strip()
                connection = "Wi-Fi"
                break

        return {
            "computer_name": hostname,
            "host_name": hostname,
            "mac_address": mac,
            "connection_type": connection,
            "adapter": adapter,
        }

    except (
        OSError,
        subprocess.CalledProcessError,
    ) as error:

        raise NetworkInformationError(
            "Unable to retrieve network information."
        ) from error