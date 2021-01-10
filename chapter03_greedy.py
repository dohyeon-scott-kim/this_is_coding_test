# Chapter 03 그리디(greedy)

# 실전문제 1

# 답안 1
N, M, K = map(int, input().split())
numb_list = []
for i in map(int, input().split()):
    numb_list.append(i)
numb_list.sort()
per_cycle = numb_list[-1] * K + numb_list[-2]
Q, R = divmod(M, K + 1)
biggest_total = per_cycle * Q + numb_list[-1] * R
print(biggest_total)

# 답안 2
n, m, k = map(int, input().split())
data = list(map(int, input().split()))
data.sort()
biggest_numb = data[-1]
second_biggest_numb = data[-2]
result = 0

while True:
    for i in range(k):
        if m == 0:
            break
        result += biggest_numb
        m -= 1
    if m == 0:
        break
    result += second_biggest_numb
    m -= 1

print(result)

# 실전문제 2
# 답안 1
m, n = map(int, input().split())
smallest_numb_list = []
for i in range(m):
    numb_list = []
    for j in map(int, input().split()):
        numb_list.append(j)
    # numb_list.sort()
    # smallest_numb_list.append(numb_list[0])
    smallest_numb_list.append(min(numb_list))
# smallest_numb_list.sort()
# print(smallest_numb_list[-1])
print(max(smallest_numb_list))

# 답안 2
n, m = map(int, input().split())
result = 0

for i in range(n):
    data = list(map(int, input().split()))
    min_value = min(data)
    result = max(result, min_value)

print(result)

# 실전문제 3
# 답안 1

n, k = map(int, input().split())

count = 0
while True:
    a, b = divmod(n, k)
    n = a
    count += b + 1
    if n == 1:
        break
print(count)

# 백준 그리디 Bohemian Rhaksody

# h, w, n = map(int, input().split())
# x_min = 0
# x_max = h
# y_min = 0
# y_max = w
# for i in range(n):
#     x, y = map(int,input().split())
#     if x <= x_min or x >= x_max or y <= y_min or y >= y_max:
#         continue
#     area_list = left_area, right_area, below_area, above_area = [(x - x_min) * (y_max - y_min),
#                                                                 (x_max - x) * (y_max - y_min),
#                                                                 (x_max - x_min) * (y - y_min),
#                                                                 (x_max - x_min) * (y_max - y)]
#     if left_area == max(area_list):
#         x_max = x
#     elif right_area == max(area_list):
#         x_min = x
#     elif below_area == max(area_list):
#         y_max = y
#     elif above_area == max(area_list):
#         y_min = y
#
# max_area = (x_max - x_min) * (y_max - y_min)
# print(max_area)

# 백준 그리디 회의실 배정
n = int(input())
meeting = []
for i in range(n):
    meeting.append(list(map(int, input().split())))
meeting.sort()
meeting.sort(key = lambda x: x[1])
st = meeting[1][0]
et = meeting[1][1]
count = 1
for s in meeting:
    if s[0] >= et:
        st = s[0]
        et = s[1]
        count += 1
    else:
        continue
print(count)
