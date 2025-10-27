from cryptography.fernet import Fernet
import os
from models import SessionLocal, FileMeta

key = Fernet.generate_key()
cipher = Fernet(key)

def encrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    encrypted = cipher.encrypt(data)
    enc_file = file_path + ".enc"
    with open(enc_file, 'wb') as f:
        f.write(encrypted)
    print(f"File {file_path} encrypted as {enc_file}.")
    return enc_file

def decrypt_file(file_path):
    with open(file_path, 'rb') as f:
        data = f.read()
    decrypted = cipher.decrypt(data)
    dec_file = file_path.replace(".enc", "")
    with open(dec_file, 'wb') as f:
        f.write(decrypted)
    print(f"File {file_path} decrypted as {dec_file}.")
    return dec_file

def save_metadata(filename, owner):
    db = SessionLocal()
    new_file = FileMeta(filename=filename, owner=owner)
    db.add(new_file)
    db.commit()
    db.close()
    print(f"Metadata for {filename} saved in database.")
