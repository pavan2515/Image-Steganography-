import wave
import numpy as np
from crypto_utils import encrypt_AES, decrypt_AES

def encode_audio(audio_path, message, key, output_path):
    encrypted = encrypt_AES(key, message)
    binary_data = ''.join(format(ord(i), '08b') for i in encrypted) + '1111111111111110'

    with wave.open(audio_path, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))
    
    for i in range(len(binary_data)):
        frames[i] = (frames[i] & ~1) | int(binary_data[i])

    with wave.open(output_path, 'wb') as stego:
        stego.setparams(audio.getparams())
        stego.writeframes(frames)
    print("Data embedded in audio!")

def decode_audio(audio_path, key):
    with wave.open(audio_path, 'rb') as audio:
        frames = bytearray(list(audio.readframes(audio.getnframes())))

    binary_data = ''
    for byte in frames:
        binary_data += str(byte & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    encrypted = ''
    for byte in all_bytes:
        if byte == '11111110': break
        encrypted += chr(int(byte, 2))

    return decrypt_AES(key, encrypted)