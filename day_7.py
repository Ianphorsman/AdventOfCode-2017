from collections import defaultdict


def part_1():
    with open('day_7_data_1') as file:
        data = list(map(lambda line: line.strip().split(), file.readlines()))
        nodes = set()
        words = []
        for line in data:
            if '->' in line:
                words.append(line[0])
                index = line.index('->')
                children = [child.strip(',') for child in line[index + 1:]]
                for child in children:
                    nodes.add(child)

        for word in words:
            if word not in nodes:
                return word


def part_2():
    with open('day_7_data_1') as file:
        data = list(map(lambda line: line.strip().split(), file.readlines()))
        nodes = set()
        words = []
        weights = {}
        children = defaultdict(list)

        for line in data:
            words.append(line[0])
            weights[line[0]] = int(line[1].strip('()'))
            if '->' in line:
                index = line.index('->')
                children[words[-1]] = [child.strip(',') for child in line[index + 1:]]
                nodes |= set(children[words[-1]])
        root = ''
        for word in words:
            if word not in nodes:
                root = word

        return weigh_tree(children, weights, root, data)


def weigh_tree(children, weights, root, data):
    expected_weight = None
    total = weights[root]
    for child in children[root]:
        weight = weigh_tree(children, weights, child, data)
        total += weight
        if expected_weight is None:
            expected_weight = weight
        elif expected_weight != weight:
            # the answer to part 2 is the first printed node imbalance
            print(get_node_imbalance(child, weight - expected_weight, data))

    return total


def get_node_imbalance(child, imbalance, data):
    return int(list(filter(lambda line: line[0] == child, data))[0][1].strip('()')) - imbalance

print(part_1())
print(part_2())