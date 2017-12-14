from collections import defaultdict


def part_1():
    with open('day_12_data_1') as file:
        data = list(map(lambda line: line.strip().split(), file.readlines()))
        pipeline = defaultdict(list)

        for line in data:
            left = int(line[0])
            right = map(lambda x: int(x.strip(',')), line[2:])
            for num in right:
                pipeline[left].append(num)
                pipeline[num].append(left)

        q = [0]
        vis = set()
        while q:
            a = q.pop()
            for b in pipeline[a]:
                if b not in vis:
                    vis.add(b)
                    q.append(b)
        return len(vis)


def part_2():
    with open('day_12_data_1') as file:
        data = list(map(lambda line: line.strip().split(), file.readlines()))
        pipeline = defaultdict(list)

        for line in data:
            left = int(line[0])
            right = map(lambda x: int(x.strip(',')), line[2:])
            for num in right:
                pipeline[left].append(num)
                pipeline[num].append(left)

        print(pipeline)
        vis = set()
        groups = 0
        for i in range(len(data)):
            if i in vis:
                continue
            groups += 1
            q = [i]
            while q:
                a = q.pop()
                for b in pipeline[a]:
                    if b not in vis:
                        vis.add(b)
                        q.append(b)
        return groups





print(part_1())
print(part_2())