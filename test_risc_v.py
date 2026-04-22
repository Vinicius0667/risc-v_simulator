import os
import unittest
from unittest.mock import patch

from risc_v import main

class TestMainIntegration(unittest.TestCase):
    def setUp(self):
        self.input_test = "test_input.txt"
        self.output_test = "test_output.txt"

    def tearDown(self):
        for f in [self.input_test, self.output_test]:
            if os.path.exists(f):
                os.remove(f)

    def test_full_simulation_flow(self):
        content = "addi t0, zero, 10\naddi t1, t0, 5\nxori t2, t1, 3\n"
        with open(self.input_test, "w") as f:
            f.write(content)

        with patch("sys.argv", ["main.py", self.input_test, self.output_test]):
            main()

        self.assertTrue(os.path.exists(self.output_test))

        with open(self.output_test, "r") as f:
            lines = f.readlines()

        self.assertEqual(lines[0].strip(), "t0 = 10")
        self.assertEqual(lines[1].strip(), "t1 = 15")
        self.assertEqual(lines[2].strip(), "t2 = 12")

    def test_unknown_instruction(self):
        with open(self.input_test, "w") as f:
            f.write("wrong_instruction t0, t1, 10")

        with patch("sys.argv", ["main.py", self.input_test, self.output_test]):
            main()

        with open(self.output_test, "r") as f:
            content = f.read()

        self.assertIn("Unknown Instruction", content)
