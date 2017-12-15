from functools import reduce
#from fractions import gcd

def part_1():
    with open('day_13_data_1') as file:
        layers = {int(layer[0]): int(layer[1]) for layer in list(map(lambda line: line.replace(':', '').split(), file.readlines()))}
        return reduce(lambda acc, k: acc + layers[k] * k if k % ((layers[k] - 1) * 2) == 0 else acc, layers, 0)

print(part_1())

def part_2():
    with open('day_13_data_1') as file:
        layers = {int(layer[0]): int(layer[1]) for layer in list(map(lambda line: line.replace(':', '').split(), file.readlines()))}
        for i in range(0, 10000000, 2):
            caught = False
            for k, v in layers.items():
                if (k + i) % ((layers[k] - 1) * 2) == 0:
                    caught = True
                    break
            if not caught:
                return i


print(part_2())

