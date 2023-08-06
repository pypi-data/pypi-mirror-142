import socket
import os
from .safe import Safe
from . import _userops as uo
import nacl.exceptions
import time

def recvall(sock):
    data = b""
    while True:
        part = sock.recv(4096)
        data += part
        if len(part) < 4096:
            break
    return data

SEPARATOR = "/" if os.name != "nt" else "\\"

host = input("Server Host [0.0.0.0]: ")
if host == "":
    host = "0.0.0.0"

commands = {
    "ls": "Lists all files in the current server directory", 
    "dir": "Lists all files in the current server directory", 
    "pwd": "Prints the current server directory", 
    "cd": "Changes server directory", 
    "put": "Puts a file from your local machine onto the server", 
    "get": "Puts a file on the server onto your local machine", 
    "lcd": "Changes local machine directory", 
    "ldir": "Lists all files in the current local directory", 
    "lpwd": "Prints the current local directory",
    "quit": "Exits the program",
    "help": "Prints this help message"
}


port = input("Server Port [2022]: ")
if port == "":
    port = 2022
else:
    port = int(port)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.connect((host, port))

def get_key():
    key = input("Encryption Key: ")
    if key == "":
        print("Key cannot be empty!")
        get_key()
    return key

key = get_key()

safe = Safe(key)

try:
    uo.login(safe, s)
except ConnectionResetError:
    print("Connection was terminated by the server.")
    exit()

print("Type help for a list of commands.")

while True:
    command = input("soft> ")
    if command == "help":
        for c in commands:
            print(f"{c}: {commands[c]}")
        continue
    elif command == "quit":
        s.close()
        print("Exiting...")
        exit()
    elif command == "lpwd":
        print(os.getcwd())
        continue
    elif "lcd" in command:
        try:
            os.chdir(" ".join(command.split(" ")[1:]))
            print(f"Local Directory changed to {os.getcwd()}")
        except FileNotFoundError:
            print("Directory does not exist!")
        except IndexError:
            print("Directory cannot be empty!")
        continue
    elif command == "ldir":
        print(" ".join(os.listdir()))
        continue
    if command.split(" ")[0] not in commands:
        print("Command not found. Type help for a list of commands.")
        continue
    command = command.split(" ")
    if command[0] == "put":
        try:
            with open(f"{os.getcwd()}{SEPARATOR}{' '.join(command[1:])}", "rb") as f:
                data = f.read()
                data = data.hex()
            args = command[1:]
            args[0] = " ".join(args[0:])
            del args[1:]
            args.append(data)
            stamp = time.time() * 1000
            s.sendall(safe.encrypt_cmd(command[0], args))
            try:
                resp = safe.decrypt_cmd_resp(recvall(s))
            except nacl.exceptions.CryptoError:
                print("Server and client are out of sync, exiting...")
                exit()
            print(resp)
            print(f"Time taken: {time.time() * 1000 - stamp}ms")
            continue
        except FileNotFoundError:
            print("File does not exist!")
            continue
    elif command[0] == "get":
        command[1] = " ".join(command[1:])
        del command[2:]
        stamp = time.time() * 1000
        s.sendall(safe.encrypt_cmd(command[0], command[1:]))
        try:
            resp = recvall(s)
            resp = safe.decrypt_cmd_resp(resp)
            resp = resp.split(", ")
            if len(resp) == 1:
                print(resp[0])
                continue
            with open(f"{os.getcwd()}{SEPARATOR}{resp[0]}", "wb") as f:
                f.write(bytes.fromhex(resp[1]))
            print(f"File {resp[0]} was successfully downloaded.")
            print(f"Time taken: {time.time() * 1000 - stamp}ms")
            continue
        except nacl.exceptions.CryptoError:
            print("Server and client are out of sync, exiting...")
            exit()
    if len(command) == 1:
        s.sendall(safe.encrypt_cmd(command[0]))
        try:
            resp = safe.decrypt_cmd_resp(recvall(s))
        except ConnectionResetError:
            print("Connection was terminated by the server.")
            exit()
        print(resp)
        continue
    else:
        s.sendall(safe.encrypt_cmd(command[0], command[1:]))
        try:
            resp = safe.decrypt_cmd_resp(recvall(s))
        except ConnectionResetError:
            print("Connection was terminated by the server.")
            exit()
        print(resp)
        continue







