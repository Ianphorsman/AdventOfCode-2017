from functools import reduce

def part_1():
    with open('day_10_data_1') as file:
        data = list(map(int, file.read().split(',')))
        a = list(range(256))
        p = 0
        s = 0

        for y in data:
            b = a[p:] + a[:p]
            b = list(reversed(b[:y])) + b[y:]
            a = b[-p:] + b[:-p]
            p = p + y + s
            p %= len(a)
            s += 1

        return a[0:2]

def part_2():
    with open('day_10_data_1') as file:
        data = [ord(char) for char in file.read().strip()]
        a = list(range(256))
        tail = [17,31,73,47,23]
        data += tail
        p = 0
        s = 0
        for _ in range(64):
            for y in data:
                b = a[p:] + a[:p]
                b = list(reversed(b[:y])) + b[y:]
                a = b[-p:] + b[:-p]
                p = p + y + s
                p %= len(a)
                s += 1

        out = ''
        for i in range(0, 256, 16):
            block = a[i:i + 16]
            val = reduce(lambda acc, x: acc ^ x, block)
            val = hex(val)[2:]
            if len(val) == 1:
                val = '0' + val
            out += val
        return ''.join(out)

print(part_1())
print(part_2())

