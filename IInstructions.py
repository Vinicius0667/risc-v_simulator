from Register import Register

class IInstructions:
    def __init__(self, register: Register):
        self.register = register

    def addi(self, args):
        zero = self.register.read(args[1])
        value = zero + int(args[2])

        self.register.write(args[0], value)

        return f'{args[0]} = {args[2]}\n'
