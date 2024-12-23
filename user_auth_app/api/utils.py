import random

def generate_random_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"