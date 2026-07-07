"""
OCMOSS

P.2.01

Running Applications
"""

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


def run() -> None:
    """
    Execute the RunningApplications event.
    """

    print("────────────────────────────")
    print("ID         : P.2.01")
    print("Name       : RunningApplications")
    print()

    try:
        processes = get_running_processes()

        applications = [
            process
            for process in processes
            if (
                process["session"] == "Console"
                and process["name"] not in IGNORE_PROCESSES
            )
        ]

        unique_applications = sorted(
            {
                process["name"]
                for process in applications
            }
        )

        print(
            f"{'Applications':<18} : "
            f"{len(unique_applications)}"
        )
        print()

        print("Running Applications")
        print("────────────────────────────")

        for name in unique_applications:
            print(name)

        print()

        print(f"{'Status':<18} : Success")

    except ProcessError as error:

        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")