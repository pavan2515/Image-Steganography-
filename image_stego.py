from PIL import Image
from crypto_utils import encrypt_AES, decrypt_AES

def to_bin(data):
    return ''.join(format(ord(i), '08b') for i in data)

def encode_image(image_path, message, key, output_path):
    encrypted = encrypt_AES(key, message)
    binary_data = to_bin(encrypted) + '1111111111111110'
    img = Image.open(image_path).convert('RGB')
    pixels = list(img.getdata())

    new_pixels = []
    data_index = 0

    for pixel in pixels:
        pixel = list(pixel)
        for i in range(3):  # RGB
            if data_index < len(binary_data):
                pixel[i] = (pixel[i] & ~1) | int(binary_data[data_index])
                data_index += 1
        new_pixels.append(tuple(pixel))

    img.putdata(new_pixels)
    img.save(output_path)
    print("Encrypted data embedded into image!")

def decode_image(image_path, key):
    img = Image.open(image_path)
    binary_data = ''
    for pixel in img.getdata():
        for i in range(3):
            binary_data += str(pixel[i] & 1)

    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    encrypted = ''
    for byte in all_bytes:
        if byte == '11111110': break
        encrypted += chr(int(byte, 2))

    return decrypt_AES(key, encrypted)