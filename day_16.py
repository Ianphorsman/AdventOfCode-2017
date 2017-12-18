from functools import reduce

def spin(l, pivot):
    return l[-pivot:] + l[:-pivot]

def exchange(l, a, b):
    l[a], l[b] = l[b], l[a]
    return l

def partner(l, a, b):
    index_a, index_b = l.index(a), l.index(b)
    l[index_a], l[index_b] = l[index_b], l[index_a]
    return l

def perform_dance_move(l, move):
    action = move[0]
    if action == 's':
        return spin(l, int(move[1:]))
    elif action == 'x':
        a, b = move[1:].split('/')
        return exchange(l, int(a), int(b))
    elif action == 'p':
        a, b = move[1:].split('/')
        return partner(l, a, b)

def part_1():
    with open('day_16_data_1') as file:
        dance = file.read().strip().split(',')
        programs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p']
        for move in dance:
            programs = perform_dance_move(programs, move)
        return ''.join(programs)

print(part_1())


def part_2():
    with open('day_16_data_1') as file:
        data = file.read().split(',')
        return data