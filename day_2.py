from functools import reduce
from itertools import combinations

def part_1():
    with open('day_2_data_1') as file:
        data = file.readlines()
        data = [x.replace('\n', '').split('\t') for x in data]
        min_max = [reduce(lambda x,y: (min(x[0], int(y)), max(x[1], int(y))), line, (int(line[0]), int(line[0]))) for line in data]
        sum_of_differences = reduce(lambda total, x: total + abs(x[0]-x[1]), min_max, 0)
        return sum_of_differences

print(part_1())

def part_2():
    with open('day_2_data_1') as file:
        data = file.readlines()
        data = [x.replace('\n', '').split('\t') for x in data]
        data = [list(filter(lambda tup: int(tup[0]) % int(tup[1]) == 0 or int(tup[1]) % int(tup[0]) == 0, combinations(line, 2))) for line in data]
        total = 0
        for arr in data:
            if not arr == []:
                arr = list(map(int, arr[0]))
                total += max(arr) // min(arr)
        return total

print(part_2())