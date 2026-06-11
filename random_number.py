import random

def get_random_number():
    """Returns a random integer between 1 and 100."""
    return random.randint(1, 100)

if __name__ == "__main__":
    print(f"Random number from 1 to 100: {get_random_number()}")
