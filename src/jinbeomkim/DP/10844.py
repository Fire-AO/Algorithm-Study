# BOJ 10844 쉬운 계단 실버1
#https://www.acmicpc.net/problem/15486

#풀이: https://jinbeomk.tistory.com/3

n = int(input())
d = [[0 for _ in range(10)] for _ in range(n)]

# 첫번째 자릿수는 초기화해준다.
for i in range(1, 10):
    d[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            d[i][1] += d[i-1][j]
        elif j == 9:
            d[i][8] += d[i-1][j]
        else:
            d[i][j-1] += d[i-1][j]
            d[i][j+1] += d[i-1][j]

print(sum(d[n-1])%10**9)
