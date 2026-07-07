"""
OCMOSS

Windows IP Address Module

This module retrieves the
local IP address.
"""

from __future__ import annotations

import socket


class IPAddressError(Exception):
    """
    Raised when IP address
    cannot be retrieved.
    """
    pass


def get_ip_address() -> dict[str, str]:
    """
    Retrieve the local IP address.

    Returns
    -------
    dict[str, str]
        IP address information.
    """

    try:
        hostname = socket.gethostname()

        local_ip = socket.gethostbyname(hostname)

        return {
            "local_ip": local_ip,
        }

    except OSError as error:
        raise IPAddressError(
            "Unable to retrieve IP address."
        ) from error