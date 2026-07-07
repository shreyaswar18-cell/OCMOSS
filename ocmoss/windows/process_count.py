"""
OCMOSS

Windows Process Count Module

This module retrieves the total
number of running processes and
applications.
"""

from __future__ import annotations

from ocmoss.windows.processes import (
    ProcessError,
    get_running_processes,
)


IGNORE_PROCESSES = {
    "svchost.exe",
    "RuntimeBroker.exe",
    "conhost.exe",
    "taskhostw.exe",
    "fontdrvhost.exe",
    "csrss.exe",
    "winlogon.exe",
    "SearchHost.exe",
    "ShellExperienceHost.exe",
    "StartMenuExperienceHost.exe",
    "TextInputHost.exe",
    "Widgets.exe",
    "WidgetService.exe",
    "backgroundTaskHost.exe",
    "dwm.exe",
}


class ProcessCountError(Exception):
    """
    Raised when process counts
    cannot be retrieved.
    """
    pass


def get_process_count() -> tuple[int, int]:
    """
    Retrieve the total number of
    running processes and applications.

    Returns
    -------
    tuple[int, int]
        Total processes,
        Total applications.
    """

    try:
        processes = get_running_processes()

        applications = {
            process["name"]
            for process in processes
            if (
                process["session"] == "Console"
                and process["name"] not in IGNORE_PROCESSES
            )
        }

        return (
            len(processes),
            len(applications),
        )

    except ProcessError as error:
        raise ProcessCountError(
            "Unable to retrieve process count."
        ) from error