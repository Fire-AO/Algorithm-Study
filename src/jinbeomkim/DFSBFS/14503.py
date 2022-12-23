# BOJ 14503 로봇 청소기 골드5
# https://www.acmicpc.net/problem/14503

from collections import deque

'''
시뮬레이션 문제의 경우 단계별로 천천히 구현해야 한다.
x,y 좌표가 혼동돼서 오류가 많이 생겼음.
'''

# 입력
# n: 세로 크기 m: 가로 크기
n, m = map(int, input().split())
# 로봇으 좌표 (r,c) 바라보는 방향 d(0:북, 1:동, 2:남, 3:서)
r, c, d = map(int, input().split())
# 장소 상태 g
g = [list(map(int, input().split())) for _ in range(n)]

# 방향 북 동 남 서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

count = 0

def dfs(x,y,d):
    global count

    #현재 위치 청소
    if g[x][y] == 0:
        count += 1
        g[x][y] = 2

    # 왼쪽 탐색
    for _ in range(4):
        nd = (d - 1) % 4
        nx = x + dx[nd]
        ny = y + dy[nd]
        if g[nx][ny] == 0:
            dfs(nx, ny, nd)
            return True
        d = nd

    #탐색 불가 뒤로가기
    xx = x - dx[d]
    yy = y - dy[d]
    if g[xx][yy] != 1:
        dfs(xx, yy, d)
        return True

    return False

dfs(r, c, d)
print(count)