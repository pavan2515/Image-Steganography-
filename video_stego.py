import cv2
import numpy as np
from crypto_utils import encrypt_AES, decrypt_AES

def to_bin(data):
    return ''.join(format(ord(i), '08b') for i in data)

def encode_video(video_path, message, key, output_path):
    encrypted = encrypt_AES(key, message)
    data = to_bin(encrypted) + '1111111111111110'  # End marker: 16 bits

    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[!] Error opening video file: {video_path}")
        return

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # Capacity Check
    capacity_bits = total_frames * width * height * 3
    print(f"[i] Data to embed: {len(data)} bits ≈ {len(data)//8} bytes")

    if len(data) > capacity_bits:
        cap.release()
        out.release()
        return

    data_index = 0
    success, frame = cap.read()

    while success:
        flat = frame.flatten().astype(np.uint8)

        for i in range(len(flat)):
            if data_index < len(data):
                flat[i] = (flat[i] & 0xFE) | int(data[data_index])
                data_index += 1

        frame = np.clip(flat.reshape(frame.shape), 0, 255).astype(np.uint8)
        out.write(frame)
        success, frame = cap.read()

    cap.release()
    out.release()
    print("[✓] Encrypted data embedded into video!")

def decode_video(video_path, key):
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"[!] Error opening video file: {video_path}")
        return ""

    binary_data = ''
    success, frame = cap.read()

    while success:
        flat = frame.flatten()
        for value in flat:
            binary_data += str(value & 1)
        success, frame = cap.read()

    cap.release()
    print(f"[i] Total bits extracted: {len(binary_data)}")

    # Convert bits to characters until stop marker
    all_bytes = [binary_data[i:i+8] for i in range(0, len(binary_data), 8)]
    encrypted = ''
    for byte in all_bytes:
        if byte == '11111110':  # End marker (8 bits)
            break
        try:
            encrypted += chr(int(byte, 2))
        except:
            continue

    if not encrypted:
        print("[!] No encrypted data found in video.")
        return ""

    print(f"[i] Encrypted text: {encrypted[:50]}...")
    try:
        return decrypt_AES(key, encrypted)
    except Exception as e:
        print(f"[!] Decryption failed: {e}")
        return ""