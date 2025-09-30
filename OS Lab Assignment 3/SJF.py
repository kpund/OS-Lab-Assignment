# SJF: Processes with the shortest burst time are executed first.

# CODE: 

def sjf(processes, arrival_times, burst_times):
    n = len(processes)
    completed = [False] * n
    current_time = 0
    completed_count = 0

    start_times = [0] * n
    completion_times = [0] * n
    waiting_times = [0] * n
    turnaround_times = [0] * n

    while completed_count < n:
        # Select process with minimum burst time among those that have arrived and not completed
        idx = -1
        min_burst = float('inf')
        for i in range(n):
            if arrival_times[i] <= current_time and not completed[i]:
                if burst_times[i] < min_burst:
                    min_burst = burst_times[i]
                    idx = i

        if idx == -1:
            current_time += 1
        else:
            start_times[idx] = current_time
            completion_times[idx] = current_time + burst_times[idx]
            turnaround_times[idx] = completion_times[idx] - arrival_times[idx]
            waiting_times[idx] = turnaround_times[idx] - burst_times[idx]
            current_time += burst_times[idx]
            completed[idx] = True
            completed_count += 1

    print("Process\tArrival\tBurst\tStart\tCompletion\tWaiting\tTurnaround")
    for i in range(n):
        print(f"{processes[i]}\t{arrival_times[i]}\t{burst_times[i]}\t{start_times[i]}\t{completion_times[i]}\t\t{waiting_times[i]}\t{turnaround_times[i]}")

# Example usage:
processes = ['P1', 'P2', 'P3']
arrival_times = [0, 1, 2]
burst_times = [6, 8, 7]
sjf(processes, arrival_times, burst_times)
