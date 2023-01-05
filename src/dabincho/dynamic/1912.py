#연속합

#입력
N = int(input())
number = list(map(int, input().split()))

def continuous(numbers):
    '''
    연속된 수 들의 합을 계산
    앞 쪽에서부터 뒤로가며 차례로 숫자들을 더함
    1) 마이너스가 되면 가망이 없으므로 다시 덧셈을 시작
    2) 마이너스가 되지 않으면 아직 가능성이 있으므로 계속 더함
    -> 최종적으로 기억된 최댓값을 출력
    '''
    MAX = max(numbers)
    sum = [n for n in numbers]
    add = 0
    for i in range(N):
        sum[i] = add + sum[i]
        add = sum[i]
        if sum[i] + add < 0 and i < N-1:
            add = 0
        if sum[i] > MAX:
            MAX = sum[i]
    return MAX

print(continuous(number))
