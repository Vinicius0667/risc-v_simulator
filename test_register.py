import unittest                                                             # Importa o framework de testes unitários
from Register import Register                                               # Importa a classe Register que será testada

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.register = Register()                                          # Instancia um novo banco de registradores para cada teste
        
    def testwriteAndReadDirect(self):
        self.register.write("x5", 100)                                      # Testa a escrita direta usando o nome real do registrador
        self.assertEqual(self.register.read("x5"), 100)                     # Verifica se o valor lido é o mesmo que foi escrito
        
    def testAbiAlias(self):
        self.register.write("t0", 200)                                      # Testa a escrita usando o apelido da ABI (t0)
        self.assertEqual(self.register.read("t0"), 200)                     # Verifica a leitura pelo apelido
        self.assertEqual(self.register.read("x5"), 200)                     # Verifica se o apelido t0 mapeou corretamente para x5
        
    def testAbiAliasWriteDirectRead(self):
        self.register.write("t0", 300)                                      # Escreve via apelido t0
        self.assertEqual(self.register.read("x5"), 300)                     # Valida que a alteração refletiu no registrador físico x5
    
    def testZeroRegisterImmutable(self):
        self.register.write("x0", 999)                                      # Tenta escrever no registrador x0 (deve ser imutável)
        self.assertEqual(self.register.read("x0"), 0)                       # Verifica se ele permanece em 0
        
        self.register.write("zero", 111)                                    # Tenta escrever usando o apelido "zero"
        self.assertEqual(self.register.read("zero"), 0)                     # Verifica se o bloqueio de escrita também funciona para o apelido
        
    def testFpAndS0AreSame(self):
        self.register.write("fp", 50)                                       # Testa o mapeamento duplo (fp e s0 referenciam x8)
        
        self.assertEqual(self.register.read("fp"), 50)                      # Valida leitura por fp
        self.assertEqual(self.register.read("s0"), 50)                      # Valida leitura por s0
        self.assertEqual(self.register.read("x8"), 50)                      # Valida que o valor físico está em x8
        
    def testNonExistentRegister(self):
        self.assertEqual(self.register.read("test"), 0)                     # Valida que a leitura de um nome inexistente retorna 0 por padrão