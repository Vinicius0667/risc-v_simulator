from Memory import Memory                                                   # Importa a classe Memory para gerenciamento de dados
from Register import Register                                               # Importa a classe Register para manipular os registradores
from IInstructions import IInstructions                                     # Importa as implementações de instruções do tipo I
from UInstructions import UInstructions                                     # Importa as implementações de instruções do tipo U
from RInstructions import RInstructions                                     # Importa as implementações de instruções do tipo R

def setup():
    register = Register()                                                   # Instancia o banco de registradores
    memory: Memory = Memory()                                               # Instancia a memória principal do simulador

    iInstructions = IInstructions(register, memory)                         # Injeta registradores e memória nas instruções tipo I
    uInstructions = UInstructions(register)                                 # Injeta registradores nas instruções tipo U
    rInstructions = RInstructions(register)                                 # Injeta registradores nas instruções tipo R

    return register, {                                                      # Retorna o banco de registradores e o mapa de comandos
        # I Instructions Type
        'addi'  : iInstructions.addi,                                       # Mapeia a string 'addi' para o método correspondente
        'xori': iInstructions.xori,                                         # Mapeia a operação lógica XOR imediata
        'ori': iInstructions.ori,                                           # Mapeia a operação lógica OR imediata
        'andi': iInstructions.andi,                                         # Mapeia a operação lógica AND imediata
        'slli': iInstructions.slli,                                         # Mapeia o shift lógico para a esquerda imediato
        'srli': iInstructions.srli,                                         # Mapeia o shift lógico para a direita imediato
        'srai': iInstructions.srai,                                         # Mapeia o shift aritmético para a direita imediato
        'slti': iInstructions.slti,                                         # Mapeia a comparação "set less than" imediata
        'sltiu': iInstructions.sltiu,                                       # Mapeia a comparação "set less than" imediata sem sinal
        'lb': iInstructions.lb,                                             # Mapeia o carregamento de byte da memória
        'lh': iInstructions.lh,                                             # Mapeia o carregamento de half-word da memória
        'lw': iInstructions.lw,                                             # Mapeia o carregamento de word da memória
        'lbu': iInstructions.lbu,                                           # Mapeia o carregamento de byte sem sinal
        'lhu': iInstructions.lhu,                                           # Mapeia o carregamento de half-word sem sinal
        'jalr': iInstructions.jalr,                                         # Mapeia o desvio indireto com link
        'ecall': iInstructions.ecall,                                       # Mapeia a chamada de sistema
        'ebreak': iInstructions.ebreak,                                     # Mapeia a interrupção de breakpoint

        # U Instructions Type
        'lui'   : uInstructions.lui,                                        # Mapeia o carregamento de valor imediato superior
        'auipc' : uInstructions.auipc,                                      # Mapeia a soma de imediato superior ao PC

        # R Instructiosn Type
        'add'   : rInstructions.add,                                        # Mapeia a soma entre registradores
        'sub'   : rInstructions.sub,                                        # Mapeia a subtração entre registradores
        'xor'   : rInstructions.xor,                                        # Mapeia o XOR entre registradores
        'or'    : rInstructions.orR,                                        # Mapeia o OR entre registradores
        'and'   : rInstructions.andR,                                       # Mapeia o AND entre registradores
        'sll'   : rInstructions.sll,                                        # Mapeia o shift lógico à esquerda entre registradores
        'srl'   : rInstructions.srl,                                        # Mapeia o shift lógico à direita entre registradores
        'sra'   : rInstructions.sra,                                        # Mapeia o shift aritmético à direita entre registradores
        'slt'   : rInstructions.slt,                                        # Mapeia a comparação entre registradores
        'sltu'  : rInstructions.sltu,                                       # Mapeia a comparação sem sinal entre registradores
    }
