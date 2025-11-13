import random

def play_basic():
    secret = random.randint(1, 100)
    attempts = 0
    print("🎯 I picked a number between 1 and 100. Can you guess it?")
    while True:
        raw = input("Enter your guess: ").strip()
        if not raw.isdigit():
            print("Please enter a whole number.")
            continue
        guess = int(raw)
        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"✅ Correct! You needed {attempts} attempts.")
            break

def main():
    print("\n=== Number Guessing Game ===\n")
    play_basic()
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()