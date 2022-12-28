#퇴사
#남은 날짜 N
days = int(input())

consult_dict = {}
#상담 기간 T, 상담 금액 P
for i in range(days) :
    T, P = map(int, input().split())
    #리스트 0번째 금액, 1번째 상담 기간, 2번째 상담 금액
    consult_dict[i+1] = [-1, T, P]

#days += 1
result = []
def search(now, profit = 0) :
    consult_dict[now][0] = profit

    if now+consult_dict[now][1] > days+1:
        result.append(profit)
        return '퇴사'
    elif now + consult_dict[now][1] == days+1:
        profit += consult_dict[now][2]
        result.append(profit)
        return '마지막 날까지 일하고 퇴사'
    else:
        profit += consult_dict[now][2]
        search(now+consult_dict[now][1], profit)

for i in range(1, days) :
    search(i)
print(max(result))