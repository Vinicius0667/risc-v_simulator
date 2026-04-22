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
    
    def sub (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 - number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def xor (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 ^ number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def orR (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 | number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def andR (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 & number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def sll (self, args):
        number1 = self.register.read(args[1])
        number2 = int(str(args[2]), 0)
        number2 = number2 & 31
        
        result = number1 << number2

        result = result & 0xFFFFFFFF

        if result > 0x7FFFFFFF:
            result -= 0x100000000
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def srl (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])

        number2 = number2 & 31

        number1 = number1 & 0xFFFFFFFF

        result = number1 >> number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def sra (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 >> number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def slt (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = 1 if number1 < number2 else 0
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def sltu (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = 1 if number1 < number2 else 0
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
