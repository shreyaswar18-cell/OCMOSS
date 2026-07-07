"""
OCMOSS SDK

Entry Point
"""

from ocmoss.events.system_started import run as system_started
from ocmoss.events.last_shutdown import run as last_shutdown
from ocmoss.events.current_uptime import run as current_uptime
from ocmoss.events.last_restart import run as last_restart
from ocmoss.events.sleep_started import run as sleep_started
from ocmoss.events.wake_up import run as wake_up
from ocmoss.events.power_source_changed import (
    run as power_source_changed,
)
from ocmoss.events.running_processes import (
    run as running_processes,
)
from ocmoss.events.process_count import (
    run as process_count,
)
from ocmoss.events.process_memory import (
    run as process_memory,
)


def main() -> None:
    """
    Start the OCMOSS SDK.
    """

    print("══════════════════════════════════════")
    print("OCMOSS")
    print("Version 1.0")
    print("Operating System Lifecycle")
    print("══════════════════════════════════════")
    print()

    system_started()
    print()

    last_shutdown()
    print()

    current_uptime()
    print()

    last_restart()
    print()

    sleep_started()
    print()

    wake_up()
    print()

    power_source_changed()
    print()

    print("══════════════════════════════════════")
    print("       Version 1.0 Completed")
    print("══════════════════════════════════════")
    print()

    print("══════════════════════════════════════")
    print("OCMOSS")
    print("Version 2.0")
    print("Process Monitoring")
    print("══════════════════════════════════════")
    print()

    running_processes()
    print()

    process_count()
    print()

    process_memory()
    print()


    print("══════════════════════════════════════")
    print("       Version 2.0 Completed")
    print("══════════════════════════════════════")


if __name__ == "__main__":
    main()