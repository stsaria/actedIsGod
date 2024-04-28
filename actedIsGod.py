import random, time

def actedIsGod():
    with open("actedIsGod.txt", encoding="utf-8" ,mode="r") as f:
        actedIsGodTexts = f.read().split("\n")
    return random.choice(actedIsGodTexts)