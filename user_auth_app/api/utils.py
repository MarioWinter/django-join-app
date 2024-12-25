import random

def generate_random_color():
    """
    Generates a random hex color code.
    Returns:
        str: A string representing a random hex color code in the format '#RRGGBB'.
    """
    return f"#{random.randint(0, 0xFFFFFF):06x}"