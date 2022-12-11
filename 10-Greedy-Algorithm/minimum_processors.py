n = int(input("- Job 수: "))
jobs = []

for i in range(n):
    start, end = map(int, input("- Job [%d] 시작 시간, 끝 시간: " % i).split())
    jobs.append([start, end])

cpu = []

cpu.append(jobs[0][1]) # 첫 CPU에 첫 job 할당

for i in range(1, n):
    assigned = False
    for j in range(len(cpu)):
        if cpu[j] <= jobs[i][0]:
            cpu[j] = jobs[i][1] # 해당 CPU에 job 할당
            assigned = True
            break
    if not assigned:
        cpu.append(jobs[i][1]) # 새 CPU에 job 할당

print("- 필요 CPU 수: %d" % len(cpu))
print("- 최종 종료 시간: %d" % max(cpu))