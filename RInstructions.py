from Register import Register                                               # Importa a classe Register para manipulação de registradores

class RInstructions:
    def __init__(self, register: Register):
        self.register = register                                            # Armazena a referência do banco de registradores

    def add (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor do primeiro registrador de origem (rs1)
        number2 = self.register.read(args[2])                               # Lê o valor do segundo registrador de origem (rs2)

        result = number1 + number2                                          # Realiza a soma aritmética entre os dois valores

        self.register.write(args[0], result)                                # Escreve o resultado no registrador de destino (rd)

        return f'{args[0]} = {result}\n'                                    # Retorna o log da operação formatado

    def sub (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor de rs1
        number2 = self.register.read(args[2])                               # Lê o valor de rs2

        result = number1 - number2                                          # Realiza a subtração aritmética (rs1 - rs2)

        self.register.write(args[0], result)                                # Salva o resultado no registrador rd

        return f'{args[0]} = {result}\n'

    def xor (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor de rs1
        number2 = self.register.read(args[2])                               # Lê o valor de rs2

        result = number1 ^ number2                                          # Realiza a operação lógica XOR bit a bit

        self.register.write(args[0], result)                                # Armazena o resultado em rd

        return f'{args[0]} = {result}\n'

    def orR (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor de rs1
        number2 = self.register.read(args[2])                               # Lê o valor de rs2

        result = number1 | number2                                          # Realiza a operação lógica OR bit a bit

        self.register.write(args[0], result)                                # Armazena o resultado em rd

        return f'{args[0]} = {result}\n'

    def andR (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor de rs1
        number2 = self.register.read(args[2])                               # Lê o valor de rs2

        result = number1 & number2                                          # Realiza a operação lógica AND bit a bit

        self.register.write(args[0], result)                                # Armazena o resultado em rd

        return f'{args[0]} = {result}\n'

    def sll (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor do registrador rs1
        
        number2 = self.register.read(args[2])                               # Lê o valor do registrador rs2 (ex: t4)

        number2 = number2 & 31                                              # Limita o deslocamento a 5 bits (0-31)

        result = number1 << number2                                         # Realiza o shift lógico para a esquerda
        result = result & 0xFFFFFFFF                                        # Trunca para 32 bits

        if result > 0x7FFFFFFF:                                             # Ajusta para representação de sinal do Python
            result -= 0x100000000

        self.register.write(args[0], result)                                # Escreve no registrador de destino rd
        return f'{args[0]} = {result}\n'

    def srl (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor base
        number2 = self.register.read(args[2])                               # Lê a quantidade do deslocamento do registrador

        number2 = number2 & 31                                              # Limita o deslocamento a 31 posições
        number1 = number1 & 0xFFFFFFFF                                      # Trata o valor como unsigned para shift lógico

        result = number1 >> number2                                         # Realiza o shift lógico para a direita

        self.register.write(args[0], result)                                # Salva o resultado em rd

        return f'{args[0]} = {result}\n'

    def sra (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor base (com sinal preservado pelo Python)
        number2 = self.register.read(args[2])                               # Lê a quantidade do deslocamento

        result = number1 >> number2                                         # Realiza o shift aritmético para a direita

        self.register.write(args[0], result)                                # Escreve o resultado em rd

        return f'{args[0]} = {result}\n'

    def slt (self, args):
        number1 = self.register.read(args[1])                               # Lê o valor de rs1 (com sinal)
        number2 = self.register.read(args[2])                               # Lê o valor de rs2 (com sinal)

        result = 1 if number1 < number2 else 0                              # Define 1 se rs1 for menor que rs2, caso contrário 0

        self.register.write(args[0], result)                                # Salva o booleano (0 ou 1) em rd

        return f'{args[0]} = {result}\n'

    def sltu (self, args):
        number1 = self.register.read(args[1])                               # Lê rs1
        number2 = self.register.read(args[2])                               # Lê rs2

        result = 1 if number1 < number2 else 0                              # Realiza a comparação (lógica unsigned deve ser tratada)

        self.register.write(args[0], result)                                # Salva o resultado em rd

        return f'{args[0]} = {result}\n'
