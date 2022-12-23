import math

N = int(input())
result = list(map(int, input().split()))

def findK(card):
    R = int(math.log2(N))

    for k1 in range(R+1):
        for k2 in range(R+1):
            expect = [x+1 for x in range(N)]
            expect = shuffle(expect, k1) 
            expect = shuffle(expect, k2)
            if expect == card:
                print(k1, k2)
                return

def shuffle(card, k):
    up = N - 2**k
    c = [item for item in card[up:]]
    for u in range(up):
        c.append(card[u])
    R = 2**k
    for i in range(1, k+1):
        temp = []
        start = R - 2**(k-i) 
        U = c[start:R]
        D = c[:start]
        S = c[R:]
        for u in U:
            temp.append(u)
        for d in D:
            temp.append(d)
        for s  in S:
            temp.append(s)
        c = [x for x in temp]
        R = start
    return c

findK(result)