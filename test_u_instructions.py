import unittest

from UInstructions import UInstructions
from Register import Register

class TestUInstructions(unittest.TestCase):
    def setUp(self):
        self.register = Register()
        self.u_instruction = UInstructions(self.register)
        self.default_mock = ["t0", "t1"]

    def test_lui_simple(self):
        # Prepara o registrador de origem com o valor 0x12345
        self.register.write("t1", 0x12345)
        
        result_string = self.u_instruction.lui(self.default_mock)

        # 0x12345 << 12 = 0x12345000 (305418240 em decimal)
        expected_value = 0x12345000
        self.assertEqual(self.register.read("t0"), expected_value)
        self.assertEqual(result_string.strip(), f"t0 = {expected_value}")

    def test_auipc_simple(self):
        self.register.write("t1", 1)
        
        result_string = self.u_instruction.auipc(self.default_mock)

        # 1 << 12 = 4096
        self.assertEqual(self.register.read("t0"), 4096)
        self.assertEqual(result_string.strip(), "t0 = 4096")

    def test_lui_zero(self):
        self.register.write("t1", 0)
        
        result_string = self.u_instruction.lui(self.default_mock)

        self.assertEqual(self.register.read("t0"), 0)
        self.assertEqual(result_string.strip(), "t0 = 0")

    def test_write_zero_register_u(self):
        # Testa se a escrita no registrador zero é protegida
        self.register.write("t1", 0xFFFFF)
        
        self.u_instruction.lui(["zero", "t1"])
        
        self.assertEqual(self.register.read("zero"), 0)

    def test_lui_negative_value(self):
        # Testa como o shift se comporta com valores negativos no registrador
        self.register.write("t1", -1)
        
        result_string = self.u_instruction.lui(self.default_mock)
        
        # Em Python, -1 << 12 resulta em -4096
        self.assertEqual(self.register.read("t0"), -4096)
        self.assertEqual(result_string.strip(), "t0 = -4096")