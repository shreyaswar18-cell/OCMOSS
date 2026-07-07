"""
OCMOSS SDK

Entry Point
"""

from ocmoss.events.system_started import run as system_started
from ocmoss.events.system_exit import run as system_exit
from ocmoss.events.current_uptime import run as current_uptime
from ocmoss.events.last_restart import run as last_restart
from ocmoss.events.sleep_started import run as sleep_started
from ocmoss.events.wake_up import run as wake_up
from ocmoss.events.power_source_changed import (
    run as power_source_changed,
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

    system_exit()

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


if __name__ == "__main__":
    main()