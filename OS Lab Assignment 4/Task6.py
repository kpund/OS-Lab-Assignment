import os
def main():
    print("=== System Calls and IPC Simulation ===")

    # Create a pipe (two file descriptors)
    read_fd, write_fd = os.pipe()

    # Fork a new process
    pid = os.fork()

    if pid > 0:
        # 🟢 Parent process
        os.close(read_fd)  # Close unused read end
        message = "Hello from Parent Process!"
        print(f"[Parent] Sending message to child: {message}")

        # Encode and write message into pipe
        os.write(write_fd, message.encode())
        os.close(write_fd)  # Close write end after sending

        # Wait for child process to finish
        os.wait()
        print("[Parent] Child process has finished execution.")

    else:
        # 🔵 Child process
        os.close(write_fd)  # Close unused write end

        # Read message from parent through pipe
        read_message = os.read(read_fd, 1024).decode()
        print(f"[Child] Received message from parent: {read_message}")

        # Simulate exec() — replacing the process with a new one
        print("[Child] Executing new program using exec()...")
        os.execlp("echo", "echo", "Child process executed new program via exec()!")

        # (The following line won’t execute since exec() replaces the current process)
        os.close(read_fd)

if __name__ == "__main__":
    main()
