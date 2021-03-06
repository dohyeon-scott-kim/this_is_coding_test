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

# 문제 요약
## 컴퓨터 바이러스인 웜바이러스: 네트워크를 통해 전파
## 한 컴퓨터가 웜바이러스에 걸리면 그 컴퓨터와 네트워상에 연결된 모든 컴퓨터는 웜바이러스에 걸림
## 1번 컴퓨터가 웜바이러스에 걸렸을 때 1번 컴퓨터를 통해 웜바이러스에 걸리는 컴퓨터의 수 출력

N = int(input()) # 컴퓨터의 수 7
network_N = int(input()) # 컴퓨터 쌍의 수 6

network_info = [[] for i in range(N + 1)]
# [[], [], [], [], [], [], [], [], []]
# 1, 2, 3, ... 컴퓨터와 연결된 네트워크 정보를 저장할 list 생성
virus_comp = [0 for i in range(N + 1)]
# 바이러스가 걸렸는 지 정보를 저장할 list

for i in range(network_N):
    start, end = map(int, input().split())
    network_info[start].append(end)
    network_info[end].append(start)
# network의 정보를 다 저장
# 1 2
# start = 1 end = 2
# network_info[1] = 2 저장
# network_info[2] = 1 저장
# ...

def dfs(V):
    virus_comp[V] = 1 # virus가 걸렸다고 저장
    for i in network_info[V]: # V와 연결된 컴퓨터 중
        if virus_comp[i] == 0: # 바이러스에 걸리지 않은 컴퓨터만 다시 dfs 돌리기
            dfs(i)

dfs(1) # 1번 컴퓨터가 바이러스에 걸렸을 때 바이러스에 걸리는 컴퓨터는 virus_comp에 저장

print(sum(virus_comp)-1)
# 문제 상에서 1번 컴퓨터를 통해 웜 바이러스에 걸리는 컴퓨터의 수 출력
# 따라서, virus_comp를 다 합한 후 1번 컴퓨터 자신은 제외해야되기 때문에 -1

# 단지번호 붙이기

N = int(input())
graph = []
for i in range(N):
    graph.append(list(map(int, input())))

apt_cplx = [[0] * N for i in range(N)]
count = 1
def dfs(x, y):
    global count
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    if graph[x][y] == 1:
        if apt_cplx[x][y] == 0:
            apt_cplx[x][y] = count
            dfs(x - 1, y)
            dfs(x + 1, y)
            dfs(x, y - 1)
            dfs(x, y + 1)
            return True
    return False

for i in range(N):
    for j in range(N):
        if dfs(i, j) == True:
            count += 1

print(count - 1)
numb_apt = []
for i in range(1, count):
    n = 0
    for j in range(N):
        n += apt_cplx[j].count(i)
    numb_apt.append(n)

numb_apt.sort()

for i in range(count-1):
    print(numb_apt[i])
