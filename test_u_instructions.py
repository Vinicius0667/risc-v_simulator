import unittest                                                             # Importa o framework de testes unitários

from UInstructions import UInstructions                                     # Importa a classe das instruções tipo U
from Register import Register                                               # Importa a classe de gerenciamento de registradores

class TestUInstructions(unittest.TestCase):
    def setUp(self):
        self.register = Register()                                          # Inicializa o banco de registradores para os testes
        self.u_instruction = UInstructions(self.register)                   # Instancia as instruções injetando os registradores
        # O MOCK CORRETO: [RD, IMEDIATO]
        self.default_mock = ["t0", "0x12345"]                               # Define o mock corrigido: destino e valor imediato numérico

    def test_lui_simple(self):
        # Agora o mock envia o valor direto como o RISC-V espera
        result_string = self.u_instruction.lui(self.default_mock)           # Executa Load Upper Immediate (LUI)

        expected_value = 0x12345000                                         # Define o valor esperado (0x12345 deslocado 12 bits)
        self.assertEqual(self.register.read("t0"), expected_value)          # Valida se t0 recebeu o valor deslocado corretamente
        self.assertEqual(result_string.strip(), f"t0 = {expected_value}")    # Valida o log formatado da operação

    def test_auipc_simple(self):
        # RD=t0, IMM=1, PC=0 (assumido por falta de args[2])
        result_string = self.u_instruction.auipc(["t0", "1"])               # Testa AUIPC (soma o PC ao imediato deslocado)

        self.assertEqual(self.register.read("t0"), 4096)                    # Verifica se o resultado é 4096 (1 << 12 + PC 0)
        self.assertEqual(result_string.strip(), "t0 = 4096")                # Valida o log da operação

    def test_lui_zero(self):
        result_string = self.u_instruction.lui(["t0", "0"])                 # Testa LUI carregando o valor zero

        self.assertEqual(self.register.read("t0"), 0)                       # Valida que o registrador t0 contém zero
        self.assertEqual(result_string.strip(), "t0 = 0")

    def test_write_zero_register_u(self):
        # Tenta escrever no registrador zero
        self.u_instruction.lui(["zero", "0xFFFFF"])                         # Tenta gravar um valor imediato alto no registrador x0
        
        self.assertEqual(self.register.read("zero"), 0)                     # Valida que a proteção de escrita no zero funcionou

    def test_lui_negative_value(self):
        # Imediatos negativos são comuns em código assembly
        result_string = self.u_instruction.lui(["t0", "-1"])                # Testa o comportamento com imediato negativo (-1)
        
        self.assertEqual(self.register.read("t0"), -4096)                   # Valida se o shift manteve a integridade do sinal (-4096)
        self.assertEqual(result_string.strip(), "t0 = -4096")               # Valida o log final