# 숨바꼭질
from collections import deque

def bfs(n):
    queue = deque()
    count = 0
    queue.append([n, count])
    while queue:
        n, count = queue.popleft()
        if visited[n] == 0:
            visited[n] = 1
            if n == k:
                return count
            count += 1
            if 2 * n >= 0 and 2 * n <= 100000:
                queue.append([2*n, count])
            if n - 1 >= 0 and n - 1 <= 100000:
                queue.append([n-1, count])
            if n + 1 >= 0 and n + 1 <= 100000:
                queue.append([n+1, count])

n, k = map(int, input().split())
visited = [False] * 100001
print(bfs(n))

# 벽 부수고 이동하기
from collections import deque
n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    break_wall = 1
    queue.append((x, y, break_wall))
    while queue:
        x, y, break_wall = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= m:
                continue
            if graph[nx][ny] == 1 and break_wall == 1:
                break_wall -= 1
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny, break_wall))
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny, break_wall))
    return graph[n-1][m-1]

graph[0][0] = 1
print(bfs(0, 0))
