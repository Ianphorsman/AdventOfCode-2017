from functools import reduce
def part_1():
    with open('day_5_data_1') as file:
        data = [int(num.replace('\n', '')) for num in file.readlines()]
        index = 0
        step = 0

        while 0 <= index < len(data):
            val = data[index]
            data[index] += 1
            index += val
            step += 1
        return step

print(part_1())

def part_2():
    with open('day_5_data_1') as file:
        data = [int(num.replace('\n', '')) for num in file.readlines()]
        index = 0
        step = 0

        while 0 <= index < len(data):
            val = data[index]
            if val >= 3:
                data[index] -= 1
            else:
                data[index] += 1
            index += val
            step += 1
        return step

print(part_2())