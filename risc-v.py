import sys

from Register import Register

SUPPORTED_COMMANDS = ['add', 'addi', 'sub', 'lui', 'lw', 'sw']

def main():
    register = Register()
    file_path = sys.argv[1]

    try:
        with open (file_path, 'r') as file:
            for pc, line in enumerate(file):
                instruction = line.strip()

                if not instruction or instruction.startswith('#'):
                    continue

                commandPieces = instruction.replace(',', ' ').split()
                command = commandPieces[0]

                if command not in SUPPORTED_COMMANDS:
                    print(f"Error, command: {command} not found, in line {pc}")
                    sys.exit(1)
                if command == 'addi':
                    register.write(commandPieces[1], commandPieces[2])
    except FileNotFoundError:
        print(f"Error: File {file_path} not found!")

    print(register.read('x5'))

if __name__ == "__main__":
    main()
