import math
from itertools import count
def part_1():
    with open('day_3_data_1') as file:
        n = int(file.read())
        side = math.ceil(math.sqrt(n))
        side = side if side % 2 != 0 else side + 1
        x_comp = (side - 1) / 2
        axis_intercepts = [side ** 2 - ((side - 1) * i) - math.floor(side / 2) for i in range(0, 4)]
        y_comp = min([abs(ai - n) for ai in axis_intercepts])
        return x_comp + y_comp

print(part_1())

def part_2():
    with open('day_3_data_1') as file:
        n = int(file.read())
        for x in spiral_generator():
            if x > n:
                return x


def spiral_generator():
    # mapping of spiral locations defined as offset (x_comp, y_comp) coord from center of spiral with its value
    pos_val = {(0, 0): 1}
    b, c = 0, 0

    get_spiral_value = lambda x, y: sum(pos_val.get((i, j), 0) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2))

    for s in count(1, 2):
        for dir_1, dir_2, dir_3 in zip([0, 0, 1, 1], [1, 0, -1, 0], [0, -1, 0, 1]):
            for _ in range(s + dir_1):
                b += dir_2
                c += dir_3
                pos_val[b, c] = get_spiral_value(b, c)

                yield pos_val[b, c]

print(part_2())

