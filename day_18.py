from collections import defaultdict, deque


class Register(object):

    def __init__(self, data, registers):
        self.data = data
        self.op_index = 0
        self.registers = registers
        self.played_sounds = deque()


    def inc(func):
        def wrapper(self, *args):
            self.op_index += 1
            func(self, *args)
        return wrapper

    def run(self):
        while 0 <= self.op_index < len(self.data) - 1:
            self.eval_command()

    def eval_command(self):
        op = self.data[self.op_index]
        getattr(self, op[0])(*op[1:])

    def eval_pointer(self, y):
        if str(y).isalpha():
            return self.registers[y]
        else:
            return int(y)

    @inc
    def snd(self, x):
        self.played_sounds.append(self.registers[x])

    @inc
    def set(self, x, y):
        self.registers[x] = self.eval_pointer(y)

    @inc
    def add(self, x, y):
        self.registers[x] += self.eval_pointer(y)

    @inc
    def mul(self, x, y):
        self.registers[x] *= self.eval_pointer(y)

    @inc
    def mod(self, x, y):
        self.registers[x] %= self.eval_pointer(y)

    @inc
    def rcv(self, x):
        #print(self.eval_pointer(x))
        if not self.eval_pointer(x) == 0:
            self.played_sounds.rotate()

    def jgz(self, x, y):
        if not self.eval_pointer(x) == 0:
            self.op_index += self.eval_pointer(y)
        else:
            self.op_index += 1



def part_1():
    with open('day_18_data_1') as file:
        data = [line.split() for line in file.readlines()]
        registers = Register(data, defaultdict(int))
        registers.run()
        return registers.played_sounds[0]



def part_2():
    with open('day_18_data_1') as file:
        data = [line.split() for line in file.readlines()]

        return data


print(part_1())