from flask import Flask, request, jsonify
from cipher.railfence import RailFenceCipher

app = Flask(__name__)

vigenere_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.rail_fence_encrypt(plain_text, key) 
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.rail_fence_decrypt(cipher_text,key)
    return jsonify({'decrypted_text': decrypted_text})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)