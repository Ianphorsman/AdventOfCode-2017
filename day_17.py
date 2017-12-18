from collections import deque


def part_1():
    with open('day_17_data_1') as file:
        buffer_size = int(file.read().strip())
        buffer = [0]
        current_index = 0
        for i in range(1, 2017 + 1):
            index = (current_index + buffer_size) % len(buffer)
            current_index = index + 1
            buffer = buffer[:index] + [i] + buffer[index:]
        return buffer[buffer.index(2017) + 1]


def part_2():
    with open('day_17_data_1') as file:
        buffer_size = int(file.read().strip())
        buffer = deque([0])

        for i in range(1, 50000000 + 1):
            buffer.rotate(-buffer_size)
            buffer.append(i)
            if i % 100000 == 0:
                print(i)
        val = None
        while val != 0:
            val = buffer.popleft()
        return buffer.popleft()


print(part_1())

print(part_2())