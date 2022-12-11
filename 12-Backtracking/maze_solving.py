def findPath(x, y):
    maze[x][y] = 2
    print((x, y), end=" ")
    if x == 4 and y == 4:
        print("Success!")
        return 1

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < 5 and 0 <= ny < 5:
            if maze[nx][ny] == 1:
                res = findPath(nx, ny)
                if res == 1:
                    return
                return

maze = [
    [1, 1, 0, 1, 1],
    [0, 1, 0, 1, 0],
    [1, 1, 1, 1, 0],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 1, 1]
]

visited = [[False] * 5 for _ in range(5)]
start = [0, 0]
finish = [4, 4]

findPath(0, 0)
