import time

# 모든 노드가 이어져 있으므로 경로 리스트를 순열로 생성
def path(nodeList, n):
    result = []
    if n == 1:
        for i in nodeList:
            result.append([i])
    elif n > 1:
        for i in range(len(nodeList)):
            currPath = [i for i in nodeList]
            currPath.remove(nodeList[i])
            for p in path(currPath, n - 1):
                result.append([nodeList[i]] + p)
    return result

def TSP(graph, pathList):
    minDist = 50
    routeList = []

    for path in pathList:
        dist = 0
        path.insert(0, 0)
        path.insert(5, 0)
        for i in range(len(path) - 1):
            dist += graph[path[i]][path[i + 1]]
        if minDist > dist:
            minDist = dist
        routeList.append([path, dist])

    for route in routeList:
        if route[1] == minDist:
            print('path: %s - dist: %d' % (route[0], route[1]))

nodeList = [1, 2, 3, 4]
graph = [
    [0, 2, 3, 2, 3],
    [2, 0, 3, 4, 1],
    [3, 3, 0, 2, 4],
    [2, 4, 2, 0, 5],
    [3, 1, 4, 5, 0]
]

start = time.time()
TSP(graph, path(nodeList, 4))
print("Running time: %.9f seconds" % (time.time() - start))
