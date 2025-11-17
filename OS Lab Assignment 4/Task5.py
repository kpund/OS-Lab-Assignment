import multiprocessing
import time
import logging
from datetime import datetime

# --- Configure logging ---
logging.basicConfig(
    filename="system_startup.log",
    level=logging.INFO,
    format="%(asctime)s - %(processName)s - %(message)s"
)

# --- Define dummy startup process ---
def system_service(service_name, duration):
    logging.info(f"{service_name} started.")
    time.sleep(duration)  # Simulate time taken for startup
    logging.info(f"{service_name} finished startup.")

# --- Main simulation ---
if __name__ == "__main__":
    print("=== System Startup Simulation Initiated ===\n")

    # Define system services (name, duration)
    services = [
        ("Network Manager", 2),
        ("Database Service", 3),
        ("Authentication Service", 1.5),
        ("File System Monitor", 2.5),
        ("Security Daemon", 1)

    ]

    # Create process list
    processes = []
    for name, duration in services:
        p = multiprocessing.Process(target=system_service, args=(name, duration), name=name)
        processes.append(p)
        p.start()  # Start the process

    # Wait for all to finish
    for p in processes:
        p.join()

    print("=== All System Services Started Successfully ===")
    print("Logs saved in 'system_startup.log'")
