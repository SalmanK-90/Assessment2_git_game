import random
from scores import update_high_score, load_scores

DIFFICULTY = {
<<<<<<< Updated upstream
    "easy":   {"range": (1, 20),   "max_attempts": 8},
    "normal": {"range": (1, 50),   "max_attempts": 7},
    "hard":   {"range": (1, 100),  "max_attempts": 6},
=======
    "easy":   {"range": (1, 20),   "max_attempts": 8, "mult": 1},
    "normal": {"range": (1, 50),   "max_attempts": 7, "mult": 2},
    "hard":   {"range": (1, 100),  "max_attempts": 6, "mult": 3},
>>>>>>> Stashed changes
}

def choose_difficulty():
    print("Select difficulty: [easy] [normal] [hard]")
    while True:
        choice = input("Difficulty: ").strip().lower()
        if choice in DIFFICULTY:
            return choice
        print("Please choose 'easy', 'normal', or 'hard'.")

<<<<<<< Updated upstream
def play_with_difficulty():
    level = choose_difficulty()
    rmin, rmax = DIFFICULTY[level]["range"]
    max_attempts = DIFFICULTY[level]["max_attempts"]
=======
def play_with_difficulty(level: str, player: str):
    rmin, rmax = DIFFICULTY[level]["range"]
    max_attempts = DIFFICULTY[level]["max_attempts"]
    mult = DIFFICULTY[level]["mult"]
>>>>>>> Stashed changes
    secret = random.randint(rmin, rmax)
    attempts = 0

    print(f"\n🎯 Guess the number between {rmin} and {rmax}.")
    print(f"🕒 You have {max_attempts} attempts.")

    while attempts < max_attempts:
        raw = input(f"Attempt {attempts+1}/{max_attempts} — your guess: ").strip()
<<<<<<< Updated upstream
        if not raw.lstrip("-").isdigit():  # allow negative sign, we'll range-check next
=======
        if not raw.lstrip("-").isdigit():
>>>>>>> Stashed changes
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
<<<<<<< Updated upstream
            print(f"✅ Correct! You needed {attempts} attempt(s).")
            return

    print(f"❌ Out of attempts! The number was {secret}.")

def main():
    print("\n=== Number Guessing Game ===\n")
    play_with_difficulty()
=======
            # Simple scoring: base 100, minus attempts penalty, times difficulty multiplier
            score = max(0, (100 - (attempts - 1) * 10)) * mult
            print(f"✅ Correct! You needed {attempts} attempt(s). Score: {score}")

            improved, best = update_high_score(level, player, score)
            if improved:
                print(f"🏆 New high score for {level}! {best['player']} — {best['score']}")
            else:
                print(f"Best {level} score: {best['player']} — {best['score']}")

            return

    print(f"❌ Out of attempts! The number was {secret}. Score: 0")

def main():
    print("\n=== Number Guessing Game ===\n")
    player = input("Enter your name: ").strip() or "Player"
    level = choose_difficulty()
    highs = load_scores()
    if level in highs:
        print(f"Current {level} high score: {highs[level]['player']} — {highs[level]['score']}")
    play_with_difficulty(level, player)
>>>>>>> Stashed changes
    print("\nThanks for playing!")

if __name__ == "__main__":
    main()