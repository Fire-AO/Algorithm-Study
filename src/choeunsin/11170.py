#0의 개수

#테스트 케이스의 수
T = int(input())
for i in range(T) :
    count = 0   #0의 개수 저장할 변수
    a, b = map(int, input().split())    #범위 a 이상 b 이하
    for i in range(a, b+1) :
        now = str(i)
        count += now.count('0')         #0 세기
    print(count)