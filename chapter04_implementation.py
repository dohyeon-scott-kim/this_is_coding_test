# Chapter04 구현(implementation)

# 예제 4-1

# n = int(input())
# x = 1
# y = 1
# for j in map(str, input().split()):
#     if j == 'L' and x - 1 >= 1:
#         y -= 1
#     elif j == 'R' and x + 1 <= n:
#         y += 1
#     elif j == 'U' and y - 1 >= 1:
#         x -= 1
#     elif j == 'D' and y + 1 <= n:
#         x += 1
# print(x, y)

n = int(input())
x, y = 1, 1
plans = input().split()

move_types = ['L','R','U','D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for plan in plans:
    for i in range(len(move_types)):
        if plan == move_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n:
        continue
    else:
        x, y = nx, ny

print(x, y)

# 예제 4-2

n = int(input())
count = 0
for i in range(n+1):
    for j in range(60):
        for s in range(60):
            if '3' in str(i) + str(j) + str(s):
                count += 1

print(count)

# 실전문제 1
y_axis = {
          'a' : 1,
          'b' : 2,
          'c' : 3,
          'd' : 4,
          'e' : 5,
          'f' : 6,
          'g' : 7,
          'h' : 8
}

index = str(input())
plans = ['UUL', 'UUR', 'DDL', 'DDR', 'LLU', 'LLD', 'RRU', 'RRD']

move_types = ['L','R','U','D']
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
count = 0

for plan in plans:
    x, y = y_axis.get(index[0]), int(index[1])
    for i in plan:
        for j in range(len(move_types)):
            if i == move_types[j]:
                x += dx[j]
                y += dy[j]
    if x >= 1 and x <= 8 and y >= 1 and y <= 8:
        count += 1

print(count)

# 답압
index = input()
x = int(index[1])
y = ord(index[0]) - ord('a') + 1

plans = [
        [+2, +1],
        [+2, -1],
        [-2, +1],
        [-2, -1],
        [-1, +2],
        [+1, +2],
        [-1, -2],
        [+1, -2]
        ]

count = 0

for plan in plans:
    nx = x + plan[0]
    ny = y + plan[1]
    if nx >= 1 and ny >= 1 and nx <= 8 and ny <= 8:
        count += 1

print(count)

# 실전문제 2
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, input().split())
x, y, direction = map(int, input().split())

maps = []
for i in range(n):
    maps.append(list(map(int, input().split())))

maps[x][y] = 1

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turn_time = 0

while True:
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if maps[ny][nx] == 0:
        count += 1
        maps[ny][nx] = 1
        x = nx
        y = ny
    else:
        turn_time += 1

    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dx[direction]
        if maps[ny][nx] == 0:
            x = nx
            y = ny
            turn_time = 0
        else:
            break

print(count)

# 백준 블랙잭

n, answer = map(int, input().split())

numbers = list(map(int, input().split()))

# added_list = []

# for i in numbers:
#     for j in numbers:
#         for k in numbers:
#             if i == j or j == k or k == i:
#                 continue
#             else:
#                 added_list.append(abs(answer -(i+j+k)))
#
# print(answer - min(added_list))
biggest_add = 0

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if numbers[i] + numbers[j] + numbers[k] > answer:
                continue
            else:
                biggest_add = max(biggest_add, numbers[i] + numbers[j] + numbers[k])

print(biggest_add)
