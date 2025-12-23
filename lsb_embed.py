import numpy as np

def embed_lsb(image, bitstream):
    flat = image.flatten()
    for i in range(len(bitstream)):
        flat[i] = (flat[i] & 0xFE) | int(bitstream[i])
    return flat.reshape(image.shape)

def extract_lsb(stego_img, length):
    flat = stego_img.flatten()
    bits = [str(flat[i] & 1) for i in range(length)]
    return ''.join(bits)
