# 피보나치 함수 소스코드

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

# 피보나치 수열 소스코드(재귀적)

d = [0] * 100

def fibo(x):
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

print(fibo(99))

# 호출되는 함수 확인

d = [0] * 100

def pibo(x):
    print('f(' + str(x) + ')', end = ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x - 1) + pibo(x - 2)
    return d[x]

pibo(6)

# 피보나치 수열 소스코드(반복적)

d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n + 1):
    d[i] = d[i - 1] + d[i - 2]

print(d[n])

# 실전문제 1

x = int(input())
d = [0] * 30001

for i in range(2, x + 1):
    d[i] = d[i - 1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i // 2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i // 3] + 1)
    if i % 5 == 0:
        d[i] = min(d[i], d[i // 5] + 1)

print(d[x])

# 실전문제 2
## 내 답안
n = int(input())

food_store_list = list(map(int, input().split()))
d = [0] * (len(food_store_list) - 1)

d[0] = food_store_list[0]
d[1] = food_store_list[1]
d[2] = food_store_list[2]

for i in range(3, len(food_store_list)):
    d[i] = food_store_list[i] + max(d[i - 2], d[i - 3])

max(d)
## 답안
n = int(input())
array = list(map(int, input().split()))

d = [0] * 100

d[0] = array[0]
d[1] = max(array[0], array[1])

for i in range(2, n):
    d[i] = max(d[i - 1], d[i - 2] + array[i])

print(d[n - 1])

# 실전문제 3

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])

# 실전문제 4
## 내 답안
n, m = map(int, input().split())
money_list = []
for i in range(n):
    money_list.append(int(input()))

money_list.sort()
money_list.reverse()

d = [0] * 10001
for i in money_list:
    d[i] = 1

for i in range(m + 1):
    d_list = []
    for j in money_list:
        if i - j >= 0 and d[i - j] != 0:
            d_list.append(d[i - j])
    if d_list == []:
        continue
    else:
        d[i] = min(d_list) + 1

if d[m] == 0:
    print('-1')
else:
    print(d[m])

## 답안
n, m = map(int, input().split())
array = []
for i in range(n):
    array.append(int(input()))

d = [10001] * (m + 1)

d[0] = 0
for i in range(n):
    for j in range(array[i], m + 1):
        if d[j - array[i]] != 10001:
            d[j] = min(d[j - array[i]] + 1, d[j])

if d[m] == 10001:
    print(-1)
else:
    print(d[m])
