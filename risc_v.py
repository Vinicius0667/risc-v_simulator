import sys

from instruction_map import setup
from TraceWriter import TraceWriter

def main():
    input_file_path = sys.argv[1] if len(sys.argv) > 1 else "input.txt"
    output_file_path = sys.argv[2] if len(sys.argv) > 2 else "output.txt"

    register, commands = setup()
    traceWriter = TraceWriter(output_file_path)

    try:
        with open(input_file_path, "r") as input_file:
            for pc, line in enumerate(input_file):
                instruction = line.strip()

                if not instruction or instruction.startswith("#"):
                    continue

                command, *args = instruction.replace(",", " ").split()

                if command in commands:
                    output = commands[command](args)
                    traceWriter.add_line(output)
                else:
                    traceWriter.add_line("Unknown Instruction")
                    break
    except FileNotFoundError:
        print(f"Error: File {input_file_path} not found!")

    traceWriter.write()

if __name__ == "__main__":
    main()
