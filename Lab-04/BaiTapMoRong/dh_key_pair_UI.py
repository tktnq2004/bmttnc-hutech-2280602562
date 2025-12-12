import tkinter as tk
from tkinter import messagebox, scrolledtext

from cryptography.hazmat.primitives.asymmetric import dh
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import hashes


# ================== DH FUNCTIONS ======================

def generate_client_key_pair(parameters):
    private_key = parameters.generate_private_key()
    public_key = private_key.public_key()
    return private_key, public_key

def derive_shared_secret(private_key, server_public_key):
    shared_key = private_key.exchange(server_public_key)
    return shared_key

def perform_dh():
    try:
        with open("../dh_key_pair/server_public_key.pem", "rb") as f:
            server_public_key = serialization.load_pem_public_key(f.read())
            
        parameters = server_public_key.parameters()

        private_key, public_key = generate_client_key_pair(parameters)

        shared_secret = derive_shared_secret(private_key, server_public_key)
        hex_secret = shared_secret.hex()

        output_box.configure(state="normal")
        output_box.insert(tk.END, "Shared Secret:\n" + hex_secret + "\n\n")
        output_box.configure(state="disabled")
        output_box.see(tk.END)

        messagebox.showinfo("Success", "Shared secret computed successfully.")

    except Exception as e:
        messagebox.showerror("Error", str(e))


window = tk.Tk()
window.title("Diffie-Hellman Client Key Exchange")
window.geometry("550x400")

title_label = tk.Label(window, text="DH Client Key Exchange", font=("Arial", 16, "bold"))
title_label.pack(pady=10)

# Output box
output_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state="disabled", height=15)
output_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Button
run_button = tk.Button(window, text="Perform DH Handshake", font=("Arial", 12), command=perform_dh)
run_button.pack(pady=10)


window.mainloop()
