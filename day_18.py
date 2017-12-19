from collections import defaultdict


class Register(object):

    def __init__(self, id, data, registers):
        self.id = id
        self.data = data
        self.op_index = 0
        self.registers = registers
        self.registers['p'] = self.id
        self.coupled_register = None
        self.send_count = 0
        self.sends = []
        self.done = False


    def inc(func):
        def wrapper(self, *args):
            self.op_index += 1
            func(self, *args)
        return wrapper

    # part 1
    def run(self):
        while 0 <= self.op_index < len(self.data):
            self.eval_command()

    def can_run(self):
        if self.done:
            return False
        else:
            try:
                rcv = self.data[self.op_index][0] == 'rcv'
                if rcv:
                    return len(self.coupled_register.sends) > 0
            except IndexError:
                return False
            return True

    def eval_command(self):
        if not self.can_run():
            return
        else:
            try:
                op = self.data[self.op_index]
            except IndexError:
                self.done = True
                print("Done")
                return
            getattr(self, op[0])(*op[1:])

    def eval_pointer(self, y):
        if str(y).isalpha():
            return self.registers[y]
        else:
            return int(y)

    @inc
    def snd(self, x):
        self.sends.append(self.eval_pointer(x))
        self.send_count += 1

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
        #if not self.eval_pointer(x) == 0:
        #if len(self.coupled_register.sends) > 0:
        self.registers[x] = self.coupled_register.sends.pop(0)

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
        return #registers.played_sounds[0]



def part_2():
    with open('day_18_data_1') as file:
        data = [line.split() for line in file.readlines()]
        p0 = Register(0, data, defaultdict(int))
        p1 = Register(1, data, defaultdict(int))
        p0.coupled_register = p1
        p1.coupled_register = p0

        while True:
            p0.eval_command()
            p1.eval_command()
            if not p0.can_run() and not p1.can_run():
                break
        return p1.send_count


print(part_2())