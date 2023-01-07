#피보나치 함수
N = int(input()) #N번 테스트
for i in range(N):
    count0 = [1,0] #index번째에 누적된 0의 출력 수 저장 리스트
    count1 = [0,1] #index번째에 누적된 1의 출력 수 저장 리스트
    n = int(input())
    if n > 1 :     #0,1번째는 이미 저장되어 있음, 2부터 시작
        for _ in range(n-1) :
            count0.append(count0[-1] + count0[-2])  #n번째에 n-1, n-2번째에 출력되었던 0 출력 수 더해서 저장
            count1.append(count1[-1] + count1[-2])  #n번째에 n-1, n-2번째에 출력되었던 1 출력 수 더해서 저장
    print(count0[n], count1[n]) #0,1이 n일 수 있기 때문에 리스트의 마지막(count[-1])이 아닌, n으로 출력