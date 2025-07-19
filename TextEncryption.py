import tkinter as tk
from tkinter import ttk, messagebox
from Crypto.Cipher import AES, DES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Hash import SHA256
from Crypto.Random import get_random_bytes
import base64

# Key derivation
def derive_key(passkey, length):
    hashed = SHA256.new(passkey.encode()).digest()
    return hashed[:length]

# AES
def aes_encrypt(text, passkey):
    key = derive_key(passkey, 16)
    cipher = AES.new(key, AES.MODE_CBC)
    ct = cipher.encrypt(pad(text.encode(), AES.block_size))
    return base64.b64encode(cipher.iv).decode(), base64.b64encode(ct).decode()

def aes_decrypt(iv, ct, passkey):
    key = derive_key(passkey, 16)
    cipher = AES.new(key, AES.MODE_CBC, base64.b64decode(iv))
    pt = unpad(cipher.decrypt(base64.b64decode(ct)), AES.block_size)
    return pt.decode()

# DES
def des_encrypt(text, passkey):
    key = derive_key(passkey, 8)
    cipher = DES.new(key, DES.MODE_CBC)
    ct = cipher.encrypt(pad(text.encode(), DES.block_size))
    return base64.b64encode(cipher.iv).decode(), base64.b64encode(ct).decode()

def des_decrypt(iv, ct, passkey):
    key = derive_key(passkey, 8)
    cipher = DES.new(key, DES.MODE_CBC, base64.b64decode(iv))
    pt = unpad(cipher.decrypt(base64.b64decode(ct)), DES.block_size)
    return pt.decode()

# RSA
rsa_private_key = None
rsa_public_key = None

def rsa_generate_keys():
    global rsa_private_key, rsa_public_key
    key = RSA.generate(2048)
    rsa_private_key = key.export_key()
    rsa_public_key = key.publickey().export_key()

def rsa_encrypt(text):
    key = RSA.import_key(rsa_public_key)
    cipher = PKCS1_OAEP.new(key)
    return base64.b64encode(cipher.encrypt(text.encode())).decode()

def rsa_decrypt(cipher_text):
    key = RSA.import_key(rsa_private_key)
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(base64.b64decode(cipher_text)).decode()

# GUI Functions
def perform_encryption():
    algorithm = algo_var.get()
    text = input_text.get("1.0", tk.END).strip()
    passkey = passkey_entry.get()
    
    if not text:
        messagebox.showwarning("Input Required", "Please enter text to encrypt.")
        return

    try:
        if algorithm == "AES":
            if not passkey:
                messagebox.showerror("Passkey Required", "AES requires a passkey.")
                return
            iv, ct = aes_encrypt(text, passkey)
            iv_output.set(iv)
            result_output.set(ct)

        elif algorithm == "DES":
            if not passkey:
                messagebox.showerror("Passkey Required", "DES requires a passkey.")
                return
            iv, ct = des_encrypt(text, passkey)
            iv_output.set(iv)
            result_output.set(ct)

        elif algorithm == "RSA":
            rsa_generate_keys()
            ct = rsa_encrypt(text)
            iv_output.set("Not required")
            result_output.set(ct)

    except Exception as e:
        messagebox.showerror("Encryption Error", str(e))

def perform_decryption():
    algorithm = algo_var.get()
    ct = result_output.get()
    iv = iv_output.get()
    passkey = passkey_entry.get()

    if not ct:
        messagebox.showwarning("Input Required", "No ciphertext to decrypt.")
        return

    try:
        if algorithm == "AES":
            decrypted = aes_decrypt(iv, ct, passkey)
        elif algorithm == "DES":
            decrypted = des_decrypt(iv, ct, passkey)
        elif algorithm == "RSA":
            decrypted = rsa_decrypt(ct)
        decrypted_output.set(decrypted)
    except Exception as e:
        messagebox.showerror("Decryption Error", str(e))

# Build GUI
root = tk.Tk()
root.title("Encryption Tool")
root.geometry("600x500")

tk.Label(root, text="Text to Encrypt:").pack()
input_text = tk.Text(root, height=5, width=70)
input_text.pack()

tk.Label(root, text="Choose Algorithm:").pack()
algo_var = tk.StringVar(value="AES")
algo_menu = ttk.Combobox(root, textvariable=algo_var, values=["AES", "DES", "RSA"], state="readonly")
algo_menu.pack()

tk.Label(root, text="Passkey (AES/DES only):").pack()
passkey_entry = tk.Entry(root, show="*")
passkey_entry.pack()

tk.Button(root, text="Encrypt", command=perform_encryption).pack(pady=5)

tk.Label(root, text="IV (for AES/DES):").pack()
iv_output = tk.StringVar()
tk.Entry(root, textvariable=iv_output, width=70).pack()

tk.Label(root, text="Encrypted Text:").pack()
result_output = tk.StringVar()
tk.Entry(root, textvariable=result_output, width=70).pack()

tk.Button(root, text="Decrypt", command=perform_decryption).pack(pady=5)

tk.Label(root, text="Decrypted Text:").pack()
decrypted_output = tk.StringVar()
tk.Entry(root, textvariable=decrypted_output, width=70).pack()

tk.Button(root, text="Exit", command=root.quit).pack(pady=10)

root.mainloop()
