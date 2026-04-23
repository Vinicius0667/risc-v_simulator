class Register:
    def __init__ (self):
        self.registers = {f"x{i}": 0 for i in range (32)}                   # Cria 32 registros x, numerados de 0 a 31 na lista registers
        
        # As seguintes linhas "criam" nomes alternativos para as variáveis em registro, possibilitando acessá-las através de nomes que implicam sua utilização
        self.abiName = {
            "zero": "x0", "ra": "x1", "sp": "x2", "gp": "x3", "tp": "x4", "s0": "x8", "fp": "x8", "s1": "x9"
        } 
        self.abiName.update({f"t{i}": f"x{i+5}" for i in range(3)})         # Cria alternativas para as variáveis temporárias que ocupam as variáveis de x5 a x7
        self.abiName.update({f"a{i}": f"x{i+10}" for i in range(8)})        # Cria alternativas para as variáveis de argumentos que ocupam as variáveis de x10 a x17
        self.abiName.update({f"s{i}": f"x{i+16}" for i in range(2, 12)})    # Cria alternativas para as variáveis salvas que ocupam as variáveis de x18 a x27
        self.abiName.update({f"t{i}": f"x{i+25}" for i in range(3, 7)})     # Cria alternativas para as variáveis temporárias que ocupam as variáveis de x28 a x31
        
    def write(self, name, value):
        realName = self.abiName.get(name, name)                             # Retorna o equivalente de name (ABI) para o nome real x0-x31
        
        if realName in ["x0", "zero"]:                                                # Impede a escrita no registro x0, que deve ser sempre zero no RISC-V
            return
        
        self.registers[realName] = value                                    # Escreve o valor fornecido no registro identificado

    def read(self, name):
        realName = self.abiName.get(name, name)                             # Converte nomes como 't0' ou 'sp' para o formato interno 'xN'
        
        return self.registers.get(realName, 0)                              # Retorna o valor atual do registro ou 0 por padrão