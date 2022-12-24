# BOJ 14500 퇴사 골드4
#https://www.acmicpc.net/problem/14500
'''
파이썬 파라미터는 call by reference
따라서 dfs의 경우 true 값을 준후, 바로 false 하면 구현 가능
'''

n, m = map(int, input().split())

g = [list(map(int, input().split())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

v = [[False] * m for _ in range(n)]

def dfs(x, y, l):

    if l == 3:
        return g[x][y]

    val = 0
    # ㅜ, ㅗ  모양 추가
    if l == 1:
        f = []
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if not v[nx][ny]:
                    f.append(g[nx][ny])

        if len(f) >= 2:
            f.sort(reverse=True)
            val += f[0]
            val += f[1]
            val += g[x][y]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m:
            if not v[nx][ny]:
                v[nx][ny] = True
                val = max(val, g[x][y] + dfs(nx, ny, l+1))
                v[nx][ny] = False

    return val

# 최댓값 찾기
res = 0
for i in range(n):
    for j in range(m):
        v[i][j] = True
        res = max(dfs(i,j,0), res)
        v[i][j] = False

print(res)