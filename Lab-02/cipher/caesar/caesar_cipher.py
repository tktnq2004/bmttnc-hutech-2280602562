from .alphabet import ALPHABET

class CaesarCipher:
    def __init__(self):
        self.alphabet = ALPHABET

    def encrypt_text(self, text: str, shift: int) -> str:
        text = text.upper()
        encrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                idx = self.alphabet.index(letter)
                encrypted_text.append(self.alphabet[(idx + shift) % len(self.alphabet)])
            else:
                encrypted_text.append(letter)
        return ''.join(encrypted_text)

    def decrypt_text(self, text: str, shift: int) -> str:
        text = text.upper()
        decrypted_text = []
        for letter in text:
            if letter in self.alphabet:
                idx = self.alphabet.index(letter)
                decrypted_text.append(self.alphabet[(idx - shift) % len(self.alphabet)])
            else:
                decrypted_text.append(letter)
        return ''.join(decrypted_text)
