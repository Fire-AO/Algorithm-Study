NM = list(map(int, input().split()))
DNA = [list(input()) for _ in range(NM[0])]

#통계사용
def hamming(DNA):
    statistic = []

    for i in range(NM[1]):
        # A = 0 / C = 1 / G = 2 / T = 3
        d = [0 for _ in range(4)]
        for j in range(NM[0]):
            if DNA[j][i] == 'A':
                d[0] += 1
            elif DNA[j][i] == 'C':
                d[1] += 1
            elif DNA[j][i] == 'G':
                d[2] += 1
            elif DNA[j][i] == 'T':
                d[3] += 1
        statistic.append(d.index(max(d)))
    
    S = ''
    for index in range(NM[1]):
        if statistic[index] == 0:
            S += 'A'
        elif statistic[index] == 1:
            S += 'C'
        elif statistic[index] == 2:
            S += 'G'
        elif statistic[index] == 3:
            S += 'T'
    count = 0
    s = list(S)
    for t in range(NM[0]):
        for o in range(NM[1]):
            if DNA[t][o] != s[o]:
                count += 1
    
    print(S)
    print(count)

#brute force
def hamming2(origin, DNA, level):    
    if level == NM[1]:
        distance = 0
        for t in range(NM[0]):
            for o in range(NM[1]):
                if origin[t][o] != DNA[o]:
                    distance += 1
        return [distance, DNA]
    else:
        d = [x for x in DNA]
        d[level] = 'T'
        d1 = hamming2(origin, d, level+1)
        d[level] = 'G'
        d2 = hamming2(origin, d, level+1)
        d[level] = 'C'
        d3 = hamming2(origin, d, level+1)
        d[level] = 'A'
        d4 = hamming2(origin, d, level+1)
        result = [d1, d2, d3, d4]
        cost = [d1[0], d2[0], d3[0], d4[0]]
        index = cost.index(min(cost))
        return result[index]

hamming(DNA)
find = hamming2(DNA, ['A' for _ in range(NM[1])], 0)
stri = ''
for s in find[1]:
    stri += s
print(stri, '\n', find[0])