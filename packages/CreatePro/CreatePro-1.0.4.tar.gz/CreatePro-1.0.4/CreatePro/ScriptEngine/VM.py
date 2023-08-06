"""
Virtual Machine
"""
import sys

from collections import deque

from . import BaseMachine


class Stack(deque):
    push = deque.append

    def top(self):
        return self[-1]


class Preprocessor:
    def __init__(self, code):
        self.stack = []
        self.out = []
        wait = []
        end = []
        for i in code:
            if len(wait) != 0:
                self.out += self.stack
                self.out.append(i)
                self.out += wait
                wait.pop()
                self.stack = []
            elif (i in BaseMachine.keyword_set) and (i in BaseMachine.start_end_set):
                end.append(i)
            elif (i in BaseMachine.keyword_set) and (i in BaseMachine.wait_set):
                wait.append(i)
            elif (i in BaseMachine.keyword_set) and (i not in BaseMachine.wait_set):
                self.out.append(i)
            else:
                self.stack.append(i)
        self.out += self.stack + end
        
        
class VirtualMachine(BaseMachine):
    def __init__(self, code):
        super(VirtualMachine, self).__init__()
        self.data_stack = Stack()
        self.return_stack = Stack()
        self.instruction_pointer = 0
        self.code = code
        self.base = self.__dict__
        self.output = None

    def pop(self):
        return self.data_stack.pop()

    def push(self, value):
        self.data_stack.push(value)

    def top(self):
        return self.data_stack.top()

    def run(self):
        while self.instruction_pointer < len(self.code):
            opcode = self.code[self.instruction_pointer]
            self.instruction_pointer += 1
            self.dispatch(opcode)

    def dispatch(self, op):
        if op in self.dispatch_map:
            self.dispatch_map[op]()
        elif isinstance(op, int):
            self.push(op)  # push numbers on stack
        elif isinstance(op, str):
            self.push(op)  # push quoted strings on stack
        else:
            raise RuntimeError("Unknown opcode: '%s'" % op)

    # OPERATIONS FOLLOW:

    def plus(self):
        self.push(self.pop() + self.pop())

    @staticmethod
    def exit():
        """退出"""
        sys.exit(0)

    def minus(self):
        """-"""
        last = self.pop()
        self.push(self.pop() - last)

    def mul(self):
        """*"""
        self.push(self.pop() * self.pop())

    def div(self):
        """/"""
        last = self.pop()
        self.push(self.pop() / last)

    def mod(self):
        last = self.pop()
        self.push(self.pop() % last)

    def dup(self):
        """重复"""
        self.push(self.top())

    def over(self):
        b = self.pop()
        a = self.pop()
        self.push(a)
        self.push(b)
        self.push(a)

    def drop(self):
        """拖放"""
        self.pop()

    def swap(self):
        """交换"""
        b = self.pop()
        a = self.pop()
        self.push(b)
        self.push(a)

    def print(self):
        """print"""
        sys.stdout.write(str(self.pop()))
        sys.stdout.flush()

    def print_in(self):
        sys.stdout.write("%s\n" % self.pop())
        sys.stdout.flush()

    def read(self):
        self.push(input())

    def cast_int(self):
        """强制转换int"""
        self.push(int(self.pop()))

    def cast_str(self):
        """强制转换str"""
        self.push(str(self.pop()))

    def eq(self):
        """=="""
        self.push(self.pop() == self.pop())

    def if_stmt(self):
        false_clause = self.pop()
        true_clause = self.pop()
        test = self.pop()
        self.push(true_clause if test else false_clause)

    def jmp(self):
        """地址跳转"""
        address = self.pop()
        if isinstance(address, int) and 0 <= address < len(self.code):
            self.instruction_pointer = address
        else:
            raise RuntimeError("JMP address must be a valid integer.")

    def dump_stack(self):
        print("Data stack (top first):")

        for v in reversed(self.data_stack):
            print(" - type %s, value '%s'" % (type(v), v))

    def assignment(self):
        """赋值"""
        self.push(Stack(self.pop()))

    # Keys

    def get(self):
        """下载"""
        pass
