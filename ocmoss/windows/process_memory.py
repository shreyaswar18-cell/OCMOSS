"""
OCMOSS

Windows Process Memory Module

This module retrieves memory
usage of all running processes.
"""

from __future__ import annotations

from ocmoss.windows.processes import (
    ProcessError,
    get_running_processes,
)


class ProcessMemoryError(Exception):
    """
    Raised when process memory
    cannot be retrieved.
    """
    pass


def get_process_memory() -> list[dict]:
    """
    Retrieve memory usage of all
    running processes.

    Returns
    -------
    list[dict]
        Process memory information.
    """

    try:
        return get_running_processes()

    except ProcessError as error:
        raise ProcessMemoryError(
            "Unable to retrieve process memory."
        ) from error