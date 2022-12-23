# BOJ 2667 단지번호붙이기 실버1
#https://www.acmicpc.net/problem/2667

'''
트리 완전탐색 문제이기 때문에 dfs, bfs 둘다 가능하다.
파이썬 pypy3의 경우 재귀가 취약하기 때문에 완전탐색은 되도록 bfs로 풀어야겠다 생각을 했다.
bfs의 경우 시작 노드의 방문처리도 꼭 해야한다.
'''

from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

#입력 n
n = int(input())
#입력 g (2차원 배열)
g = [list(map(int, input())) for _ in range(n)]

#방문 확인
v = [[False]*n for _ in range(n)]

def bfs(g, start, v):
    q = deque()
    q.append(start)
    # 첫 방문으로 변경
    v[start[0]][start[1]] = True
    count = 0

    while q:
        x, y = q.popleft()
        # 단지수를 세기위한 코드
        count += 1

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 조건:  nx, ny 가 2차원 배열안에 있고, 트리 이면서(1을 가져야 트리 0일 경우 공백), 방문하지 않아야한다.
            if 0 <= nx < n and 0 <= ny < n and g[nx][ny] == 1 and not v[nx][ny]:
                    # 방문할 트리이기 때문에 큐에 추가
                    q.append((nx, ny))
                    # 방문으로 변경
                    v[nx][ny] = True

    #단지수 반환
    return count

countList = []
for i in range(n):
    for j in range(n):
        if g[i][j] == 1 and not v[i][j]:
            countList.append(bfs(g,(i,j), v))

#출력
countList.sort()
print(len(countList))
for count in countList:
    print(count)
