from functools import reduce

def part_1():
    with open('day_11_data_1') as file:
        path = file.read().split(',')

        x_move = [-1, -1, 0, 0, 1, 1]
        y_move = [-1, 0, -1, 1, 0, 1]
        directions = ['n', 'ne', 'nw', 'se', 'sw', 's']

        offset = reduce(lambda acc, i: (acc[0] + x_move[i], acc[1] + y_move[i]), [directions.index(p) for p in path], (0, 0))

        return offset

print(part_1())

def part_2():
    with open('day_11_data_1') as file:
        path = file.read().split(',')

        x_move = [-1, -1, 0, 0, 1, 1]
        y_move = [-1, 0, -1, 1, 0, 1]
        directions = ['n', 'ne', 'nw', 'se', 'sw', 's']

        max_distance = 0
        distance = lambda tup: max(max(abs(tup[0]), abs(tup[1])), max_distance)
        total_offset = (0, 0)
        for i in [directions.index(p) for p in path]:
            total_offset = (total_offset[0] + x_move[i], total_offset[1] + y_move[i])
            print(total_offset)
            max_distance = distance(total_offset)



        return max_distance

print(part_2())