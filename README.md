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
   git clone https://github.com/your-username/python-encryption-tool.git
   cd python-encryption-tool
