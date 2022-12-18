#DFS와 BFS
from sys import stdin
read = stdin.readline
#첫번째 문자열에서 각각 정점의 개수, 간선의 개수, 탐색 시작 정점 저장
N, M, V = map(int, read().split())

#그래프를 위해 정점의개수+1만큼의 행,열을 만들기(2차원 배열)
#index가 0부터 시작하기 때문에 N+1로 제작. index==0인 부분은 사용X
graph = [[0]*(N+1) for i in range(N+1)]
#방문했던 배열 정점의 개수+1개 만들기(1차원 배열)
visited = [False]*(N+1)

#간선 저장
for i in range(M):
    x, y = map(int, read().split())
    #양방향이기 때문 x->y, y->x
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(V):
    #V 반복 방지
    visited[V] = True
    print(V, end=" ")
    for i in range(1, N+1):
        #i 정점이 False이면서, graph[V][i]==1, 즉 방문한 적 없는 간선이 존재할 때
        if not visited[i] and graph[V][i] == 1:
            #재귀함수 호출
            dfs(i)

def bfs(V):
    #앞서 호출한 dfs에서 방문했던 함수를 True로 바꾸어놓음
    #V 반복 방지로 방문한 정점은 다시 False로 선언
    visited[V] = False
    queue = [V]
    #큐에 하나라도 존재할 때 반복문 실행
    while queue:
        #선입선출. 가장 먼저 들어온 큐를 pop하고 출력
        V = queue.pop(0)
        print(V, end=" ")
        #정점의 개수만큼 반복
        for i in range(1, N+1):
            #i 정점이 True이면서, graph[V][i]==1, 즉 방문한 적 없는 간선이 존재할 때
            if visited[i] and graph[V][i] == 1:
                queue.append(i)
                visited[i] = False

dfs(V)
print()     #줄 바꿈 출력
bfs(V)