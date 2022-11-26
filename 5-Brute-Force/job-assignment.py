import time

def assign(people, n):
    result = []
    if n == 1:
        for i in people:
            result.append([i])
    elif n > 1:
        for i in range(len(people)):
            curr = [i for i in people]
            curr.remove(people[i])
            for p in assign(curr, n - 1):
                result.append([people[i]] + p)
    return result

def jobAssignment(assignList):
    minC = 300
    ja = []
    for a in assignList:
        c = 0
        for i in range(len(a)):
            c += cost[i][a[i]]
        if minC > c:
            minC = c
        ja.append([a, c])

    for j in ja:
        if j[1] == minC:
            for i in range(len(j[0])):
                print("Person %d: Job %d" % (i, j[0][i]))
    print("Minimum Cost:", minC)

cost = [
    [13, 6, 7, 12, 14, 15, 10, 11, 15, 4],
    [8, 14, 11, 9, 6, 14, 7, 9, 16, 12],
    [10, 8, 10, 10, 8, 15, 11, 5, 7, 9],
    [13, 13, 16, 9, 13, 16, 15, 9, 14, 16],
    [11, 4, 9, 14, 12, 11, 5, 16, 8, 14],
    [7, 10, 12, 13, 4,11, 16, 12, 15, 9],
    [6, 11, 10, 11, 13,15, 7, 16,11, 12],
    [7, 15, 5, 10, 4, 16, 12, 4, 10, 16],
    [5, 14, 10, 15, 8, 8, 8, 14, 14, 4],
    [8, 11, 4, 16, 8, 12, 4, 14, 9, 6]
]

people = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

start = time.time()
jobAssignment(assign(people, 10))
print("Running time: %.9f seconds" % (time.time() - start))
