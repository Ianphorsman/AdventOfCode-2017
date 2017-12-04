import math
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