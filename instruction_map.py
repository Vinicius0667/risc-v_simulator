from Register import Register               #importa a classe register do arquivo register.py
from IInstructions import IInstructions     #importa a classe IInstructions do arquivo IInstructuions.py     
from UInstructions import UInstructions     #importa a classe UInstructions do arquivo UInstructuions.py
from RInstructions import RInstructions     #importa a classe RInstructions do arquivo RInstructuions.py

def setup():
    register = Register()                   
    
    iInstructions = IInstructions(register)
    uInstructions = UInstructions(register)
    rInstructions = RInstructions(register)
    
    return register, {
        # I Instructions Type
        'addi'  : iInstructions.addi,
        'addi': iInstructions.addi,
        'xori': iInstructions.xori,
        'ori': iInstructions.ori,
        'andi': iInstructions.andi,
        'slli': iInstructions.slli,
        
        # U Instructions Type
        'lui'   : uInstructions.lui,
        'auipc' : uInstructions.auipc,
        
        # R Instructiosn Type
        'add'   : rInstructions.add,
        'sub'   : rInstructions.sub,
        'xor'   : rInstructions.xor,
        'or'    : rInstructions.orR,
        'and'   : rInstructions.andR,
        'sll'   : rInstructions.sll,
        'srl'   : rInstructions.srl,
        'sra'   : rInstructions.sra,
        'slt'   : rInstructions.slt,
        'sltu'  : rInstructions.sltu,
    }