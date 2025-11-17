import os
import subprocess

scripts = [
    r"/mnt/c/Users/Kashish Pundir/OneDrive/Desktop/Python/Typecasting.py",
    r"/mnt/c/Users/Kashish Pundir/OneDrive/Desktop/Python/String.py"
]

print("=== Batch Processing Simulation Started ===\n")

for script in scripts:
    if os.path.exists(script):
        print(f"Executing {script}...")
        result = subprocess.run(["python", script], capture_output=True, text=True)

        print(f"--- Output of {script} ---")
        print(result.stdout)
        if result.stderr:
            print(f"--- Errors in {script} ---")
            print(result.stderr)
        print("-" * 40)
    else:
        print(f"⚠️ File not found: {script}")
    print()
print("=== Batch Processing Simulation Completed ===")
