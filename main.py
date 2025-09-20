import getpass
import socket
import commands


username = getpass.getuser()
hostname = socket.gethostname()

if __name__ == "__main__":
    while True:
        print(f"{username}@{hostname}: ", end="")
        prompt = input()
        line = prompt.split()
        command = commands.get_command(line[0])
        if command != None:
            print(command(*line))
        else:
            print(f"Unknown command: {line[0]}")
        
    