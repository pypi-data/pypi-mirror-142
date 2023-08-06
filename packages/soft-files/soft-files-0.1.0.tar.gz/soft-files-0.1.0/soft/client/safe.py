import nacl.secret
import nacl.utils

class Safe:
    def __init__(self, key: str):
        self.key = bytes.fromhex(key)
        self.box = nacl.secret.SecretBox(self.key)

    def encrypt_userinfo(self, userinfo: list) -> bytes:
        return self.box.encrypt(f"{userinfo[0]}, {userinfo[1]}".encode())

    def decrypt_userinfo_resp(self, encrypted_data: bytes) -> bool:
        return bool(self.box.decrypt(encrypted_data))

    def encrypt_cmd(self, command: str, args: list = None) -> bytes:
        if command == "pwd":
            return self.box.encrypt(command.encode())
        elif command == "cd":
            return self.box.encrypt(f"{command}, {' '.join(args)}".encode())
        elif command == "ls":
            return self.box.encrypt(command.encode())
        elif command == "dir":
            return self.box.encrypt(command.encode())
        elif command == "put":
            print(args[0])
            return self.box.encrypt(f"{command}, {args[0]}".encode() + b", " + args[1].encode())
        elif command == "get":
            return self.box.encrypt(f"{command}, {args[0]}".encode())

    def decrypt_cmd_resp(self, encrypted: bytes) -> str:
        return self.box.decrypt(encrypted).decode()