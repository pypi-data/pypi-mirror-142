import nacl.secret
import nacl.utils

class Safe:
    def __init__(self, key: str):
        self.key = bytes.fromhex(key)
        self.box = nacl.secret.SecretBox(self.key)

    def decrypt_userinfo(self, encrypted: bytes) -> list:
        return self.box.decrypt(encrypted).decode().split(", ")

    def encrypt_userinfo_resp(self, resp: bool) -> bytes:
        return self.box.encrypt(bytes(resp))

    def encrypt_cmd_resp(self, resp: str) -> bytes:
        return self.box.encrypt(resp.encode())

    def decrypt_cmd(self, encrypted: bytes) -> str:
        return self.box.decrypt(encrypted).decode().split(", ")