import unittest                                                             # Importa o framework de testes unitários

from RInstructions import RInstructions                                     # Importa a classe das instruções tipo R
from Register import Register                                               # Importa a classe de gerenciamento de registradores

class TestRInstructions(unittest.TestCase):
    def setUp(self):
        self.register = Register()                                          # Inicializa os registradores para o ambiente de teste
        self.r_instruction = RInstructions(self.register)                   # Instancia as instruções injetando o banco de registradores
        # Mock padrão para R-Type: [RD, RS1, RS2]
        self.default_mock = ["t0", "t1", "t2"]                              # Define a ordem padrão dos argumentos para instruções R

    def test_add_simple(self):
        self.register.write("t1", 10)                                       # Prepara o valor 10 em t1
        self.register.write("t2", 20)                                       # Prepara o valor 20 em t2
        
        result_string = self.r_instruction.add(self.default_mock)           # Executa a operação de soma (t0 = t1 + t2)

        self.assertEqual(self.register.read("t0"), 30)                      # Valida se o resultado da soma é 30
        self.assertEqual(result_string.strip(), "t0 = 30")                  # Valida a string de log gerada

    def test_sub_simple(self):
        self.register.write("t1", 50)                                       # Prepara o valor 50 em t1
        self.register.write("t2", 15)                                       # Prepara o valor 15 em t2
        
        result_string = self.r_instruction.sub(self.default_mock)           # Executa a subtração (t0 = t1 - t2)

        self.assertEqual(self.register.read("t0"), 35)                      # Valida se o resultado é 35
        self.assertEqual(result_string.strip(), "t0 = 35")

    def test_xor_simple(self):
        self.register.write("t1", 0b1010) # 10                              # Prepara valor binário em t1
        self.register.write("t2", 0b1100) # 12                              # Prepara valor binário em t2
        
        result_string = self.r_instruction.xor(self.default_mock)           # Executa a operação lógica XOR

        # 1010 ^ 1100 = 0110 (6)
        self.assertEqual(self.register.read("t0"), 6)                       # Valida o resultado binário da operação
        self.assertEqual(result_string.strip(), "t0 = 6")

    def test_orR_simple(self):
        self.register.write("t1", 0b1010) # 10                              # Prepara valor binário em t1
        self.register.write("t2", 0b1100) # 12                              # Prepara valor binário em t2
        
        result_string = self.r_instruction.orR(self.default_mock)           # Executa a operação lógica OR

        # 1010 | 1100 = 1110 (14)
        self.assertEqual(self.register.read("t0"), 14)                      # Valida o resultado lógico OR
        self.assertEqual(result_string.strip(), "t0 = 14")

    def test_andR_simple(self):
        self.register.write("t1", 0b1010) # 10                              # Prepara valor binário em t1
        self.register.write("t2", 0b1100) # 12                              # Prepara valor binário em t2
        
        result_string = self.r_instruction.andR(self.default_mock)          # Executa a operação lógica AND

        # 1010 & 1100 = 1000 (8)
        self.assertEqual(self.register.read("t0"), 8)                       # Valida o resultado lógico AND
        self.assertEqual(result_string.strip(), "t0 = 8")

    def test_sll_with_string_immediate(self):
        self.register.write("t1", 1)                                        # Valor a ser deslocado
        self.register.write("t2", 2)                                        # Valor do deslocamento guardado em t2
        
        # Agora passamos o NOME do registrador "t2" em vez da string "2"
        result_string = self.r_instruction.sll(["t0", "t1", "t2"])          

        self.assertEqual(self.register.read("t0"), 4)                             # 1 << 2 = 4
        self.assertEqual(result_string.strip(), "t0 = 4")

    def test_sll_hex_immediate(self):
        self.register.write("t1", 1)                                                   # Valor base
        self.register.write("t2", 3)                                                  # Deslocamento 3 (era o antigo 0x3)
        
        # O simulador Tipo R deve sempre referenciar registradores
        result_string = self.r_instruction.sll(["t0", "t1", "t2"])

        self.assertEqual(self.register.read("t0"), 8)                          # 1 << 3 = 8
        self.assertEqual(result_string.strip(), "t0 = 8")

    def test_srl_simple(self):
        self.register.write("t1", 16)                                       # Prepara valor 16
        self.register.write("t2", 2)                                        # Prepara deslocamento de 2 bits
        
        result_string = self.r_instruction.srl(self.default_mock)           # Executa shift lógico para a direita

        self.assertEqual(self.register.read("t0"), 4)                       # Valida que 16 >> 2 resultou em 4
        self.assertEqual(result_string.strip(), "t0 = 4")

    def test_srl_negative(self):
        self.register.write("t1", -16)                                      # Prepara valor negativo
        self.register.write("t2", 2)                                        # Define deslocamento
        
        result_string = self.r_instruction.srl(self.default_mock)           # Executa shift lógico (deve tratar como unsigned)

        self.assertEqual(self.register.read("t0"), 1073741820)              # Valida comportamento de shift lógico em 32 bits
        self.assertEqual(result_string.strip(), "t0 = 1073741820")

    def test_sra_negative(self):
        # Shift Right Arithmetic mantém o sinal
        self.register.write("t1", -16)                                      # Prepara valor negativo
        self.register.write("t2", 2)                                        # Define deslocamento
        
        result_string = self.r_instruction.sra(self.default_mock)           # Executa shift aritmético (preserva sinal)

        self.assertEqual(self.register.read("t0"), -4)                      # Valida que o sinal de negativo foi mantido
        self.assertEqual(result_string.strip(), "t0 = -4")

    def test_slt_true(self):
        self.register.write("t1", -5)                                       # Define valor menor
        self.register.write("t2", 2)                                        # Define valor maior
        
        result_string = self.r_instruction.slt(self.default_mock)           # Testa comparação "set less than"

        self.assertEqual(self.register.read("t0"), 1)                       # Valida que -5 < 2 (Verdadeiro = 1)
        self.assertEqual(result_string.strip(), "t0 = 1")

    def test_write_zero(self):
        self.register.write("t1", 10)                                       # Prepara valores para operação
        self.register.write("t2", 10)
        
        # Tentando escrever o resultado de ADD em zero/x0
        self.r_instruction.add(["zero", "t1", "t2"])                        # Tenta gravar soma no registrador imutável x0
        
        self.assertEqual(self.register.read("zero"), 0)                     # Garante que x0 permaneceu em zero