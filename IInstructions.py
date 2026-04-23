from Memory import Memory                                                   # Importa a classe de memória
from Register import Register                                               # Importa a classe de registradores

class IInstructions:
    def __init__(self, register: Register, memory: Memory):
        self.register = register                                            # Armazena a referência dos registradores
        self.memory = memory                                                # Armazena a referência da memória

    def addi(self, args) -> str:
        register_value = self.register.read(args[1])                        # Lê o valor do registrador de origem
        result = register_value + int(str(args[2]), 0)                      # Soma o valor lido ao imediato (aceita hex ou dec)

        if args[0] in ['x0', 'zero']:
            result = 0

        self.register.write(args[0], result)                                # Escreve o resultado no registrador de destino
        

        return f"{args[0]} = {result}\n"                                    # Retorna a string de log da operação

    def xori(self, args) -> str:
        register_value = self.register.read(args[1])                        # Lê o valor do registrador rs1
        result = register_value ^ int(str(args[2]), 0)                      # Aplica a operação lógica XOR com o imediato

        self.register.write(args[0], result)                                # Salva o resultado no registrador rd

        return f"{args[0]} = {result}\n"

    def ori(self, args) -> str:
        register_value = self.register.read(args[1])                        # Lê o valor do registrador rs1
        result = register_value | int(str(args[2]), 0)                      # Aplica a operação lógica OR com o imediato

        self.register.write(args[0], result)                                # Salva o resultado no registrador rd

        return f"{args[0]} = {result}\n"

    def andi(self, args) -> str:
        register_value = self.register.read(args[1])                        # Lê o valor do registrador rs1
        result = register_value & int(str(args[2]), 0)                      # Aplica a operação lógica AND com o imediato

        self.register.write(args[0], result)                                # Salva o resultado no registrador rd

        return f"{args[0]} = {result}\n"

    def slli(self, args) -> str:
        register_value = self.register.read(args[1])                        # Obtém o valor base para o shift
        shift_amout = int(str(args[2]), 0)                                  # Converte o imediato para inteiro

        shift_amout = shift_amout & 31                                      # Garante que o shift seja no máximo de 5 bits (0-31)

        result = register_value << shift_amout                              # Realiza o shift lógico para a esquerda

        result = result & 0xFFFFFFFF                                        # Trunca o resultado para 32 bits

        if result > 0x7FFFFFFF:                                             # Verifica se o resultado deve ser negativo (extensão de sinal)
            result -= 0x100000000

        self.register.write(args[0], result)                                # Escreve o valor final no registrador
        return f"{args[0]} = {result}\n"

    def srli(self, args) -> str:
        register_value = self.register.read(args[1])                        # Obtém o valor base
        shift_amout = int(str(args[2]), 0) & 31                             # Limita o deslocamento a 31 posições

        result = (register_value & 0xFFFFFFFF) >> shift_amout               # Realiza shift lógico à direita em valor sem sinal

        self.register.write(args[0], result)                                # Salva no registrador rd
        return f"{args[0]} = {result}\n"

    def srai(self, args) -> str:
        register_value = self.register.read(args[1])                        # Obtém o valor base
        shift_amout = int(str(args[2]), 0) & 31                             # Limita o deslocamento a 31 posições

        result = register_value >> shift_amout                              # Realiza shift aritmético (preserva o sinal)

        result = result & 0xFFFFFFFF                                        # Aplica máscara de 32 bits

        if result > 0x7FFFFFFF:                                             # Reajusta o sinal para a representação do Python
            result -= 0x100000000

        self.register.write(args[0], result)                                # Salva no registrador rd
        return f"{args[0]} = {result}\n"

    def slti(self, args) -> str:
        register_value = self.register.read(args[1])                        # Lê o valor com sinal do registrador

        result = int(register_value < int(str(args[2]), 0))                 # Verifica se é menor que o imediato (com sinal)

        self.register.write(args[0], result)                                # Define 1 se verdadeiro, 0 se falso
        return f"{args[0]} = {result}\n"

    def sltiu(self, args) -> str:
        register_value = self.register.read(args[1]) & 0xFFFFFFFF           # Converte o valor do registrador para sem sinal

        immediate_value = int(str(args[2]), 0) & 0xFFFFFFFF                 # Converte o imediato para sem sinal

        result = int(register_value < immediate_value)                      # Realiza a comparação sem sinal

        self.register.write(args[0], result)                                # Salva o resultado booleano
        return f"{args[0]} = {result}\n"

    def lb(self, args) -> str:
        base_value = self.register.read(args[2])                            # Lê o endereço base do registrador
        offset = int(str(args[1]), 0)                                       # Obtém o deslocamento
        address = base_value + offset                                       # Calcula o endereço final na memória

        value = self.memory.read_byte(address)                              # Lê um único byte da memória
        if value > 0x7F:                                                    # Realiza a extensão de sinal para 32 bits
            value -= 0x100

        self.register.write(args[0], value)                                 # Armazena o byte estendido no rd
        return f"{args[0]} = {value}\n"

    def lh(self, args) -> str:
        base_value = self.register.read(args[2])                            # Lê o endereço base
        offset = int(str(args[1]), 0)                                       # Obtém o deslocamento
        address = base_value + offset                                       # Calcula o endereço

        value = self.memory.read_halfword(address)                          # Lê 16 bits da memória
        if value > 0x7FFF:                                                  # Realiza a extensão de sinal
            value -= 0x10000

        self.register.write(args[0], value)                                 # Armazena no rd
        return f"{args[0]} = {value}\n"

    def lw(self, args) -> str:
        base_value = self.register.read(args[2])                            # Lê o endereço base
        offset = int(str(args[1]), 0)                                       # Obtém o deslocamento
        address = base_value + offset                                       # Calcula o endereço

        value = self.memory.read_word(address)                              # Lê 32 bits da memória
        if value > 0x7FFFFFFF:                                              # Ajusta o sinal para o Python
            value -= 0x100000000

        self.register.write(args[0], value)                                 # Armazena no rd
        return f"{args[0]} = {value}\n"

    def lbu(self, args) -> str:
        base_value = self.register.read(args[2])                            # Calcula endereço base
        offset = int(str(args[1]), 0)                                       # Define offset
        address = base_value + offset                                       # Endereço final

        value = self.memory.read_byte(address) & 0xFF                       # Lê byte sem aplicar extensão de sinal
        self.register.write(args[0], value)                                 # Salva valor puro no rd
        return f"{args[0]} = {value}\n"

    def lhu(self, args) -> str:
        base_value = self.register.read(args[2])                            # Endereço base
        offset = int(str(args[1]), 0)                                       # Offset
        address = base_value + offset                                       # Endereço final

        value = self.memory.read_halfword(address) & 0xFFFF                 # Lê meia-palavra sem extensão de sinal
        self.register.write(args[0], value)                                 # Salva no rd
        return f"{args[0]} = {value}\n"

    def jalr(self, args) -> str:
        current_pc = int(args[3])                                           # Recupera o PC atual passado pelo simulador
        base_value = self.register.read(args[2])                            # Lê o valor base para o salto
        offset = int(str(args[1]), 0)                                       # Obtém o offset do salto

        self.register.write(args[0], current_pc + 4)                        # Salva o endereço de retorno (PC + 4) no rd
        new_pc = (base_value + offset) & ~1                                 # Calcula novo PC forçando o último bit a zero

        return f"NEXT_PC={new_pc}\n"                                          # Informa ao simulador o endereço do salto

    def ecall(self, args=None) -> str:
        return "Environment Call\n"                                           # Retorna identificação de chamada de sistema

    def ebreak(self, args=None) -> str:
        return "Breakpoint\n"                                                 # Retorna identificação de parada para depuração
