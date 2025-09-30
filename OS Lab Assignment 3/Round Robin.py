# Round Robin: Each process gets a fixed time quantum. Processes are executed in a cyclic order.

# CODE: 

from collections import deque

def round_robin(processes, arrival_times, burst_times, time_quantum):
    n = len(processes)
    remaining_bt = burst_times[:]
    current_time = 0
    waiting_times = [0] * n
    completion_times = [0] * n
    turnaround_times = [0] * n
    start_times = [-1] * n

    queue = deque()
    visited = [False] * n

    # Add processes that arrive at time 0
    for i in range(n):
        if arrival_times[i] <= current_time and not visited[i]:
            queue.append(i)
            visited[i] = True

    while queue:
        i = queue.popleft()

        if start_times[i] == -1:
            start_times[i] = max(current_time, arrival_times[i])
            current_time = start_times[i]

        exec_time = min(time_quantum, remaining_bt[i])
        remaining_bt[i] -= exec_time
        current_time += exec_time

        # Add newly arrived processes to queue
        for j in range(n):
            if arrival_times[j] <= current_time and not visited[j]:
                queue.append(j)
                visited[j] = True

        if remaining_bt[i] > 0:
            queue.append(i)
        else:
            completion_times[i] = current_time
            turnaround_times[i] = completion_times[i] - arrival_times[i]
            waiting_times[i] = turnaround_times[i] - burst_times[i]

    print("Process\tArrival\tBurst\tStart\tCompletion\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{start_times[i]}\t{completion_times[i]}\t\t{waiting_times[i]}\t{turnaround_times[i]}")

# Example usage:
processes = ['P1', 'P2', 'P3']
arrival_times = [0, 1, 2]
burst_times = [10, 5, 8]
time_quantum = 3
round_robin(processes, arrival_times, burst_times, time_quantum)
