#바이러스

computer_s = 7
pair_s = 6

sample = [
    [1, 2],
    [2, 3],
    [1, 5],
    [5, 2],
    [5, 6],
    [4, 7]
]

def virus(network, computer):
    valid = [False for _ in range(computer)]
    network.sort(key = lambda x:x[0])

    valid[0] = True
    for i in network:
        if valid[i[0]-1] == True:
            valid[i[1]-1] = True
    count = 0
    for item in valid:
        if item == True:
            count += 1
    
    print(count)

virus(sample, computer_s)