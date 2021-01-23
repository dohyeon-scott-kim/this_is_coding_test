# 수찾기

def binary_search(array, target, start, end):
        if start > end:
              return 0
        mid = (start + end) // 2
        if array[mid] == target:
            return 1
        elif array[mid] < target:
            return binary_search(array, target, mid + 1, end)
        else:
            return binary_search(array, target, start, mid - 1)

n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

for i in range(m):
    print(binary_search(n_list, m_list[i], 0, n - 1))

# 랜선 자르기

k, n = map(int, input().split())
line_list = []
for i in range(k):
    line_list.append(int(input()))

start = 1
end = max(line_list)

final_cut = 0

while start <= end:
    mid = (start + end) // 2
    line_n = 0
    for i in line_list:
        line_n += i % mid
    if line_n >= n:
        final_cut = mid
        end = mid - 1
    else:
        start = mid + 1

print(final_cut)

# 나무 자르기(pypy3)

n, m = map(int, input().split())
tree_list = list(map(int, input().split()))

start = 0
end = max(tree_list)

cutter_length = 0

while start <= end:
    mid = (start + end) // 2
    total_length = 0
    for i in tree_list:
        if i > mid:
            total_length += (i - mid)
    if total_length >= m:
        cutter_length = mid
        start = mid + 1
    else:
        end = mid - 1

print(cutter_length)
