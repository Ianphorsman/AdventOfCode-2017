from functools import reduce

def part_1():
    with open('day_9_data_1') as file:
        stream = file.read()
        score = 0
        acc = 0
        ignore = False
        garbage = False

        for char in stream:
            if ignore:
                ignore = False
                continue
            if char == '!':
                ignore = True
                continue
            if garbage and char == '>':
                garbage = False
                continue
            elif garbage:
                continue
            if char == '<':
                garbage = True
                continue
            if char == '{':
                acc += 1
                score += acc
                continue
            elif char == '}':
                acc -= 1
                continue

        return score






def part_2():
    with open('day_9_data_1') as file:
        stream = file.read()
        score = 0
        acc = 0
        ignore = False
        garbage = False
        character_count = 0
        for char in stream:
            if ignore:
                ignore = False
                continue
            if char == '!':
                ignore = True
                continue
            if garbage and char == '>':
                garbage = False
                continue
            elif garbage:
                character_count += 1
                continue
            if char == '<':
                garbage = True
                continue
            if char == '{':
                acc += 1
                score += acc
                continue
            elif char == '}':
                acc -= 1
                continue

        return character_count


print(part_1())
print(part_2())