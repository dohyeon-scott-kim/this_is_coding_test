# 수 정렬하기 3

## 선택정렬
N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))

for i in range(len(n_list)):
    min_index = i
    for j in range(i + 1, len(n_list)):
        if n_list[i] > n_list[j]:
            min_index = j
    n_list[i], n_list[min_index] = n_list[min_index], n_list[i]

for i in range(N):
    print(n_list[i])
## 삽입정렬
N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))

for i in range(len(n_list)):
    for j in range(i, 0, -1):
        if n_list[j] < n_list[j-1]:
            n_list[j], n_list[j-1] = n_list[j-1], n_list[j]
        else:
            break

for i in range(N):
    print(n_list[i])
## 퀵정렬
N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))

def quick_sort(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]
    left = [x for x in tail if x <= pivot]
    right = [x for x in tail if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

sorted_list =  quick_sort(n_list)

for i in sorted_list:
    print(i)
## 계수정렬
import sys
input = sys.stdin.readline
N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))

count = [0] * (max(n_list) + 1)

for i in range(len(n_list)):
    count[n_list[i]] += 1

for i in range(len(count)):
    for j in range(count[i]):
        print(i)
## 파이썬 라이브러리
import sys
input = sys.stdin.readline

N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))
n_list.sort()
for i in range(N):
    sys.stdin.write(n_list[i])

## 정답
import sys
input = sys.stdin.readline
N = int(input())
count = [0] * 10001

for i in range(N):
    numb = int(input())
    count[numb] += 1

for i in range(10001):
    for j in range(count[i]):
        print(i)

# 통계학
from collections import Counter
import sys
input = sys.stdin.readline

N = int(input())
n_list = []
for i in range(N):
    n_list.append(int(input()))

mean = sum(n_list)/N

n_list.sort()
median = n_list[N//2]

counted_list = Counter(n_list)

sorted_list = sorted(counted_list.items(), key = lambda x: x[1], reverse = True)

if N != 1:
    if sorted_list[0][1] == sorted_list[1][1]:
        mode = sorted_list[1][0]
    else:
        mode = sorted_list[0][0]
else:
    mode = sorted_list[0][0]

rng = max(n_list) - min(n_list)

print('{:.0f}'.format(mean))
print(median)
print(mode)
print(rng)
