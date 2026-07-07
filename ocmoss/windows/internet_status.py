"""
OCMOSS

Windows Internet Status Module

This module checks whether
Internet access is available.
"""

from __future__ import annotations

import socket


class InternetStatusError(Exception):
    """
    Raised when Internet status
    cannot be determined.
    """
    pass


def get_internet_status() -> bool:
    """
    Check Internet connectivity.

    Returns
    -------
    bool
        True if connected,
        otherwise False.
    """

    try:
        socket.create_connection(
            ("8.8.8.8", 53),
            timeout=3,
        )

        return True

    except OSError:

        return False

    except Exception as error:

        raise InternetStatusError(
            "Unable to determine Internet status."
        ) from error