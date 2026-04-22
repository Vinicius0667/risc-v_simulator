import sys

from instruction_map import setup                                           #importa a função Instructionsetup da classe instruction_map
from TraceWriter import TraceWriter                                         #importa a classe TraceWriter do arquivo TraceWriter

def main():
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"     # caso o aplicativo seja iniciado pela linha de comando o arquivo de entrada é o primeiro argumento passado, se não ele assume o valor padrão de input.txt
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else "output.txt"   # caso o aplicativo seja iniciado pela linha de comando o arquivo de saida é o segundo argumento passado, se não ele assume o valor padrão de output.txt

    register, commands = setup()                                            #cria os dicionarios para funções register e commands(no qual as funções são referenciadas por strings)
    traceWriter = TraceWriter(output_file_path)

    try:                                                                    #tenta abrir o arquivo input_file_path se der certo prossegue, se não printa a menssagem de erro de arquivo não encontrado
        with open(input_file_path, "r") as input_file:                      #abre o arquivo input_file_path como leitura, caso ocorram erros no meio da função em sseguida ou simplesemente ela seja encerrada ele automaticamente fecha o arquivo
            for pc, line in enumerate(input_file):                          #cria a variavel PC(program counter que controla onde se encontra a proxima instrução) ele é incrementado em 1 a cada 'intrução'(linha) e a variavel line que recebe a linha atual          
                instruction = line.strip()                                  #retira espaços da frente e no final da linha           

                if not instruction or instruction.startswith("#"):          #se a linha estiver vazia ou a instrução começar com # deve ignorar pois é um comentario ou linha vazia
                    continue

                command, *args = instruction.replace(",", " ").split()      #salva a primeira frase/comando na variavel command e as outras frases na lista args

                if command == 'auipc':                                      #caso a função a ser chamada é auipc ele envia pc como um argumento
                    args[1] = pc

                if command in commands:                                     #verifica se command se encontra na lista commands
                    output = commands[command](args)                        #salva a saida das funções rodadas utilizando command para procurar as funções guardadas em commands utilizando args como os argumentos
                    traceWriter.add_line(output)                            #salva a saida das funções executadas anteriormente para o arquivo de saida
                else:
                    traceWriter.add_line("Unknown Instruction")             #caso a função anterior não exista no dicionario de comandos é escrito que a instrução é invalida no arquivo de saida
                    break

    except FileNotFoundError:
        print(f"Error: File {input_file_path} not found!")

    traceWriter.write()                                                     #escreve definitivamente para o arquivo de saida

if __name__ == "__main__":
    main()
