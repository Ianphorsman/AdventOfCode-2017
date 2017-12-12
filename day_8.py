from collections import defaultdict


def part_1():
    with open('day_8_data_1') as file:
        data = list(map(lambda line: line.replace('dec', '-=').replace('inc', '+=').split(), file.readlines()))
        register = defaultdict(int)

        for action in data:
            action[0] = "register['{}']".format(action[0])
            action[4] = "register['{}']".format(action[4])
            statement = ' '.join(action[0:3])
            conditional = ' '.join(action[4:])
            condition_met = eval(conditional)
            if condition_met:
                exec(statement)

        return max(list(map(lambda tup: tup[1], register.items())))



def part_2():
    with open('day_8_data_1') as file:
        data = list(map(lambda line: line.replace('dec', '-=').replace('inc', '+=').split(), file.readlines()))
        register = defaultdict(int)
        ceil = 0

        for action in data:
            action[0] = "register['{}']".format(action[0])
            action[4] = "register['{}']".format(action[4])
            statement = ' '.join(action[0:3])
            conditional = ' '.join(action[4:])
            condition_met = eval(conditional)
            if condition_met:
                exec(statement)
                ceil = max(ceil, max(list(map(lambda tup: tup[1], register.items()))))
        return ceil


print(part_1())
print(part_2())