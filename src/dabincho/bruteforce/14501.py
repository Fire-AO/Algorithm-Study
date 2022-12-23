N = int(input())
task = [list(map(int, input().split())) for _ in range(N)]
valid = [False for _ in range(N)]

def resignation(task, valid, level):
    pay = 0
    v = [item for item in valid]
    for i in range(N):
       if v[i] == True:
            pay += task[i][1]
    if level > N:
        return 0
    elif level == N:
        return pay
    else:
        max1 = resignation(task, v, level+1)
        v[level] = True
        max2 = resignation(task, v, level + task[level][0])
        if max2 == 0:
            max2 = pay
        if max1 > max2:
            return max1
        else:
            return max2


result = resignation(task, valid, 0)
print(result)