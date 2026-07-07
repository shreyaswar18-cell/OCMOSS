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
from ocmoss.events.network_information import (
    run as network_information,
)
from ocmoss.events.internet_status import (
    run as internet_status,
)
from ocmoss.events.ip_address import (
    run as ip_address,
)
from ocmoss.events.wifi_information import (
    run as wifi_information,
)
from ocmoss.events.wifi_password import (
    run as wifi_password,
)

def main() -> None:
    """
    Start the OCMOSS SDK.
    """

    # ===============================
    # Version 1.0
    # ===============================

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

    # ===============================
    # Version 2.0
    # ===============================

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
    print()

    # ===============================
    # Version 3.0
    # ===============================

    print("══════════════════════════════════════")
    print("OCMOSS")
    print("Version 3.0")
    print("Network Monitoring")
    print("══════════════════════════════════════")
    print()

    network_information()
    print()

    internet_status()
    print()

    ip_address()
    print()

    wifi_information()
    print()

    wifi_password()
    print()

    print("══════════════════════════════════════")
    print("       Version 3.0 Completed")
    print("══════════════════════════════════════")


if __name__ == "__main__":
    main()