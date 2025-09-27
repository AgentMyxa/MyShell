import getpass
import socket
import sys
import commands


username = getpass.getuser()
hostname = socket.gethostname()


def _print_config() -> None:
    print("Config")
    print(f"Start script: {sys.argv[0]}")
    print(f"VFS: {sys.argv[1]}")


if __name__ == "__main__":
    _print_config()
    while True:
        print(f"{username}@{hostname}: ", end="")
        prompt = input()
        line = prompt.split()
        command = commands.get_command(line[0])
        if command != None:
            print(command(*line))
        else:
            print(f"Unknown command: {line[0]}")
        
    