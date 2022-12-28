# BOJ 14501 퇴사 실버3
#https://www.acmicpc.net/problem/14501
'''
브루트포스로 재귀를 사용하면 해결가능, 여기서 DP를 사용해서 최적화 할 수 있다.
'''
# 입력
n = int(input())

c = [list(map(int, input().split())) for _ in range(n)]

# 재귀로 완전탐색 진행
def consult(day, p):

    # 정상 완료
    if day == n:
        return p

    # 비정상 완료
    if day > n:
        return 0

    # 재귀로, 상담O or 상담X 진행 , 최종적으로 제일 큰값을 가져가면 최대값을 가져갈 수 있다.
    return max(consult(day + 1, p), consult(day + c[day][0], p + c[day][1]))


print(consult(0, 0))