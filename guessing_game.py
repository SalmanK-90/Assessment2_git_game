import random

DIFFICULTY = {
    "easy":   {"range": (1, 20),   "max_attempts": 8},
    "normal": {"range": (1, 50),   "max_attempts": 7},
    "hard":   {"range": (1, 100),  "max_attempts": 6},
}

def choose_difficulty():
    print("Select difficulty: [easy] [normal] [hard]")
    while True:
        choice = input("Difficulty: ").strip().lower()
        if choice in DIFFICULTY:
            return choice
        print("Please choose 'easy', 'normal', or 'hard'.")

def play_with_difficulty():
    level = choose_difficulty()
    rmin, rmax = DIFFICULTY[level]["range"]
    max_attempts = DIFFICULTY[level]["max_attempts"]
    secret = random.randint(rmin, rmax)
    attempts = 0

    print(f"\n🎯 Guess the number between {rmin} and {rmax}.")
    print(f"🕒 You have {max_attempts} attempts.")

    while attempts < max_attempts:
        raw = input(f"Attempt {attempts+1}/{max_attempts} — your guess: ").strip()
        if not raw.lstrip("-").isdigit():  # allow negative sign, we'll range-check next
            print("Please enter a whole number.")
            continue
        guess = int(raw)

        if not (rmin <= guess <= rmax):
            print(f"Out of range! Please enter a number between {rmin} and {rmax}.")
            continue

        attempts += 1
        if guess < secret:
            print("Too low!")
        elif guess > secret:
            print("Too high!")
        else:
            print(f"✅ Correct! You needed {attempts} attempt(s).")
            return

    print(f"❌ Out of attempts! The number was {secret}.")

def main():
    print("\n=== Number Guessing Game ===\n")
    play_with_difficulty()
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()