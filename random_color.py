import random

def generate_hex_color():
    """Generates a random hex color code (e.g. #A3F2B1)."""
    return f"#{random.randint(0, 0xFFFFFF):06x}"

if __name__ == "__main__":
    print("Random hex color:", generate_hex_color())
    print("Another random color:", generate_hex_color())
    
    # Generate 5 random colors
    colors = [generate_hex_color() for _ in range(5)]
    print("5 random colors:", colors)
