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
    
    def orI (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 | number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def andI (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 & number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def sll (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 << number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def srl (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])

        if(number1 < 0):
            result = (number1 + 0x100000000)
        
        result = number1 >> number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def sra (self, args):
        number1 = self.register.read(args[1])
        number2 = self.register.read(args[2])
        
        result = number1 >> number2
        
        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
