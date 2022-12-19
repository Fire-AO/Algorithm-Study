#토마토

sample1 = [
    [0, -1, 0, 0, 0],
    [-1, -1, 0, -1, -1],
    [0, 0, 0, -1, -1]
]

sample2 = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

sample3 = [
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [-1, -1, -1, -1],
    [1, 1, 1, -1]
]

def tomato(box, size, number):
    boxes = []
    valid_layer = [0 for _ in range(number)]
    check = []
    for i in range(size[1]*number):
        check.append([0 for _ in range(size[0])])
    day = 0

    for n in range(number):
        boxes.append([item for item in box[n*size[1]:size[1]+n*size[1]]])

    while True:
        full = 1
        for layer in range(number):
            for v in range(size[1]):
                v *= (layer+1)
                for h in range(size[0]):
                    if box[v][h] == 0:
                        full = 0
                    elif box[v][h] == -1:
                        check[v][h] = 1
                    elif box[v][h] == 1 and check[v][h] == 0:
                        check[v][h] = 1
                        if layer < number-1 and box[v+size[1]][h] != -1:
                            box[v+size[1]][h] = 1
                        if layer > 0 and box[v-size[1]][h] != -1:
                             box[v-size[1]][h] = 1
                        if v > 0 and box[v-1][h] != -1:
                            box[v-1][h] = 1
                        if v < size[1]-1 and box[v+1][h] != -1:
                            box[v+1][h] = 1
                        if h > 0 and box[v][h-1] != -1:
                            box[v][h-1] = 1
                        if h < size[0]-1 and box[v][h+1] != -1:
                            box[v][h+1] = 1
            valid_layer[layer] = full
        potential = 0
        for v1 in range(size[1]*number):
            for h1 in range(size[0]):
                if check[v1][h1] == 0:
                    if box[v1][h1] == 1:
                        potential = 1
                        break
        if potential != 1:
            valid_layer[0] = -1

        if -1 in valid_layer:
            day = -1
            break
        elif 0 not in valid_layer:
            if day != 0:
                day += 1
            break
        day += 1
    print(day)

tomato(sample1, [5, 3], 1)
tomato(sample2, [5, 3], 2)
tomato(sample3, [4, 3], 2)