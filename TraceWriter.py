class TraceWriter:
    def __init__(self, file_path):
        self.file_path = file_path                                          # Define o caminho do arquivo de saída
        self.lines = []                                                     # Inicializa a lista que armazenará os logs das instruções

    def add_line(self, instruction):
        formatted_line = f"{instruction}"                                   # Formata a string da instrução executada
        self.lines.append(formatted_line)                                   # Adiciona o resultado da execução à lista de rastreio

    def write(self):
        try:
            with open(self.file_path, "w") as output_file:                  # Abre o arquivo de destino para escrita
                output_file.write("".join(self.lines))                      # Concatena todas as linhas e grava no arquivo de uma vez
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found!")               # Exibe erro caso o diretório ou arquivo não sejam acessíveis