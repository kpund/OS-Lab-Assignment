n = int(input("Enter number of processes: "))
processes = []
for i in range(n):
    bt = int(input(f"Enter Burst Time for Process {i+1}: "))
    pr = int(input(f"Enter Priority for Process {i+1} (lower = higher priority): "))
    processes.append([i+1, bt, pr])

# Sort by priority
processes.sort(key=lambda x: x[2])

waiting_time = [0] * n
turnaround_time = [0] * n

# Calculate waiting time and turnaround time
for i in range(1, n):
    waiting_time[i] = waiting_time[i-1] + processes[i-1][1]

for i in range(n):
    turnaround_time[i] = waiting_time[i] + processes[i][1]

avg_wt = sum(waiting_time) / n
avg_tat = sum(turnaround_time) / n

print("\nProcess\tBurst Time\tPriority\tWaiting Time\tTurnaround Time")
for i in range(n):
    print(f"P{processes[i][0]}\t{processes[i][1]}\t\t{processes[i][2]}\t\t{waiting_time[i]}\t\t{turnaround_time[i]}")

print(f"\nAverage Waiting Time: {avg_wt:.2f}")
print(f"Average Turnaround Time: {avg_tat:.2f}")
