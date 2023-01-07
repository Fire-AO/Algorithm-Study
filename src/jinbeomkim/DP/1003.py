# BOJ 1003 피보나 함수 실버3
#https://www.acmicpc.net/problem/1003

T = int(input())

for _ in range(T):
    n = int(input())

    dp = [[0] * 2 for _ in range(n + 2)]

    dp[0][0] = 1
    dp[1][1] = 1

    i = 0
    while n >= i + 2:
        dp[i + 2][0] = dp[i + 1][0] + dp[i][0]
        dp[i + 2][1] = dp[i + 1][1] + dp[i][1]
        i += 1

    print(dp[n][0], end=' ')
    print(dp[n][1])