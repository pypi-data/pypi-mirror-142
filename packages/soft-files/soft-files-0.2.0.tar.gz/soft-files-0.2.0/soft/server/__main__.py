import socket
from threading import Thread
from . import safe, _userops
from configparser import ConfigParser
import os
import nacl.utils
import nacl.secret
import nacl.exceptions
from loguru import logger

default_directory_prompt = "C:\\" if os.name == "nt" else "/"

def recvall(sock):
    data = b""
    while True:
        part = sock.recv(4096)
        data += part
        if len(part) < 4096:
            break
    return data

def first_time_config():
    host = input("Host IP [0.0.0.0]: ")
    if host == "":
        host = "0.0.0.0"
    port = input("Port [2022]: ")
    if port == "":
        port = 2022
    else:
        port = int(port)
    directory = input(f"Default Server Directory [{default_directory_prompt}]: ")
    if directory == "":
        directory = "/"
    key = nacl.utils.random(nacl.secret.SecretBox.KEY_SIZE).hex()
    conf["general"] = {"host": host, "port": port, "secret_key": key, "directory": "/"}
    print(f"Your secret key can be found in {appdata}{SEPARATOR}server.ini. Only share it with people you trust!\n")
    with open(f"{appdata}{SEPARATOR}server.ini", "w") as f:
        conf.write(f)
    username = _userops.get_username()
    _userops.get_password(username)
    choice = input("Would you like to create more users? [y/n]: ")
    if choice == "y":
        print("Leave name blank to quit.")
        while True:
            name = _userops.get_username_not_mandatory()
            if name == None:
                break
            _userops.get_password(name)
    print("Done first time configuration! Starting server.")

COMMANDS = ["get", "ls", "dir", "pwd", "cd", "put"]

SEPARATOR = "/" if os.name != "nt" else "\\"

appdata = f"{os.getenv('PROGRAMDATA')}\\soft" if os.name == 'nt' else "/opt/soft"

conf = ConfigParser()

def on_connection(conn, addr):
    directory = conf["general"]["directory"]
    logger.info(f"New connection from {addr[0]}")
    user_safe = safe.Safe(conf["general"]["secret_key"])
    while True:
        uinfo = recvall(conn)
        try:
            uinfo = user_safe.decrypt_userinfo(uinfo)
        except nacl.exceptions.ValueError:
            logger.info(f"Connection {addr[0]} terminated by client.")
            return
        exists = _userops.check_if_user_exists(uinfo[0])
        if not exists:
            conn.sendall(user_safe.encrypt_userinfo_resp(exists))
            continue
        else:
            password = _userops.pull_password(uinfo[0])
            if password != uinfo[1]:
                conn.sendall(user_safe.encrypt_userinfo_resp(False))
                continue
            else:
                conn.sendall(user_safe.encrypt_userinfo_resp(True))
        break
    while True:
        try:
            command = recvall(conn)
            command = user_safe.decrypt_cmd(command)
        except nacl.exceptions.ValueError:
            logger.info(f"Connection from {addr[0]} terminated by client.")
            break
        except nacl.exceptions.CryptoError:
            logger.info(f"Verification failed from {addr[0]}.")
            conn.sendall(user_safe.encrypt_cmd_resp("Verification failed."))
            continue
        if command[0] == "pwd":
            conn.sendall(user_safe.encrypt_cmd_resp(directory))
        elif command[0] == "cd":
            old_dir = directory
            if SEPARATOR == "/":
                command[1].replace("\\", "/")
            else:
                command[1].replace("/", "\\")
            if command[1][0] == SEPARATOR:
                directory = command[1]
            else:
                if directory == SEPARATOR:
                    directory += command[1] 
                else:
                    directory += SEPARATOR + command[1]
            if os.path.exists(directory):
                if os.path.isdir(directory):
                    conn.sendall(user_safe.encrypt_cmd_resp(f"Directory changed to {directory}"))
                else:
                    conn.sendall(user_safe.encrypt_cmd_resp(f"{directory} is not a directory"))
                    directory = old_dir
            else:
                conn.sendall(user_safe.encrypt_cmd_resp(f"{directory} does not exist"))
                directory = old_dir
        elif command[0] == "ls":
            files = ' '.join(os.listdir(directory))
            conn.sendall(user_safe.encrypt_cmd_resp(files))
        elif command[0] == "dir":
            files = ' '.join(os.listdir(directory))
            conn.sendall(user_safe.encrypt_cmd_resp(files))
        elif command[0] == "put":
            data = bytes.fromhex(command[2])
            with open(f"{directory}{SEPARATOR}{command[1]}", "wb") as f:
                f.write(data)
            conn.sendall(user_safe.encrypt_cmd_resp(f"{command[1]} uploaded successfully"))
        elif command[0] == "get":
            if os.path.exists(f"{directory}{SEPARATOR}{command[1]}"):
                if not os.path.isdir(f"{directory}{SEPARATOR}{command[1]}"):
                    with open(f"{directory}{SEPARATOR}{command[1]}", "rb") as f:
                        data = f.read()
                    conn.sendall(user_safe.encrypt_cmd_resp(f"{command[1]}, {data.hex()}"))
            else:
                conn.sendall(user_safe.encrypt_cmd_resp(f"{command[1]} does not exist"))
    del conn
    


conf.read(f"{appdata}{SEPARATOR}server.ini")
if len(conf.sections()) == 0:
    first_time_config()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((conf["general"]["host"], int(conf["general"]["port"])))
server.listen(5)
while True:
    conn, addr = server.accept()
    Thread(target=on_connection, args=(conn, addr)).start()
