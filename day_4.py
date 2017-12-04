
def part_1():
    with open('day_4_data_1') as file:
        data = file.readlines()
        data = [line.replace('\n', '').split(' ') for line in data]
        return len(list(filter(lambda x: len(x) == len(set(x)), data)))

print(part_1())


def part_2():
    with open('day_4_data_1') as file:
        data = file.readlines()
        data = [line.replace('\n', '').split(' ') for line in data]
        return len(list(filter(lambda x: len(x) == len(set([''.join(sorted(phrase)) for phrase in x])), data)))

print(part_2())