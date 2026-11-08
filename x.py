import secrets
import string

def generate_cipher(length: int = 1024, alphabet: str = None) -> str:
    if alphabet is None:
        alphabet = string.ascii_letters + string.digits + string.punctuation
    return ''.join(secrets.choice(alphabet) for _ in range(length))

if __name__ == "__main__":
    full_cipher = generate_cipher()
    hex_cipher = generate_cipher(length=1024, alphabet='0123456789ABCDEF')
    print(f"Ключ (1024 HEX-символа):\n{hex_cipher}\n")
    print(f"Длина: {len(hex_cipher)} символов")