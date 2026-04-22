from Register import Register

class UInstructions:
    def __init__(self, register: Register):
        self.register = register

    def lui(self, args):
        number1 = self.register.read(args[1])

        result = number1 << 12

        self.register.write(args[0], result)

        return f"{args[0]} = {result}\n"

    def auipc(self, args):
        number1 = self.register.read(args[1])
        result = number1 << 12

        self.register.write(args[0], result)

        return f"{args[0]} = {result}\n"
