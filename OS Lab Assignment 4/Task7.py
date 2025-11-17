import os
import platform
import subprocess

def detect_vm():
    print("=== Virtual Machine Detection ===")

    try:
        manufacturer = subprocess.getoutput("sudo dmidecode -s system-manufacturer")
        product_name = subprocess.getoutput("sudo dmidecode -s system-product-name")

        print(f"Manufacturer: {manufacturer}")
        print(f"Product Name: {product_name}")

        vm_indicators = ["virtualbox", "vmware", "qemu", "kvm", "hyper-v", "xen"]

        if any(vm in manufacturer.lower() for vm in vm_indicators) or \
           any(vm in product_name.lower() for vm in vm_indicators):
            print("The system appears to be running inside a Virtual Machine.")
        else:
            print("The system appears to be running on physical hardware.")
    except Exception as e:
        print("Error detecting VM:", e)

if __name__ == "__main__":
    detect_vm()
