#동전(경우의 수)

#입력
'''
Q : 제공되는 동전의 수, 목표 금액
coin : 제공되는 동전의 가치 리스트
    - 목표로 하는 금액을 초과하는 경우는 필요하지 않으므로 제거
    - 오름차순으로 정렬
    - 마지막은 목표 가격
'''
Q = list(map(int, input().split()))
sample = [int(input()) for _ in range(Q[0])]
coin = [i for i in sample if i <= Q[1]]
coin.sort()

#경우의 수를 계산하는 함수
def coin_count(value, coins):
    '''
    count[j] : j원을 만드는 경우의 수
    * j == i인 경우가 존재하기 떄문에 count[0] = 1로 설정

    --------------------------------------------------------------------
    |     |  1  |  2  |  3  |  4  |  5  |  6  |  7  |  8  |  9  |  10  |
    |  1  |  1  |  1  |  1  |  1  |  1  |  1  |  1  |  1  |  1  |   1  |
    |  2  |  0  |  1  |  1  |  2  |  2  |  3  |  3  |  4  |  4  |   5  |
    |  5  |  0  |  0  |  0  |  0  |  1  |  1  |  2  |  2  |  3  |   4  |
    | 최종|  1  |  2  |  2  |  3  |  4  |  5  |  5  |  7  |  8  |  10  |
    --------------------------------------------------------------------
    : 1원부터 10원까지 1, 2, 5로 만들 수 있는 경우의 수
    : 가로(j)/ 세로(i)
    : count[j] = count[j - i]

    *반복문
    1) 주어진 각각의 i원에 대해
    2) coin[i-1]을 적어도 하나 이상 사용했을 경우의 수 + coin[i]를 적어도 하나 이상 사용했을 경우의 수 = 현재 count[j]
        -> 이전 count[j]                                  -> count[j - coin[i]]

    '''
    count = [0 for _ in range(value+1)]
    count[0] = 1

    for i in range(len(coins)):
        for j in range(coins[i], value+1):
            count[j] += count[j-coins[i]]
    
    print(count[len(count)-1])

coin_count(Q[1], coin)