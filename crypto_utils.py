from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    return data + (16 - len(data) % 16) * chr(16 - len(data) % 16)

def unpad(data):
    return data[:-ord(data[-1])]

def encrypt_AES(key, plaintext):
    key = key[:16].encode('utf-8')
    key = (key + b'0'*16)[:16] # 16-byte key
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plaintext)
    encrypted = cipher.encrypt(padded.encode('utf-8'))
    return base64.b64encode(encrypted).decode('utf-8')

def decrypt_AES(key, ciphertext):
    key = key[:16].encode('utf-8')
    key = (key + b'0'*16)[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    decrypted = cipher.decrypt(base64.b64decode(ciphertext.encode('utf-8')))
    return unpad(decrypted.decode('utf-8'))