import json
from ui import game_over

SCORES_FILE = "scores.json"

def load_scores():
    try:
        with open(SCORES_FILE, "r") as file:
            pass

    except FileNotFoundError:
        pass

def save(score):
    name = input("What is your name?")
    game_over(name, score)
    return name