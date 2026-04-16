class Register:
    def __init__ (self):
        self.registers = {f"x{i}": 0 for i in range (32)}
        
        self.abiName = {
            "zero": "x0", "ra": "x1", "sp": "x2", "gp": "x3", "tp": "x4", "s0": "x8", "fp": "x8", "s1": "x9"
        }
        
        self.abiName.update({f"t{i}": f"x{i+5}" for i in range(3)})
        self.abiName.update({f"a{i}": f"x{i+10}" for i in range(8)})
        self.abiName.update({f"s{i}": f"x{i+16}" for i in range(2, 12)})
        self.abiName.update({f"t{i}": f"x{i+25}" for i in range(3, 7)})
        
    def save(self, name, value):
        realName = self.abiName.get(name, name)
        
        if realName == "x0":
            return
        
        self.registers[realName] = value
        
    def read(self, name):
        realName = self.abiName.get(name, name)
        
        return self.registers.get(realName, 0)