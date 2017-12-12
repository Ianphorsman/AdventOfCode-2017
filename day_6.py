
def part_1():
    with open('day_6_data_1') as file:
        data = tuple(map(int, file.read().split()))
        s = set()
        step = 0
        while data not in s:
            s.add(data)
            step += 1
            data = distribute_blocks(data)
        return step

def part_2():
    with open('day_6_data_1') as file:
        data = tuple(map(int, file.read().split()))
        s = set()
        step = 0
        while data not in s:
            s.add(data)
            step += 1
            data = distribute_blocks(data)
        loop_set = data
        step = 1
        data = distribute_blocks(data)
        while data != loop_set:
            step += 1
            data = distribute_blocks(data)
    return step



def distribute_blocks(data):
    max_block = 0
    size = len(data)
    for i in range(size):
        if data[i] > data[max_block]:
            max_block = i
    mut_data = list(data)
    x = data[max_block]
    mut_data[max_block] = 0
    for i in range(x):
        mut_data[(max_block + i + 1) % size] += 1

    return tuple(mut_data)

print(part_1())
print(part_2())

