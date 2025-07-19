# Text-Encryption

This is a **GUI-based encryption and decryption tool** built with **Python**.  
The application allows users to **secure text data** using **AES, DES, and RSA** encryption algorithms, with a simple **Tkinter-based interface**.

---

## 📌 Features
- **AES & DES Encryption/Decryption**  
  - Uses a **passkey** for secure encryption  
  - Automatically handles **IV (Initialization Vector)**  
- **RSA Encryption/Decryption**  
  - Generates a new **key pair** automatically  
  - Simplifies asymmetric encryption  
- **User-Friendly GUI**  
  - Built using Tkinter  
  - Interactive fields for text, IV, passkey, and results  
- **Error Handling**  
  - Guides the user with popups for invalid inputs

---

## 🛠️ Technologies Used
- **Python**
- **Tkinter** (for GUI)
- **PyCryptodome** (for AES, DES, RSA, SHA256 cryptography)
- **Base64 encoding** (for readable key, IV, and ciphertext)

---

## 📥 Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/imvinxx/Text-Encryption.git

2. Install dependencies:
   ```bash
   pip install pycryptodome

3. Run the Program:
   ```bash
   python TextEncryption.py

---

## 🖥️ How to Use

1. Launch the application:
   ```bash
   python TextEncryption.py

2. To Encrypt:
  -Enter the text you want to encrypt.
  -Select AES, DES, or RSA.
  -For AES/DES, enter a passkey.
  -Click Encrypt to generate:
    -Encrypted text
    -IV (for AES/DES)
  -Copy these values if you want to decrypt later.

3. To Decrypt:
  -Paste the IV, ciphertext, and the same passkey (for AES/DES).
  -Select the algorithm used.
  -Click Decrypt to reveal the original text.

---

## 📸 Screenshot (Sample UI)
  ```bash
  GUI_ScreenShot.png

---


