import heapq

graph = {
    'A': {'B': 2, 'C': 4},
    'B': {'A': 2, 'C': 3, 'D': 9, 'G': 4, 'H': 2},
    'C': {'A': 4, 'B': 3, 'D': 1, 'E': 3},
    'D': {'B': 9, 'C': 1, 'E': 3, 'F': 3, 'G': 1},
    'E': {'C': 3, 'D': 3, 'F': 2},
    'F': {'D': 3, 'E': 2, 'G': 6},
    'G': {'B': 4, 'D': 1, 'F': 6, 'H': 14},
    'H': {'B': 2, 'G': 14}
}

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])
    while queue:
        currDist, currDestination = heapq.heappop(queue)
        if distances[currDestination] < currDist:
            continue
        for newDestination, newDist in graph[currDestination].items():
            distance = currDist + newDist
            if distance < distances[newDestination]:
                distances[newDestination] = distance
                heapq.heappush(queue, [distance, newDestination])
    return distances


print(dijkstra(graph, 'A'))