import sys
S = list(input())
T = list(input())

def dfs(t) :
    if t == S:      #S와 T가 같아짐
        print(1)
        sys.exit()  #전체 종료
    if len(t) == 0 :#더이상 제거할 T의 요소가 없음
        return 0
    if t[-1] == 'A' :   #t의 마지막 요소가 A일 때
        dfs(t[:-1])     #A 제거 후 재귀
    if t[0] == 'B' :    #t의 첫번째 요소가 B일 때
        t.pop(0)
        t.reverse()
        dfs(t)          #B 제거 후, 뒤집어서 재귀

dfs(T)
print(0)