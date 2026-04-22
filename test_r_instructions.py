import unittest

from RInstructions import RInstructions
from Register import Register

class TestRInstructions(unittest.TestCase):
    def setUp(self):
        self.register = Register()
        self.r_instruction = RInstructions(self.register)
        # Mock padrão para R-Type: [RD, RS1, RS2]
        self.default_mock = ["t0", "t1", "t2"]

    def test_add_simple(self):
        self.register.write("t1", 10)
        self.register.write("t2", 20)
        
        result_string = self.r_instruction.add(self.default_mock)

        self.assertEqual(self.register.read("t0"), 30)
        self.assertEqual(result_string.strip(), "t0 = 30")

    def test_sub_simple(self):
        self.register.write("t1", 50)
        self.register.write("t2", 15)
        
        result_string = self.r_instruction.sub(self.default_mock)

        self.assertEqual(self.register.read("t0"), 35)
        self.assertEqual(result_string.strip(), "t0 = 35")

    def test_xor_simple(self):
        self.register.write("t1", 0b1010) # 10
        self.register.write("t2", 0b1100) # 12
        
        result_string = self.r_instruction.xor(self.default_mock)

        # 1010 ^ 1100 = 0110 (6)
        self.assertEqual(self.register.read("t0"), 6)
        self.assertEqual(result_string.strip(), "t0 = 6")

    def test_orR_simple(self):
        self.register.write("t1", 0b1010) # 10
        self.register.write("t2", 0b1100) # 12
        
        result_string = self.r_instruction.orR(self.default_mock)

        # 1010 | 1100 = 1110 (14)
        self.assertEqual(self.register.read("t0"), 14)
        self.assertEqual(result_string.strip(), "t0 = 14")

    def test_andR_simple(self):
        self.register.write("t1", 0b1010) # 10
        self.register.write("t2", 0b1100) # 12
        
        result_string = self.r_instruction.andR(self.default_mock)

        # 1010 & 1100 = 1000 (8)
        self.assertEqual(self.register.read("t0"), 8)
        self.assertEqual(result_string.strip(), "t0 = 8")

    def test_sll_with_string_immediate(self):
        self.register.write("t1", 1)
        # sll converte args[2] usando int(str(args[2]), 0)
        result_string = self.r_instruction.sll(["t0", "t1", "2"])

        self.assertEqual(self.register.read("t0"), 4)
        self.assertEqual(result_string.strip(), "t0 = 4")

    def test_sll_hex_immediate(self):
        self.register.write("t1", 1)
        result_string = self.r_instruction.sll(["t0", "t1", "0x3"])

        self.assertEqual(self.register.read("t0"), 8) # 1 << 3
        self.assertEqual(result_string.strip(), "t0 = 8")

    def test_srl_simple(self):
        self.register.write("t1", 16)
        self.register.write("t2", 2)
        
        result_string = self.r_instruction.srl(self.default_mock)

        self.assertEqual(self.register.read("t0"), 4)
        self.assertEqual(result_string.strip(), "t0 = 4")

    def test_srl_negative(self):
        self.register.write("t1", -16)
        self.register.write("t2", 2)
        
        result_string = self.r_instruction.srl(self.default_mock)

        self.assertEqual(self.register.read("t0"), 1073741820)
        self.assertEqual(result_string.strip(), "t0 = 1073741820")

    def test_sra_negative(self):
        # Shift Right Arithmetic mantém o sinal
        self.register.write("t1", -16)
        self.register.write("t2", 2)
        
        result_string = self.r_instruction.sra(self.default_mock)

        self.assertEqual(self.register.read("t0"), -4)
        self.assertEqual(result_string.strip(), "t0 = -4")

    def test_slt_true(self):
        self.register.write("t1", -5)
        self.register.write("t2", 2)
        
        result_string = self.r_instruction.slt(self.default_mock)

        self.assertEqual(self.register.read("t0"), 1)
        self.assertEqual(result_string.strip(), "t0 = 1")

    def test_write_zero(self):
        self.register.write("t1", 10)
        self.register.write("t2", 10)
        
        # Tentando escrever o resultado de ADD em zero/x0
        self.r_instruction.add(["zero", "t1", "t2"])
        
        self.assertEqual(self.register.read("zero"), 0)
