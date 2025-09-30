
# FCFS (First Come, First Server): Processes are executed in the order they arrive.

# Code:

def fcfs(processes, arrival_times, burst_times):
    n = len(processes)
    start_times = [0] * n
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n

    current_time = 0
    for i in range(n):
        if current_time < arrival_times[i]:
            current_time = arrival_times[i]
        start_times[i] = current_time
        completion_times[i] = current_time + burst_times[i]
        turnaround_times[i] = completion_times[i] - arrival_times[i]
        waiting_times[i] = turnaround_times[i] - burst_times[i]
        current_time += burst_times[i]

    print("Process\tArrival\tBurst\tStart\tCompletion\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{start_times[i]}\t{completion_times[i]}\t\t{waiting_times[i]}\t{turnaround_times[i]}")

# Example usage:
processes = ['P1', 'P2', 'P3']
arrival_times = [0, 2, 4]
burst_times = [5, 3, 1]
fcfs(processes, arrival_times, burst_times)
