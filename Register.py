class Register:
    def __init__ (self):
        self.registers = {f"x{i}": 0 for i in range (32)}                   #cria 32 registros x, numerados de 0 a 31 na lista registers
        
        #As seguintes linhas "criam" nomes alternativos para as variaveis em registro, possibilitando acessa-las atrávez de nomes que implicam sua utilização
        self.abiName = {
            "zero": "x0", "ra": "x1", "sp": "x2", "gp": "x3", "tp": "x4", "s0": "x8", "fp": "x8", "s1": "x9"
        } 
        self.abiName.update({f"t{i}": f"x{i+5}" for i in range(3)})         #cria alternativas para as variaveis temporarias que ocupam as variaveis de x5 a x7
        self.abiName.update({f"a{i}": f"x{i+10}" for i in range(8)})        #cria alternativas para as variaveis de argumentos que ocupam as variaveis de x10 a x17
        self.abiName.update({f"s{i}": f"x{i+16}" for i in range(2, 12)})    #cria alternativas para as variaveis salvas que ocupam as variaveis de x18 a x27
        self.abiName.update({f"t{i}": f"x{i+25}" for i in range(3, 7)})     #cria alternativas para as variaveis salvas que ocupam as variaveis de x28 a x31
        
    def write(self, name, value):
        realName = self.abiName.get(name, name)                             #retorna o equivalente de name, caso tenha sido escrito como xy ou ty e assim em diante
        
        if realName == "x0":                                                #sai da função escrita caso o nome da variavel seja x0 ou zero que é a variavel estática equivalente a 0x0
            return
        
        self.registers[realName] = value                                    #escreve o valor value no registro name

    def read(self, name):
        realName = self.abiName.get(name, name)                             #retorna o equivalente de name, caso tenha sido escrito como xy ou ty e assim em diante
        
        return self.registers.get(realName, 0)                              #retorna o valor guardado pelo registro name
