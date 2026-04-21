from Register import Register

class RInstructions:
    def __init__(self, register: Register):
        self.register = register
        
    def add (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 + number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'