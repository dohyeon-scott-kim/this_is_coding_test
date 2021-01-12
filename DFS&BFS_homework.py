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
visited = [[[0] * 2 for i in range(m)] for i in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0][1] = 1
    while queue:
        x, y, break_wall = queue.popleft()

        if x == n - 1 and y == m - 1:
            return visited[x][y][break_wall]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 0 and visited[nx][ny][break_wall] == 0:
                    visited[nx][ny][break_wall] = visited[x][y][break_wall] + 1
                    queue.append((nx, ny, break_wall))
                if graph[nx][ny] == 1 and break_wall == 1:
                    visited[nx][ny][0] = visited[x][y][1] + 1
                    queue.append((nx, ny, 0))
    return -1

print(bfs())
