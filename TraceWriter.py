class TraceWriter:
    def __init__(self, file_path):
        self.file_path = file_path
        self.lines = []

    def add_line(self, instruction):
        formatted_line = f"{instruction}"
        self.lines.append(formatted_line)

    def write(self):
        try:
            with open(self.file_path, "w") as output_file:
                output_file.write("".join(self.lines))
        except FileNotFoundError:
            print(f"Error: File {self.file_path} not found!")
