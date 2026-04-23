import unittest                                                             # Importa o framework de testes unitários

from IInstructions import IInstructions                                     # Importa a classe das instruções tipo I
from Register import Register                                               # Importa a classe de registradores
from Memory import Memory                                                   # Importa a classe de memória


class TestIInstructions(unittest.TestCase):
    def setUp(self):
        self.register = Register()                                          # Instancia registradores para cada teste
        self.memory = Memory()                                              # Instancia memória para cada teste
        self.i_instruction = IInstructions(self.register, self.memory)      # Instancia a classe de instruções injetando as dependências
        self.default_mock = ['t0', 'zero', '20']                            # Define um mock padrão de argumentos [rd, rs1, imm]

    def test_addi_simple(self):
        result_string = self.i_instruction.addi(self.default_mock)          # Executa addi t0, zero, 20

        self.assertEqual(self.register.read(self.default_mock[0]), 20)      # Verifica se t0 agora vale 20
        self.assertEqual(result_string.strip(), 't0 = 20')                  # Valida a string de retorno do log

    def test_addi_negative(self):
        self.i_instruction.addi(self.default_mock)                          # Primeiro define t0 = 20
        result_string = self.i_instruction.addi(['t0', 't0', '-5'])         # Executa t0 = t0 - 5

        self.assertEqual(self.register.read('t0'), 15)                      # Valida se a subtração via addi funcionou
        self.assertEqual(result_string.strip(), 't0 = 15')

    def test_write_zero(self):
        self.i_instruction.addi(['x0', 'zero', '20'])                       # Tenta escrever 20 no registrador x0
        
        self.assertEqual(self.register.read('x0'), 0)                       # Valida se x0 permanece 0 (imutabilidade)

    def test_hex_immediate(self):
        self.i_instruction.addi(['t0', 'zero', '0x10'])                     # Testa se o simulador aceita imediatos em hexadecimal
        
        self.assertEqual(self.register.read('t0'), 16)                      # 0x10 deve ser convertido para 16

    def test_simple_xori(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20

        result_string = self.i_instruction.xori(['t1', 't0', '10'])         # 20 XOR 10 = 30

        self.assertEqual(self.register.read('t1'), 30)
        self.assertEqual(result_string.strip(), 't1 = 30')

    def test_zero_xori(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        result_string = self.i_instruction.xori(['t1', 't0', '0'])          # 20 XOR 0 = 20

        self.assertEqual(self.register.read('t1'), 20)
        self.assertEqual(result_string.strip(), 't1 = 20')

    def test_hex_xori(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        result_string = self.i_instruction.xori(['t1', 't0', '0xA'])        # 20 XOR 10 (0xA) = 30

        self.assertEqual(self.register.read('t1'), 30)
        self.assertEqual(result_string.strip(), 't1 = 30')

    def test_negative_xori(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        result_string = self.i_instruction.xori(['t1', 't0', '-1'])         # Testa XOR com imediato negativo (extensão de sinal)

        self.assertEqual(self.register.read('t1'), -21)
        self.assertEqual(result_string.strip(), 't1 = -21')

    def test_simple_ori(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20 (10100)
        result_string = self.i_instruction.ori(['t1', 't0', '4'])           # 20 OR 4 (00100) = 20 (10100)

        self.assertEqual(self.register.read('t1'), 20)
        self.assertEqual(result_string.strip(), 't1 = 20')

    def test_negative_ori(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        result_string = self.i_instruction.ori(['t1', 't0', '-5'])          # OR com imediato negativo resulta em -1 (todos bits 1)

        self.assertEqual(self.register.read('t1'), -1)
        self.assertEqual(result_string.strip(), 't1 = -1')

    def test_zero_ori(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.ori(['t1', 't0', '0'])

        self.assertEqual(self.register.read('t1'), 20)
        self.assertEqual(result_string.strip(), 't1 = 20')

    def test_hex_ori(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.ori(['t1', 't0', '0xA'])

        self.assertEqual(self.register.read('t1'), 30)
        self.assertEqual(result_string.strip(), 't1 = 30')

    def test_simple_andi(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20 (10100)
        result_string = self.i_instruction.andi(['t1', 't0', '7'])          # 20 AND 7 (00111) = 4 (00100)

        self.assertEqual(self.register.read('t1'), 4)
        self.assertEqual(result_string.strip(), 't1 = 4')

    def test_negative_andi(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.andi(['t1', 't0', '-5'])

        self.assertEqual(self.register.read('t1'), 16)
        self.assertEqual(result_string.strip(), 't1 = 16')

    def test_zero_andi(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.andi(['t1', 't0', '0'])

        self.assertEqual(self.register.read('t1'), 0)
        self.assertEqual(result_string.strip(), 't1 = 0')

    def test_hex_andi(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.andi(['t1', 't0', '0x7'])

        self.assertEqual(self.register.read('t1'), 4)
        self.assertEqual(result_string.strip(), 't1 = 4')

    def test_slli_positive(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        self.i_instruction.slli(['t1', 't0', '2'])                          # 20 << 2 = 80
        
        self.assertEqual(self.register.read('t1'), 80)

    def test_slli_limit(self):
        self.i_instruction.addi(['t0', 'zero', '1'])
        self.i_instruction.slli(['t1', 't0', '31'])                         # Shift de 31 bits resulta no bit de sinal ligado
        
        self.assertEqual(self.register.read('t1'), -2147483648)             # Valida comportamento de 32 bits assinado

    def test_srli_positive(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        self.i_instruction.srli(['t1', 't0', '2'])                          # 20 >> 2 = 5
        
        self.assertEqual(self.register.read('t1'), 5)

    def test_srli_negative_to_positive(self):
        self.i_instruction.addi(['t0', 'zero', '-2'])
        self.i_instruction.srli(['t1', 't0', '1'])                          # Shift lógico de valor negativo resulta em positivo grande
        
        self.assertEqual(self.register.read('t1'), 2147483647)

    def test_srai_negative(self):
        self.i_instruction.addi(['t0', 'zero', '-20'])
        self.i_instruction.srai(['t1', 't0', '2'])                          # Shift aritmético preserva o sinal negativo (-5)
        
        self.assertEqual(self.register.read('t1'), -5)

    def test_srai_positive(self):
        self.i_instruction.addi(self.default_mock)
        self.i_instruction.srai(['t1', 't0', '2'])
        
        self.assertEqual(self.register.read('t1'), 5)

    def test_simple_slti(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        self.i_instruction.slti(['t1', 't0', '30'])                         # 20 < 30? Sim (1)

        self.assertEqual(self.register.read('t1'), 1)

    def test_slti_immediately_less(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        self.i_instruction.slti(['t1', 't0', '10'])                         # 20 < 10? Não (0)
        
        self.assertEqual(self.register.read('t1'), 0)

    def test_slti_negative_value(self):
        self.i_instruction.addi(self.default_mock)                          # t0 = 20
        self.i_instruction.slti(['t1', 't0', '-30'])                        # 20 < -30? Não (0)

        self.assertEqual(self.register.read('t1'), 0)

    def test_sltiu_simple_true(self):
        self.i_instruction.addi(['t0', 'zero', '10'])
        self.i_instruction.sltiu(['t1', 't0', '20'])                        # Comparação sem sinal: 10 < 20? (1)
        
        self.assertEqual(self.register.read('t1'), 1)

    def test_sltiu_simple_false(self):
        self.i_instruction.addi(['t0', 'zero', '30'])
        self.i_instruction.sltiu(['t1', 't0', '20'])                        # 30 < 20? (0)
        
        self.assertEqual(self.register.read('t1'), 0)

    def test_sltiu_with_negative_input(self):
        self.i_instruction.addi(['t0', 'zero', '-1'])                       # -1 em unsigned é o maior valor possível
        self.i_instruction.sltiu(['t1', 't0', '100'])                       # Max < 100? Não (0)

        self.assertEqual(self.register.read('t1'), 0)

    def test_sltiu_hex_immediate(self):
        self.i_instruction.addi(['t0', 'zero', '5'])

        self.i_instruction.sltiu(['t1', 't0', '0xF'])                       # 5 < 15? Sim (1)
        self.assertEqual(self.register.read('t1'), 1)

    def test_lw_standard(self):
        self.memory.write_word(0x400, 123456)                               # Escreve na memória simulada
        self.register.write('t0', 0x400)                                    # t0 guarda o endereço
        
        self.i_instruction.lw(['t1', '0', 't0'])                            # Lê word de t0 + 0
        self.assertEqual(self.register.read('t1'), 123456)

    def test_lb_signed(self):
        self.memory.write_byte(0x500, 0x81)                                 # Escreve byte com bit de sinal ligado
        self.register.write('t0', 0x500)
        
        self.i_instruction.lb(['t1', '0', 't0'])                            # LB deve estender o sinal
        self.assertEqual(self.register.read('t1'), -127)                    # 0x81 em 8 bits assinado é -127

    def test_lbu_unsigned(self):
        self.memory.write_byte(0x500, 0x81)
        self.register.write('t0', 0x500)
        self.i_instruction.lbu(['t1', '0', 't0'])                           # LBU não estende o sinal
        self.assertEqual(self.register.read('t1'), 129)                     # 0x81 em unsigned é 129

    def test_lh_signed(self):
        self.memory.write_halfword(0x600, 0x8001)                           # Escreve halfword assinado
        self.register.write('t0', 0x600)
        self.i_instruction.lh(['t1', '0', 't0'])                            # LH deve estender o sinal
        self.assertEqual(self.register.read('t1'), -32767)

    def test_lhu_unsigned(self):
        self.memory.write_halfword(0x600, 0x8001)
        self.register.write('t0', 0x600)

        self.i_instruction.lhu(['t1', '0', 't0'])                           # LHU carrega apenas o valor positivo
        self.assertEqual(self.register.read('t1'), 32769)

    def test_jalr_flow(self):
        self.register.write('t0', 1000)                                     # Define base do salto
        result = self.i_instruction.jalr(['ra', '4', 't0', '500'])          # Executa jalr com PC fake = 500

        self.assertEqual(self.register.read('ra'), 504)                     # ra deve salvar PC + 4
        self.assertEqual(result.strip(), 'NEXT_PC=1004')                            # Novo PC deve ser t0 + offset

    def test_system_calls(self):
        self.assertEqual(self.i_instruction.ecall().strip(), 'Environment Call')    # Valida retorno das chamadas de sistema
        self.assertEqual(self.i_instruction.ebreak().strip(), 'Breakpoint')

    def test_load_with_offset(self):
        self.memory.write_word(0x704, 99)                                   # Escreve no endereço 704
        self.register.write('t0', 0x700)                                    # Base em 700

        self.i_instruction.lw(['t1', '4', 't0'])                            # Lê 700 + 4
        self.assertEqual(self.register.read('t1'), 99)