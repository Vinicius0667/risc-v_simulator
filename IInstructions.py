from Register import Register

class IInstructions:
    def __init__(self, register: Register):
        self.register = register

    def addi(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value + int(str(args[2]), 0)

        self.register.write(args[0], result)

        return f'{args[0]} = {result}\n'
    
    def xori(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value ^ int(str(args[2]), 0)
        
        self.register.write(args[0], result)
        
        return f'{args[0]} = {result}\n'
        
    def ori(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value | int(str(args[2]), 0)
        
        self.register.write(args[0], result)
        
        return f'{args[0]} = {result}'
        
    def andi(self, args) -> str:
        register_value = self.register.read(args[1])
        result = register_value & int(str(args[2]), 0)
        
        self.register.write(args[0], result)
        
        return f'{args[0]} = {result}'
        
    def slli(self, args) -> str:
        register_value = self.register.read(args[1])
        shamt = int(str(args[2]), 0)
        
        shamt = shamt & 31
        
        result = register_value << shamt
        
        result = result  & 0xFFFFFFFF
        
        if result > 0x7FFFFFFF:
            result -= 0x100000000
        
        
        self.register.write(args[0], result)
        return f'{args[0]} = {result}' 