from Register import Register                                               # Importa a classe Register para manipular os registradores

class UInstructions:
    def __init__(self, register: Register):
        self.register = register                                            # Armazena a referência do banco de registradores

    def lui(self, args):
        # O erro acontecia aqui: args[1] vinha como "t1" em vez de um número
        immediate = int(str(args[1]), 0)                                    # Converte o imediato (pode ser "10" ou "0x10")

        result = immediate << 12                                            # Desloca 12 bits para a esquerda

        self.register.write(args[0], result)                                # Salva no registrador de destino (rd)

        return f"{args[0]} = {result}\n"

    def auipc(self, args):
        immediate = int(str(args[1]), 0)                                    # Converte o imediato
        # Garante que o PC seja um inteiro; se não houver args[2], assume 0
        pc = int(args[2]) if len(args) > 2 else 0

        result = pc + (immediate << 12)                                     # Soma PC ao imediato deslocado

        self.register.write(args[0], result)                                # Salva no registrador rd

        return f"{args[0]} = {result}\n"
