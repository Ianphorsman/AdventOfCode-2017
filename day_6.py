
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

'''
def part_1():
    with open('day_6_data_1') as file:
        data = list(map(int, file.read().split()))
        data = list(map(list, zip(range(len(data)), data)))
        distributions = [data]
        for count in range(50):
            sorted_data = distributions[-1]
            #print(len(distributions))
            sorted_data.sort(key=lambda tup: tup[1])
            span = min(len(sorted_data), sorted_data[-1][1])
            for i in range(len(sorted_data)):
                if i < span:
                    sorted_data[i][1] += 1
            sorted_data[-1][1] -= span
            unzipped_data = sorted_data
            unzipped_data.sort(key=lambda tup: tup[0])
            print(count, unzipped_data)
            distributions.append(unzipped_data[:])

        return distributions

for l in part_1():
    print([tup[1] for tup in l])

def part_2():
    with open('day_6_data_1') as file:
        data = file.read()
        return data
'''