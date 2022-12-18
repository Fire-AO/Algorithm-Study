#단지 번호 붙이기

size = 7

sample = [
    [0, 1, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 1],
    [1, 1, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 1],
    [0, 1, 0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [0, 1, 1, 1, 0, 0, 0]
]

def mapAnalysis(map):
    count = 0
    count_max = count
    valid = list(map)
    result = []
    for i in range(size):
        result.append([0 for _ in range(size)])
    queue = []

    for v in range(size):
        for h in range(size):
            if valid[v][h] == 1:
                count += 1
                queue.append([v, h])
                vi = v
                hi = h                
                while valid[vi][hi] != 0:
                    while True:
                        if hi < size-1:
                            if valid[vi][hi+1] == 1:
                                queue.append([vi, hi + 1])
                            elif valid[vi][hi+1] == -1:
                                count = result[vi][hi+1]
                                break
                            elif valid[vi][hi+1] == 0:
                                hi = h
                                break
                            hi += 1
                        else:
                            break
                    if vi < size - 1:
                        if valid[vi+1][hi] == 1:
                            queue.append([vi + 1, hi])
                        elif valid[vi+1][hi] == -1:
                            count = result[vi+1][hi]
                            break
                        vi += 1
                    else:
                        break
                for item in queue:
                    result[item[0]][item[1]] = count
                    valid[item[0]][item[1]] = -1
                queue.clear()
                if count_max < count:
                    count_max = count
                else:
                    count = count_max

    number = [0 for _ in range(count_max+1)]
    for v in range(size):
        for h in range(size):
            number[result[v][h]] += 1
    number[0] = 0
    number.sort()

    print(count_max)
    for r in number[1:]:
        print(r)

mapAnalysis(sample)                 