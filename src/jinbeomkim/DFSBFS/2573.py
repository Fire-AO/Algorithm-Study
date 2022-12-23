# BOJ 1260 DFS와 BFS 실버2
#https://www.acmicpc.net/problem/1260
'''
print end파라미터 사용시 끝 부분을 지정할 수 있음
'''
from collections import deque

# v- 정점의 개수 e- 간선의 개수 f-시작
v, e, f = map(int, input().split())

#g - 그래프 입력
g = [[] for _ in range(v + 1)]

for _ in range(e):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

#정렬
for i in range(len(g)):
    g[i].sort()

#방문 체커
d = [False] * (v + 1)

def dfs(g, v, d):
    d[v] = True
    print(str(v), end=" ")
    for i in g[v]:
        if not d[i]:
            dfs(g, i, d)

def bfs(g, v, d):
    q = deque()
    q.append(v)
    print(str(v), end=" ")
    d[v] = True

    while q:
        x = q.popleft()
        for i in g[x]:
            if not d[i]:
                d[i] = True
                q.append(i)
                print(str(i), end=" ")

dfs(g, f, d)

#초기화
d = [False] * (v + 1)
print()

bfs(g, f, d)