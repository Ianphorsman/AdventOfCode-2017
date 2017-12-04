from functools import reduce

def part_1():
    with open('day_1_data_1') as file:
        data = file.read()
        data = data + data[0]
        return reduce(lambda x,y: x + int(data[y]) if data[y] == data[y+1] else x, range(len(data)-1), 0)

print(part_1())

def part_2():
    with open('day_1_data_2') as file:
        data = file.read()
        size = len(data)
        return reduce(lambda x,y: x + int(data[y]) if data[y] == data[(y+size//2)%size] else x, range(size), 0)

print(part_2())