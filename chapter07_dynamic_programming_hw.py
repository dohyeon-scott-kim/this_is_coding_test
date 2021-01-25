# 피보나치 함수
def fibonacci(n):
    if n == 0:
        print('0')
        return 0
    elif n == 1:
        print('1')
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

d = [[0, 0] for i in range(41)]
d[0] = [1, 0]
d[1] = [0, 1]

def n_of_0_and_1(n):
    for i in range(2, n + 1):
        d[i] = [x + y for x, y in zip(d[i-1], d[i-2])]
    return(d[n])


t = int(input())
for i in range(t):
    n = int(input())
    print(*n_of_0_and_1(n))

# 쉬운 계단 수

n = int(input())
d = [[0] * 10 for i in range(n + 1)]
d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

def stair_n(n):
    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                d[i][j] = d[i - 1][j + 1]
            elif j == 9:
                d[i][j] = d[i - 1][j - 1]
            else:
                d[i][j] = d[i - 1][j - 1] + d[i - 1][j + 1]
    return sum(d[n]) % 1000000000

print(stair_n(n))

# 연속합
## 답안(메모리 초과)
n = int(input())
n_list = list(map(int, input().split()))

d = [[] for i in range(n)]
d[0].append(n_list[0])

for i in range(1, n ):
    for j in d[i-1]:
        d[i].append(j + n_list[i])
    d[i].append(n_list[i])

max = -1001

for i in d:
    for j in i:
        if j > max:
            max = j

print(max)

## 답안
n = int(input())
n_list = list(map(int, input().split()))

d = [0] * n

d[0] = n_list[0]

for i in range(1, n):
    d[i] = max(n_list[i], d[i - 1] + n_list[i])
print(max(d))
