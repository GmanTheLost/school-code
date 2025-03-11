import random

def pirate_insult(name):
    words = ["Scurvy Dog", "Bilge RAT!!!", "Yellow Belly", "Kraken-Bait"]
    return f"Arrr, {name}, ye {random.choice(words)}!"

print(pirate_insult("Peter"))