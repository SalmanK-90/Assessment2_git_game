import json
from pathlib import Path

DEFAULT_FILE = Path("scores.json")

def load_scores(file_path: Path = DEFAULT_FILE):
    if not file_path.exists():
        return {}
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {}

def save_scores(scores: dict, file_path: Path = DEFAULT_FILE):
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(scores, f, indent=2)

def update_high_score(level: str, player: str, score: int, file_path: Path = DEFAULT_FILE):
    scores = load_scores(file_path)
    best = scores.get(level)
    if best is None or score > best.get("score", -1):
        scores[level] = {"player": player, "score": score}
        save_scores(scores, file_path)
        return True, scores[level]
    return False, best