class Memory:
    def __init__(self):
        self.memory = {}                                                    # Inicializa a memória como um dicionário para armazenamento esparso

    def write_byte(self, address, value):
        self.memory[address] = value & 0xFF                                 # Armazena um único byte no endereço especificado

    def read_byte(self, address):
        return self.memory.get(address, 0)                                  # Retorna o byte no endereço ou 0 caso o endereço não tenha sido escrito

    def write_halfword(self, address, value):
        self.write_byte(address, value & 0xFF)                              # Escreve o byte menos significativo (Little Endian)
        self.write_byte(address + 1, (value >> 8) & 0xFF)                   # Escreve o byte mais significativo da meia-palavra

    def read_halfword(self, address):
        low = self.read_byte(address)                                       # Lê o byte de menor peso
        high = self.read_byte(address + 1)                                  # Lê o byte de maior peso
        return (high << 8) | low                                            # Combina os bytes para formar a meia-palavra (16 bits)

    def write_word(self, address, value):
        for i in range(4):                                                  # Itera para decompor a palavra de 32 bits em 4 bytes
            self.write_byte(address + i, (value >> (i * 8)) & 0xFF)         # Escreve cada byte sequencialmente na memória

    def read_word(self, address):
        word = 0
        for i in range(4):                                                  # Itera para reconstruir a palavra a partir de 4 bytes
            word |= (self.read_byte(address + i) << (i * 8))                # Posiciona cada byte lido em seu respectivo lugar na palavra
        return word                                                         # Retorna a palavra completa (32 bits)
