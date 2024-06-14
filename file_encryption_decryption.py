from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("secret.key", "wb") as key_file:
        key_file.write(key)

def load_key():
    return open("secret.key", "rb").read()

def encrypt_message(message, key):
    encoded_message = message.encode()
    f = Fernet(key)
    encrypt_message = f.encrypt(encoded_message)
    return encrypt_message

def decrypt_message(encrypt_message, key):
    f = Fernet(key)
    decrypt_message = f.decrypt(encrypt_message)
    return decrypt_message.decode()

generate_key()
key = load_key()

encrypted = encrypt_message("Senwin please fix minthara in BG3", key)
print("Encrypted: " + encrypted.decode())

decrypted = decrypt_message(encrypted, key)
print("Decrypted: " + decrypted)