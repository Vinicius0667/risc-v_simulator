from Register import Register
from IInstructions import IInstructions
from UInstructions import UInstructions
from RInstructions import RInstructions

def setup():
    register = Register()
    
    iInstructions = IInstructions(register)
    uInstructions = UInstructions(register)
    rInstructions = RInstructions(register)
    
    return register, {
        # I Instructions Type
        'addi': iInstructions.addi,
        
        # U Instructions Type
        # '',
        
        # R Instructiosn Type
        'add': rInstructions.add,
    }