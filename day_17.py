
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
    with open('day-17_data_1') as file:
        num = int(file.read().strip())

        return num


print(part_1())