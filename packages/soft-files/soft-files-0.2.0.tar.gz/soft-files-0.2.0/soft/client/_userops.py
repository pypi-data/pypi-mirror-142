from .safe import Safe
import socket

def get_userinfo():
    username = input("Username: ")
    if username == "":
        print("Username cannot be empty!")
        get_userinfo()
    password = input("Password: ")
    if password == "":
        print("Password cannot be empty!")
        get_userinfo()
    return [username, password]

def login(safe: Safe, server: socket.socket):
    while True:
        uinfo = get_userinfo()
        uinfo = safe.encrypt_userinfo(uinfo)
        server.sendall(uinfo)
        resp = safe.decrypt_userinfo_resp(server.recv(1024))
        if not resp:
            print("Username or password is incorrect!")
            continue
        else:
            print("Login successful!")
            break
    return
