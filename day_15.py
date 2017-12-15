from functools import reduce


def part_1():
    a = 679
    b = 771

    factor_a = 16807
    factor_b = 48271
    remainder = 2147483647
    matches = 0

    for _ in range(40000000):
        if (a & 0xffff) == (b & 0xffff):
            matches += 1
        a = (a * factor_a) % remainder
        b = (b * factor_b) % remainder

    return matches


print(part_1())


def part_2():
    a = 679
    b = 771

    factor_a = 16807
    factor_b = 48271
    remainder = 2147483647

    ga = []
    gb = []


    while True:
        a = (a * factor_a) % remainder
        b = (b * factor_b) % remainder
        if a & 3 == 0:
            ga.append(a)
        if b & 7 == 0:
            gb.append(b)
        if min(len(ga), len(gb)) > 5000000:
            break
    return len(list(filter(lambda tup: (tup[0] & 0xffff) == (tup[1] & 0xffff), list(zip(ga, gb))[:5000000])))

print(part_2())