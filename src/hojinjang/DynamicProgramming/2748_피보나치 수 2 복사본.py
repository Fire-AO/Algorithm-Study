# 출력을 위한 라이브러리 print() 함수보다 더 빠른 속도를 가지고 있음.
import sys

# input() 함수를 통해 수를 입력받고 int로 형변환 후 저장
N = int(input())

# fibo라는 리스트를 만들어 모두 0으로 초기화하고 1번째 요소를 1로 저장
fibo = [0 for _ in range(N + 1)]
fibo[1] = 1

# N까지 fibo의 값을 변경
for i in range(2, N + 1):
    fibo[i] = fibo[i - 1] + fibo[i - 2]

# fibo의 N을 출력
sys.stdout.write(str(fibo[N]))
