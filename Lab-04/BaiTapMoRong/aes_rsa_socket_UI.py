from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.PublicKey import RSA
from Crypto.Util.Padding import pad, unpad
from Crypto.Random import get_random_bytes
import socket
import threading
import tkinter as tk
from tkinter import scrolledtext

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 12345))

client_key = RSA.generate(2048)

server_public_key = RSA.import_key(client_socket.recv(4096))
client_socket.send(client_key.publickey().export_key(format='PEM'))

encrypt_aes_key = client_socket.recv(4096)
cipher_rsa = PKCS1_OAEP.new(client_key)
aes_key = cipher_rsa.decrypt(encrypt_aes_key)


def encrypt_message(key, message):
    cipher = AES.new(key, AES.MODE_CBC)
    ciphertext = cipher.encrypt(pad(message.encode(), AES.block_size))
    return cipher.iv + ciphertext

def decrypt_message(key, encrypted_message):
    iv = encrypted_message[:AES.block_size]
    ciphertext = encrypted_message[AES.block_size:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_message = unpad(cipher.decrypt(ciphertext), AES.block_size)
    return decrypted_message.decode()


def receive_messages():
    while True:
        try:
            encrypted_message = client_socket.recv(4096)
            if not encrypted_message:
                break

            decrypted_message = decrypt_message(aes_key, encrypted_message)

            chat_box.configure(state='normal')
            chat_box.insert(tk.END, f"Friend: {decrypted_message}\n")
            chat_box.configure(state='disabled')
            chat_box.see(tk.END)

        except:
            break


def send_message():
    message = input_box.get()
    if message.strip() == "":
        return

    encrypted = encrypt_message(aes_key, message)
    client_socket.send(encrypted)

    chat_box.configure(state='normal')
    chat_box.insert(tk.END, f"You: {message}\n")
    chat_box.configure(state='disabled')
    chat_box.see(tk.END)

    input_box.delete(0, tk.END)

    if message == "exit":
        client_socket.close()
        window.destroy()


window = tk.Tk()
window.title("Secure Chat Client (AES/RSA)")
window.geometry("450x500")

chat_box = scrolledtext.ScrolledText(window, wrap=tk.WORD, state='disabled')
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

input_box = tk.Entry(window, font=("Arial", 12))
input_box.pack(padx=10, pady=5, fill=tk.X)

send_button = tk.Button(window, text="Send", command=send_message)
send_button.pack(pady=5)

receive_thread = threading.Thread(target=receive_messages, daemon=True)
receive_thread.start()

window.mainloop()
