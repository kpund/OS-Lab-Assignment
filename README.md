**Name:** Kashish Pundir

**Roll No:** 2301420006

**Course:** Btech CSE(Data Science)

# 🖥️ Process Management in Python

This project demonstrates key Operating System process management concepts using Python, including process creation, execution, zombies & orphans, process inspection, and scheduling with priorities.

# **📌 Tasks Overview**

**Task 1: Process Creation Utility**

- Create N child processes using os.fork()

- Each child prints:

    - Its PID
  
    - Its Parent PID
  
    - A custom message
  
- The parent waits for all children using os.wait()

**Task 2: Command Execution using exec()**

- Modify Task 1 so that each child executes a Linux command (ls, date, ps, etc.)

- Use either:

  - os.execvp()
  
  - subprocess.run()
  
- Demonstrates how processes replace their execution image with a new program

**Task 3: Zombie & Orphan Processes**

- Zombie Process → Fork a child but skip wait() in the parent

- Orphan Process → Parent exits before the child finishes

- Check with:
```
ps -el | grep defunct
```
**Task 4: Inspecting Process Info from /proc**

- Take a PID as input and read:

- Process name, state, memory usage → /proc/[pid]/status

- Executable path → /proc/[pid]/exe

- Open file descriptors → /proc/[pid]/fd

**Task 5: Process Prioritization**

- Create multiple CPU-intensive child processes

- Assign different nice() values

- Observe execution order and scheduler impact

**Happy Learning!!**
