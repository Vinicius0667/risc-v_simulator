# Registro de colaboração da IA, utilizei o Gemini

Segue a baixo os arquivos afetados:

## risc_v.py
### linhas afetadas [23 - 24]
O Gemini me ajudou a ajustar a lógica de argumentos do jalr, permitindo que o Program Counter fosse passado corretamente para a função de modo que o endereço de retorno (PC + 4) pudesse ser calculado e armazenado.

## instructions_map.py
### linhas afetadas [10 - 30]
O Gemini me ajudou a estruturar a injeção de dependência da classe Memory dentro da inicialização das IInstructions, garantindo que todas as instruções de Load tivessem acesso ao mesmo objeto de memória. Além disso, ele me orientou no mapeamento completo de todas as novas funções implementadas (como as de Load, deslocamento e comparação) para que o simulador pudesse reconhecê-las a partir das strings lidas do arquivo de entrada.

## Memory.py
### linhas afetadas [1 - 29]
O Gemini me ajudou a projetar esta classe do zero para simular a memória RAM do RISC-V de forma eficiente. Ele sugeriu o uso de um dicionário para representar o endereçamento de 32 bits sem consumir RAM desnecessária e implementou a lógica de Little Endian para leitura e escrita de bytes, half-words e words, o que é essencial para que o simulador processe os dados exatamente como o hardware real.

## IInstructions.py
### linhas afetadas [1 - 167]
O Gemini me ajudou a implementar o conjunto completo de instruções de tipo I, incluindo as operações aritméticas, lógicas, de deslocamento e de carregamento de memória. Ele foi essencial para garantir que a extensão de sinal funcionasse corretamente no Python (que usa inteiros de precisão arbitrária) para simular o comportamento de 32 bits, além de estruturar a lógica complexa do jalr e das instruções de Load que interagem com a classe Memory.

## Register.py
### linhas afetadas [15 - 18]
O Gemini me ajudou a refinar a lógica de proteção do registrador x0, garantindo que qualquer tentativa de escrita no registrador zero seja ignorada, respeitando a arquitetura RISC-V. Além disso, ele auxiliou na estruturação dos métodos de leitura e escrita para que aceitassem tanto os nomes reais (x0-x31) quanto os nomes da ABI (zero, ra, sp, etc.), tornando o simulador mais amigável para o programador.

## TraceWriter.py
### linhas afetadas [9 - 14]
O Gemini me ajudou a otimizar a forma como os resultados são gravados no arquivo. Em vez de abrir o arquivo a cada instrução (o que seria lento), ele sugeriu armazenar tudo em uma lista interna e realizar uma única operação de escrita ao final da execução do simulador, utilizando o método join para garantir eficiência e performance.

## test_risc_v.py
### linhas afetadas [1 - 47]
O Gemini me ajudou a criar um teste de integração completo que valida o fluxo inteiro do simulador, desde a leitura do arquivo até a escrita do resultado final. Ele sugeriu o uso de unittest.mock.patch para simular os argumentos de linha de comando (sys.argv) sem precisar rodar o script manualmente, e implementou a lógica de setUp e tearDown para criar e apagar arquivos de teste automaticamente, garantindo que os testes sejam limpos e repetíveis.

## test_i_instructions.py
### linhas afetadas [1 - 205]
O Gemini me ajudou a construir uma bateria de testes exaustiva para todas as instruções do tipo I. Ele sugeriu casos de teste específicos para validar a extensão de sinal em operações negativas (como em addi, lb e l) e a diferença entre operações lógicas e aritméticas (como srli e srai). Também colaborou na criação de mocks para simular a interação entre registradores e memória, garantindo que o jalr salvasse corretamente o endereço de retorno e que os deslocamentos de bits respeitassem o limite de 32 bits da arquitetura.

## test_register.py
### linhas afetadas [1 - 36]
O Gemini me ajudou a estruturar os testes unitários para o banco de registradores, focando na validação do mapeamento da ABI. Ele sugeriu casos de teste para garantir que múltiplos nomes (como fp, s0 e x8) apontassem para o mesmo endereço de memória e foi fundamental para validar a regra de imutabilidade do registrador zero, garantindo que o simulador nunca permita a alteração do valor constante 0.

