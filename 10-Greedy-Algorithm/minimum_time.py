def minimumTime(jobs):
    for i in range(len(cpu)):
        cpu[i] = jobs[i]
    for i in range(len(cpu), len(jobs)):
        minIdx = cpu.index(min(cpu))
        cpu[minIdx] += jobs[i]
    return max(cpu)

jobs = list(map(int, input("- Job 목록: ").split()))
cpu = [0] * int(input("- Processor 수: "))

shortFirst = minimumTime(sorted(jobs))
longFirst = minimumTime(sorted(jobs, reverse=True))

print("- Shortest Job First Completion Time:", shortFirst)
print("- Longest Job First Completion Time:", longFirst)