import os                                                                   # Importa funções do sistema operacional para manipular arquivos
import unittest                                                             # Importa o framework de testes unitários
from unittest.mock import patch                                             # Importa ferramenta para simular argumentos de linha de comando

from risc_v import main                                                     # Importa a função principal do simulador para teste de integração

class TestMainIntegration(unittest.TestCase):
    def setUp(self):
        self.input_test = "test_input.txt"                                  # Define nome do arquivo de entrada temporário para testes
        self.output_test = "test_output.txt"                                # Define nome do arquivo de saída temporário para testes

    def tearDown(self):
        for f in [self.input_test, self.output_test]:                       # Itera sobre os arquivos criados
            if os.path.exists(f):                                           # Verifica se o arquivo ainda existe
                os.remove(f)                                                # Remove os arquivos temporários para limpar o ambiente de teste

    def test_full_simulation_flow(self):
        content = "addi t0, zero, 10\naddi t1, t0, 5\nxori t2, t1, 3\n"     # Define um programa RISC-V simples para teste
        with open(self.input_test, "w") as f:
            f.write(content)                                                # Grava o programa no arquivo de entrada de teste

        with patch("sys.argv", ["main.py", self.input_test, self.output_test]): # Simula a execução via terminal com argumentos
            main()                                                          # Executa o simulador completo

        self.assertTrue(os.path.exists(self.output_test))                    # Verifica se o arquivo de saída foi gerado com sucesso

        with open(self.output_test, "r") as f:
            lines = f.readlines()                                           # Lê o resultado gerado pelo simulador

        self.assertEqual(lines[0].strip(), "t0 = 10")                       # Valida o resultado da primeira instrução
        self.assertEqual(lines[1].strip(), "t1 = 15")                       # Valida o resultado da segunda instrução
        self.assertEqual(lines[2].strip(), "t2 = 12")                       # Valida o resultado da terceira instrução

    def test_unknown_instruction(self):
        with open(self.input_test, "w") as f:
            f.write("wrong_instruction t0, t1, 10")                         # Grava uma instrução inválida para teste de erro

        with patch("sys.argv", ["main.py", self.input_test, self.output_test]): # Simula a execução do simulador
            main()

        with open(self.output_test, "r") as f:
            content = f.read()                                              # Lê o log de erro gerado

        self.assertIn("Unknown Instruction", content)                       # Garante que o erro foi identificado e logado corretamente