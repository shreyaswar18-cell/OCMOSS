"""
OCMOSS

P.2.03

Process Memory Usage
"""

from ocmoss.windows.process_memory import (
    ProcessMemoryError,
    get_process_memory,
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
    "Memory Compression",
}


def run() -> None:
    """
    Execute the ProcessMemoryUsage event.
    """

    print("────────────────────────────")
    print("ID         : P.2.03")
    print("Name       : ProcessMemoryUsage")
    print()

    try:
        processes = get_process_memory()

        application_memory: dict[str, int] = {}

        for process in processes:

            if process["name"] in IGNORE_PROCESSES:
                continue

            memory = int(
                process["memory"]
                .replace(",", "")
                .replace(" K", "")
            )

            application_memory[process["name"]] = (
                application_memory.get(
                    process["name"],
                    0,
                )
                + memory
            )

        top_applications = sorted(
            application_memory.items(),
            key=lambda item: item[1],
            reverse=True,
        )[:10]

        print("Top 10 Memory Usage")
        print("────────────────────────────────────────────────────────")
        print(
            f"{'Rank':<6}"
            f"{'Application':<42}"
            f"{'Memory'}"
        )

        for rank, (name, memory) in enumerate(
            top_applications,
            start=1,
        ):

            print(
                f"{rank:<6}"
                f"{name:<42}"
                f"{memory:,} K"
            )

        print()
        print(f"{'Status':<18} : Success")

    except ProcessMemoryError as error:

        print(f"{'Status':<18} : Failed")
        print(f"{'Reason':<18} : {error}")

    print("────────────────────────────")