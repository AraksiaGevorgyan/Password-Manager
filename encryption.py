from cryptography.fernet import Fernet

class Encryption:

    def __init__(self):
        self.key = self.generate_key()
        self.cipher_suite = Fernet(self.key)

    def generate_key(self):
        return Fernet.generate_key()

    def encrypt_password(self, password):
        encrypted_password = self.cipher_suite.encrypt(password.encode())
        return encrypted_password

    def decrypt_password(self, encrypted_password):
        decrypted_password = self.cipher_suite.decrypt(encrypted_password).decode()
        return decrypted_password
