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

# 이분 그래프
from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    queue = deque()
    queue.append(n)
    color[n] = 1
    while queue:
        popout = queue.popleft()
        for i in graph_info[popout]:
            if color[i] == 0:
                color[i] = 3 - color[popout]
                queue.append(i)
            elif color[i] == color[popout]:
                return False
    return True

K = int(input())
for i in range(K):
    V, E = map(int, input().split())
    graph_info = [[] for i in range(V + 1)]
    color = [0 for i in range(V + 1)]
    for j in range(E):
        start, end = map(int, input().split())
        graph_info[start].append(end)
        graph_info[end].append(start)
    ans = 'YES'
    for k in range(1, V+1):
        if color[k] == 0:
            if bfs(k) == False:
                ans = 'NO'
                break
    print(ans)

# DFS와 BFS
from collections import deque

def bfs(V):
    queue = deque()
    queue.append(V)
    visited_bfs[V] = 1
    while queue:
        pop_out = queue.popleft()
        bfs_list.append(pop_out)
        for i in graph_info[pop_out]:
            if visited_bfs[i] == 0:
                visited_bfs[i] = 1
                queue.append(i)
    return bfs_list

def dfs(V):
    visited_dfs[V] = 1
    dfs_list.append(V)
    for i in graph_info[V]:
        if visited_dfs[i] == 0:
            dfs(i)
    return dfs_list

N, M, V = map(int, input().split())

graph_info = [[] for i in range(N + 1)]
visited_dfs = [0 for i in range(N + 1)]
visited_bfs = [0 for i in range(N + 1)]
dfs_list = []
bfs_list = []

for i in range(M):
    start, end = map(int, input().split())
    graph_info[start].append(end)
    graph_info[end].append(start)

for i in range(N):
    graph_info[i].sort()

print(*dfs(V))
print(*bfs(V))

# 바이러스
N = int(input())
network_N = int(input())

network_info = [[] for i in range(N + 1)]
virus_comp = [0 for i in range(N + 1)]

for i in range(network_N):
    start, end = map(int, input().split())
    network_info[start].append(end)
    network_info[end].append(start)

def dfs(V):
    virus_comp[V] = 1
    for i in network_info[V]:
        if virus_comp[i] == 0:
            dfs(i)

dfs(1)

print(sum(virus_comp)-1)
