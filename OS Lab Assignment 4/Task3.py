# MFT (Multiprogramming with Fixed Tasks)

memory_size = int(input("Enter total memory size (KB): "))
partition_size = int(input("Enter partition size (KB): "))
num_partitions = memory_size // partition_size
remaining_memory = memory_size % partition_size

print(f"\nNumber of partitions: {num_partitions}")
print(f"Remaining memory (unused): {remaining_memory} KB\n")

processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    p = int(input(f"Enter memory required for process {i+1} (KB): "))
    processes.append(p)

allocated = [False]*n
internal_frag = 0
external_frag = 0

for i in range(n):
    if i < num_partitions:
        if processes[i] > partition_size:
            print(f"Process {i+1} of size {processes[i]} KB cannot be allocated.")
        else:
            allocated[i] = True
            internal_frag += partition_size - processes[i]
            print(f"Process {i+1} allocated in Partition {i+1}.")

    else:
        print(f"No free partition for Process {i+1}.")

print(f"\nTotal Internal Fragmentation = {internal_frag} KB")
print(f"Total External Fragmentation = {remaining_memory} KB")


# MFT (Multiprogramming with Fixed Tasks)

memory_size = int(input("Enter total memory size (KB): "))
partition_size = int(input("Enter partition size (KB): "))
num_partitions = memory_size // partition_size
remaining_memory = memory_size % partition_size

print(f"\nNumber of partitions: {num_partitions}")
print(f"Remaining memory (unused): {remaining_memory} KB\n")

processes = []
n = int(input("Enter number of processes: "))

for i in range(n):
    p = int(input(f"Enter memory required for process {i+1} (KB): "))
    processes.append(p)

allocated = [False]*n
internal_frag = 0
external_frag = 0

for i in range(n):
    if i < num_partitions:
        if processes[i] > partition_size:
            print(f"Process {i+1} of size {processes[i]} KB cannot be allocated.")
        else:
            allocated[i] = True
            internal_frag += partition_size - processes[i]
            print(f"Process {i+1} allocated in Partition {i+1}.")

    else:
        print(f"No free partition for Process {i+1}.")

print(f"\nTotal Internal Fragmentation = {internal_frag} KB")
print(f"Total External Fragmentation = {remaining_memory} KB")
