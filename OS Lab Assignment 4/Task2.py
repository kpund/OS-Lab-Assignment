# Memory Allocation Simulation: First-Fit, Best-Fit, Worst-Fit

def first_fit(blocks, processes):
    allocation = [-1] * len(processes)
    temp_blocks = blocks.copy()

    for i in range(len(processes)):
        for j in range(len(temp_blocks)):
            if temp_blocks[j] >= processes[i]:
                allocation[i] = j
                temp_blocks[j] -= processes[i]
                break
    return allocation


def best_fit(blocks, processes):
    allocation = [-1] * len(processes)
    temp_blocks = blocks.copy()

    for i in range(len(processes)):
        best_idx = -1
        for j in range(len(temp_blocks)):
            if temp_blocks[j] >= processes[i]:
                if best_idx == -1 or temp_blocks[j] < temp_blocks[best_idx]:
                    best_idx = j
        if best_idx != -1:
            allocation[i] = best_idx
            temp_blocks[best_idx] -= processes[i]
    return allocation


def worst_fit(blocks, processes):
    allocation = [-1] * len(processes)
    temp_blocks = blocks.copy()

    for i in range(len(processes)):
        worst_idx = -1
        for j in range(len(temp_blocks)):
            if temp_blocks[j] >= processes[i]:
                if worst_idx == -1 or temp_blocks[j] > temp_blocks[worst_idx]:
                    worst_idx = j
        if worst_idx != -1:
            allocation[i] = worst_idx
            temp_blocks[worst_idx] -= processes[i]
    return allocation


# Input example
blocks = [100, 500, 200, 300, 600]
processes = [212, 417, 112, 426]
print("Memory Blocks:", blocks)
print("Processes:", processes)

# Apply algorithms
ff_allocation = first_fit(blocks, processes)
bf_allocation = best_fit(blocks, processes)
wf_allocation = worst_fit(blocks, processes)

# Print results
def print_allocation(name, allocation):
    print(f"\n{name} Allocation:")
    print("Process No.\tProcess Size\tBlock No.")
    for i in range(len(processes)):
        if allocation[i] != -1:
            print(f"{i+1}\t\t{processes[i]}\t\t{allocation[i]+1}")
        else:
            print(f"{i+1}\t\t{processes[i]}\t\tNot Allocated")

print_allocation("First Fit", ff_allocation)
print_allocation("Best Fit", bf_allocation)
print_allocation("Worst Fit", wf_allocation)
