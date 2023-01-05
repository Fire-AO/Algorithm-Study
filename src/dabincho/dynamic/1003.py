#피보나치 함수

#입력
number_case = int(input())
question = [int(input()) for _ in range(number_case)]

max = max(question)

zero = [0 for _ in range(max+1)]
one = [0 for _ in range(max+1)]

def fibonacci(N):
    '''
    <피보나치 수열>
    n = (n-1) + (n-2)

    -> 1의 출력 갯수
    one = (one-1) + (one-2)
    -> 0의 출력 갯수
    zero = (zero-1) + (zero-2)
    '''
    for i in range(N+1):
        if i == 0:
            zero[i] = 1
        elif i == 1:
            one[i] = 1
        else:
            zero[i] = zero[i-1] + zero[i-2]
            one[i] = one[i-1] + one[i-2]

def result():
    for i in question:
        print(zero[i], one[i])

fibonacci(max)
result()