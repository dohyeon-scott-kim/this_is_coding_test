# chapter 07 Sequential Search

# 순차 탐색
def sequential_search(n, target, array):
    for i in range(n):
        if array[i] == target:
            return i + 1

input_data = input().split()
n = int(input_data[0])
target = input_data[1]

array = input().split()

print(sequential_search(n, target, array))

# 이진 탐색

def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    if array[mid] == target:
        return mid
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)
if result == None:
    print('원소가 존재하지 않습니다.')
else:
    print(result + 1)

# 빠르게 입력받기
import sys
input_data = sys.stdin.readline().rstrip()

print(input_data)

# 실전문제 1
## 내 답안
n_total_parts = int(input())
total_parts = list(map(int, input().split()))

n_needed_parts = int(input())
needed_parts = list(map(int, input().split()))

total_parts.sort()

def binary_search(array, target, start, end):
    if start > end:
        return print('no', end = ' ')
    mid = (start + end) // 2
    if target == array[mid]:
        return print('yes', end = ' ')
    elif target < array[mid]:
        return binary_search(array, target, start, mid - 1)
    else:
        return binary_search(array, target, mid + 1, end)

for i in needed_parts:
    binary_search(total_parts, i, 0, n_total_parts - 1)

## 답안 1(이진 탐색)
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + mid) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

n = int(input())
array = list(map(int, input().split()))
array.sort()

m = int(input())
x = list(map(int, input().split()))

for i in x:
    result = binary_search(array, i, 0, n - 1)
    if result != None:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

## 답안 2(계수 정렬)
total_part_list = [0] * 1000001
n = int(input())
for i in input().split():
    total_part_list[int(i)] = 1

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if total_part_list[i] == 1:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

## 답안 3(집합 자료형)
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x:
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')

# 실전문제 2

n_ricecake, length = map(int, input().split())
height_ricecake = list(map(int, input().split()))

height_ricecake.sort()

start = 0
end = max(height_ricecake)

final_cut = 0
while start <= end:
    total_length = 0
    cut = (start + end) // 2
    for i in height_ricecake:
        if i > cut:
            total_length += (i - cut)
    if total_length >= target:
        final_cut = cut
        start = cut + 1
    else:
        end = cut - 1

print(final_cut)
