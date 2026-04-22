import re
from ast import arg

from Register import Register


class IInstructions:
    def __init__(self, register: Register):
        self.register = register

    def addi(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value + int(str(args[2]), 0)

        self.register.write(args[0], result)

        return f"{args[0]} = {result}\n"

    def xori(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value ^ int(str(args[2]), 0)

        self.register.write(args[0], result)

        return f"{args[0]} = {result}\n"

    def ori(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value | int(str(args[2]), 0)

        self.register.write(args[0], result)

        return f"{args[0]} = {result}"

    def andi(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value & int(str(args[2]), 0)

        self.register.write(args[0], result)

        return f"{args[0]} = {result}"

    def slli(self, args) -> str:
        register_value = self.register.read(args[1])
        shift_amout = int(str(args[2]), 0)

        shift_amout = shift_amout & 31

        result = register_value << shift_amout

        result = result & 0xFFFFFFFF

        if result > 0x7FFFFFFF:
            result -= 0x100000000

        self.register.write(args[0], result)
        return f"{args[0]} = {result}"

    def srli(self, args) -> str:
        register_value = self.register.read(args[1])
        shift_amout = int(str(args[2]), 0) & 31

        result = (register_value & 0xFFFFFFFF) >> shift_amout

        self.register.write(args[0], result)
        return f"{args[0]} = {result}"

    def srai(self, args) -> str:
        register_value = self.register.read(args[1])
        shift_amout = int(str(args[2]), 0) & 31

        result = register_value >> shift_amout

        result = result & 0xFFFFFFFF

        if result > 0x7FFFFFFF:
            result -= 0x100000000

        self.register.write(args[0], result)
        return f"{args[0]} = {result}"

    def slti(self, args) -> str:
        register_value = self.register.read(args[1])

        result = int(register_value < int(str(args[2]), 0))

        self.register.write(args[0], result)
        return f"{args[0]} = {result}"

    def sltiu(self, args) -> str:
        register_value = self.register.read(args[1]) & 0xFFFFFFFF

        immediate_value = int(str(args[2]), 0) & 0xFFFFFFFF

        result = int(register_value < immediate_value)

        self.register.write(args[0], result)
        return f"{args[0]} = {result}"
