# BOJ 15686 치킨배달 골드5
#https://www.acmicpc.net/problem/15686
'''
유용한 라이브러리 itertools
permutaions, combinations
순열, 조합을 쉽게 구할 수 있다.
'''
from itertools import combinations
# d입력
n, m = map(int, input().split())

h = []
s = []
# 집과 가게를 구분해서 리스트에 따로 저장한다.
for i in range(n):
    l = list(map(int, input().split()))
    for j in range(n):
        if l[j] == 1:
            h.append((i, j))
        if l[j] == 2:
            s.append((i, j))

# 조합으로 폐업하지 않을 가게만 선정한다. 이후에는 거리계산
min_sum = []
for stores in combinations(s, m):
    sol = 0
    for house in h:
        mi = 200
        for store in stores:
            sx, sy = store
            hx, hy = house
            mi = min(mi, abs(sx-hx)+abs(sy-hy))
        sol += mi
    min_sum.append(sol)
print(min(min_sum))