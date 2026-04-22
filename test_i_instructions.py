import unittest

from IInstructions import IInstructions
from Register import Register


class TestIInstructions(unittest.TestCase):
    def setUp(self):
        self.register = Register()
        self.i_instruction = IInstructions(self.register)
        self.default_mock = ["t0", "zero", 20]

    def test_addi_simple(self):
        result_string = self.i_instruction.addi(self.default_mock)

        self.assertEqual(self.register.read(self.default_mock[0]), self.default_mock[2])

        self.assertEqual(result_string.strip(), "t0 = 20")

    def test_addi_negative(self):
        self.i_instruction.addi(self.default_mock)

        result_string = self.i_instruction.addi(["t0", "t0", "-5"])

        self.assertEqual(self.register.read(self.default_mock[0]), 15)

        self.assertEqual(result_string.strip(), "t0 = 15")

    def test_write_zero(self):
        self.i_instruction.addi(["x0", "zero", "20"])
        self.assertEqual(self.register.read("x0"), 0)

    def test_hex_immediate(self):
        self.default_mock[2] = "0x10"

        self.i_instruction.addi(self.default_mock)

        self.assertEqual(self.register.read(self.default_mock[0]), 16)

    def test_simple_xori(self):
        self.i_instruction.addi(self.default_mock)

        result_string = self.i_instruction.xori(["t1", "t0", 10])

        self.assertEqual(self.register.read("t1"), 30)
        self.assertEqual(result_string.strip(), "t1 = 30")

    def test_zero_xori(self):
        self.i_instruction.addi(self.default_mock)

        result_string = self.i_instruction.xori(["t1", "t0", 0])

        self.assertEqual(self.register.read("t1"), 20)
        self.assertEqual(result_string.strip(), "t1 = 20")

    def test_hex_xori(self):
        self.i_instruction.addi(self.default_mock)

        result_string = self.i_instruction.xori(["t1", "t0", "0xA"])

        self.assertEqual(self.register.read("t1"), 30)
        self.assertEqual(result_string.strip(), "t1 = 30")

    def test_negative_xori(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.xori(["t1", "t0", -1])

        self.assertEqual(self.register.read("t1"), -21)
        self.assertEqual(result_string.strip(), "t1 = -21")

    def test_simple_ori(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.ori(["t1", "t0", "4"])

        self.assertEqual(self.register.read("t1"), 20)
        self.assertEqual(result_string.strip(), "t1 = 20")

    def test_negative_ori(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.ori(["t1", "t0", "-5"])

        self.assertEqual(self.register.read("t1"), -1)
        self.assertEqual(result_string.strip(), "t1 = -1")

    def test_zero_ori(self):
        self.i_instruction.addi(self.default_mock)

        result_string = self.i_instruction.ori(["t1", "t0", 0])

        self.assertEqual(self.register.read("t1"), 20)
        self.assertEqual(result_string.strip(), "t1 = 20")

    def test_hex_ori(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.ori(["t1", "t0", "0xA"])

        self.assertEqual(self.register.read("t1"), 30)
        self.assertEqual(result_string.strip(), "t1 = 30")

    def test_simple_andi(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.andi(["t1", "t0", 7])

        self.assertEqual(self.register.read("t1"), 4)
        self.assertEqual(result_string.strip(), "t1 = 4")

    def test_negative_andi(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.andi(["t1", "t0", -5])

        self.assertEqual(self.register.read("t1"), 16)
        self.assertEqual(result_string.strip(), "t1 = 16")

    def test_zero_andi(self):
        self.i_instruction.addi(self.default_mock)

        result_string = self.i_instruction.andi(["t1", "t0", 0])

        self.assertEqual(self.register.read("t1"), 0)
        self.assertEqual(result_string.strip(), "t1 = 0")

    def test_hex_andi(self):
        self.i_instruction.addi(self.default_mock)
        result_string = self.i_instruction.andi(["t1", "t0", "0x7"])

        self.assertEqual(self.register.read("t1"), 4)
        self.assertEqual(result_string.strip(), "t1 = 4")

    def test_slli_positive(self):
        self.register.write("t0", 20)
        self.i_instruction.slli(["t1", "t0", "2"])
        self.assertEqual(self.register.read("t1"), 80)

    def test_slli_limit(self):
        self.register.write("t0", 1)
        self.i_instruction.slli(["t1", "t0", "31"])
        self.assertEqual(self.register.read("t1"), -2147483648)
