import random

def generate_code(length=6):
    """Generates a random 6-digit numeric code."""
    return ''.join(str(random.randint(0, 9)) for _ in range(length))

if __name__ == "__main__":
    print(f"Random 6-digit code: {generate_code()}")
    
    # Generate 5 unique codes
    codes = set()
    while len(codes) < 5:
        codes.add(generate_code())
    print("Unique codes:", sorted(codes))
