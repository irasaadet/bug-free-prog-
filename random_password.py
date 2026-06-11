import random
import string

def generate_password(length=12, use_special=True):
    """Generates a random password."""
    characters = string.ascii_letters + string.digits
    if use_special:
        characters += "!@#$%^&*()_+-="
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

if __name__ == "__main__":
    print("Random password (12 chars):", generate_password())
    print("Random password (16 chars):", generate_password(16))
    print("Simple password (no special):", generate_password(10, use_special=False))
