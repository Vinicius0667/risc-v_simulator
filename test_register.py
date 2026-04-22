import unittest
from Register import Register

class TestRegister(unittest.TestCase):
    def setUp(self):
        self.register = Register()
        
    def testwriteAndReadDirect(self):
        self.register.write("x5", 100)
        self.assertEqual(self.register.read("x5"), 100)
        
    def testAbiAlias(self):
        self.register.write("t0", 200)
        self.assertEqual(self.register.read("t0"), 200)
        self.assertEqual(self.register.read("x5"), 200)
        
    def testAbiAliasWriteDirectRead(self):
        self.register.write("t0", 300)
        self.assertEqual(self.register.read("x5"), 300)
    
    def testZeroRegisterImmutable(self):
        self.register.write("x0", 999) 
        self.assertEqual(self.register.read("x0"), 0)
        
        self.register.write("zero", 111)
        self.assertEqual(self.register.read("zero"), 0)
        
    def testFpAndS0AreSame(self):
        self.register.write("fp", 50)
        
        self.assertEqual(self.register.read("fp"), 50)
        self.assertEqual(self.register.read("s0"), 50)
        self.assertEqual(self.register.read("x8"), 50)
        
    def testNonExistentRegister(self):
        self.assertEqual(self.register.read("test"), 0)
        