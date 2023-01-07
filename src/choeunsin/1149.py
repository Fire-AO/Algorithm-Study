#RGB 거리
"""
문제.
houses는 일렬로 서있는 집들의 수이다.
이웃한 집들은 같은 색으로 칠할 수 없다고 할 때 paint 2차원 배열에는
집들의 순서대로 각각 빨강, 초록, 파랑으로 칠했을 때 필요한 비용이다.
주어진 집들을 모두 칠했을 때 최소 금액을 구하여라.
https://www.acmicpc.net/problem/1149

풀이 노션
https://www.notion.so/RGB-1149-37124f72fcb34adb90710cc89de2d646
"""

houses = int(input())
paint = [list(map(int, input().split())) for _ in range(houses)]

#첫번째 집은 누적될 값이 없기 때문에 두번째 집부터 반복문 시작
for i in range(1, houses) :
    #i번째 집이 빨간색으로 칠해지려면 i-1번째 집이 빨간색을 제외한 파랑 또는 초록이라는 뜻.
    #누적된 값을 구하기 위해 i-1번째 집의 파랑/초록 값들 중 작은 값을 구하고, i번째 집을 빨강으로 칠하는 값을 더한다.
    paint[i][0] = min(paint[i - 1][1], paint[i-1][2]) + paint[i][0]
    #i번째 집이 초록으로 칠해지려면 i-1번째 집이 초록색을 제외한 빨강 또는 파랑이라는 뜻.
    paint[i][1] = min(paint[i - 1][0], paint[i - 1][2]) + paint[i][1]
    #i번째 집이 파랑색으로 칠해지려면 i-1번째 집이 파랑색을 제외한 빨강 또는 초록이라는 뜻.
    paint[i][2] = min(paint[i - 1][0], paint[i - 1][1]) + paint[i][2]

#마지막 집이 빨강, 초록, 파랑으로 색칠되었을 때 최솟값들을 누적 저장해놓은 값들이다.
#이중에 최솟값 구해서 출력
print(min(paint[-1][0], paint[-1][1], paint[-1][2]))