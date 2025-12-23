# Image-Steganography-
A secure Python-based multimedia steganography system that hides AES-encrypted text inside image, audio, and video files using LSB techniques. Supports image, audio, and video steganography with modular design and future extensibility.

# 🔐 Secure Multimedia Steganography System

A Python-based secure steganography project that hides **AES-encrypted text data** inside **Image, Audio, and Video files** using the **Least Significant Bit (LSB)** technique.

This project demonstrates how sensitive information can be securely concealed within multimedia files without visibly altering them.

---

## ✨ Features

- 🔒 AES encryption for strong data security  
- 🖼️ Image steganography using RGB pixel LSBs  
- 🔊 Audio steganography using WAV frame LSBs  
- 🎥 Video steganography using frame-wise LSB embedding  
- 🧩 Modular and well-structured codebase  
- 📦 Optional Shannon–Fano compression support  
- 🚀 Suitable for academic, research, and security applications  

---

## 📁 Project Structure

```

.
├── main.py              # Main execution file
├── image_stego.py       # Image steganography (LSB + AES)
├── audio_stego.py       # Audio steganography (LSB + AES)
├── video_stego.py       # Video steganography (LSB + AES)
├── shannon_fano.py      # Shannon–Fano text compression (optional)
├── lsb_embed.py         # Generic LSB helper functions
├── crypto_utils.py      # AES encryption and decryption utilities
├── cover.png            # Sample image file
├── cover.wav            # Sample audio file
├── cover.avi            # Sample video file
└── README.md

````

---

## 🔧 Requirements

Install required Python packages:

```bash
pip install numpy opencv-python pillow
````

(Modules like `wave` are part of Python’s standard library.)

---

## ▶️ How to Run

Run the main program:

```bash
python main.py
```

You will be prompted to enter a secret message.
The system will:

1. Encrypt the message using AES
2. Embed it into image, audio, and video files
3. Extract and decrypt the hidden message for verification

---

## 🔐 Security Workflow

```
Plain Text
   ↓
AES Encryption
   ↓
Binary Conversion
   ↓
LSB Embedding (Image / Audio / Video)
   ↓
Stego Media
   ↓
LSB Extraction
   ↓
AES Decryption
```

---

## 🧠 Techniques Used

| Component           | Technique               |
| ------------------- | ----------------------- |
| Encryption          | AES                     |
| Image Steganography | LSB (RGB pixels)        |
| Audio Steganography | LSB (Audio frames)      |
| Video Steganography | LSB (Video frames)      |
| Compression         | Shannon–Fano (optional) |

---

## ⚠️ Limitations

* LSB technique is sensitive to compression
* Shannon–Fano compression is not yet integrated into the main pipeline
* Input and output files may overwrite existing files
* No image quality metrics (PSNR/SSIM) included

---

## 🚀 Future Enhancements

* Integrate Shannon–Fano compression before encryption
* Implement DWT/DCT-based steganography
* Add PSNR and SSIM evaluation metrics
* Develop a Flask-based web interface
* Extend support to medical images (DICOM)

---

## 📜 License

This project is intended for **educational and research purposes**.
Free to use, modify, and extend.

---

## 👨‍💻 Author

**Pavan K**
Electronics & Communication Engineering
Embedded Systems | AI | Secure Multimedia Processing

```

