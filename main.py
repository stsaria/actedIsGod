import random, time

def main():
    with open("actedIsGod.txt", encoding="utf-8" ,mode="r") as f:
        actedIsGodTexts = f.read().split("\n")
    while True:
        print(random.choice(actedIsGodTexts))
        time.sleep(2)

if __name__ == "__main__":
    main()