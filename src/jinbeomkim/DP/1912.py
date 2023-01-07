# BOJ 1912 연속합 실버2
#https://www.acmicpc.net/problem/1912

n = int(input())
l = list(map(int, input().split()))

res = l[0]

for i in range(1, n):
    if l[i] + l[i-1] > 0:
        l[i] += l[i-1]
        res = max(res, l[i])
    elif l[i] > res:
        res = l[i]
    else:
        l[i] = 0

print(res)