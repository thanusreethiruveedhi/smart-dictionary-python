import json
import os
from datetime import datetime

DATA_DIR = "data"
HISTORY_FILE = os.path.join(DATA_DIR, "history.json")
FAVORITES_FILE = os.path.join(DATA_DIR, "favorites.json")


def initialize_database():
    """Create data directory and JSON files if they don't exist."""

    os.makedirs(DATA_DIR, exist_ok=True)

    if not os.path.exists(HISTORY_FILE):
        with open(HISTORY_FILE, "w") as file:
            json.dump([], file)

    if not os.path.exists(FAVORITES_FILE):
        with open(FAVORITES_FILE, "w") as file:
            json.dump([], file)


def load_json(file_path):
    try:
        with open(file_path, "r") as file:
            return json.load(file)
    except:
        return []


def save_json(file_path, data):
    with open(file_path, "w") as file:
        json.dump(data, file, indent=4)


# --------------------------
# Search History
# --------------------------

def save_history(word):

    history = load_json(HISTORY_FILE)

    history.append({
        "word": word,
        "searched_at": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })

    save_json(HISTORY_FILE, history)


def view_history():

    history = load_json(HISTORY_FILE)

    if not history:
        print("\nNo search history found.")
        return

    print("\n========== SEARCH HISTORY ==========\n")

    for index, item in enumerate(history, start=1):
        print(f"{index}. {item['word']} ({item['searched_at']})")


def clear_history():

    save_json(HISTORY_FILE, [])

    print("\nSearch history cleared successfully.")


# --------------------------
# Favorites
# --------------------------

def add_favorite(word):

    favorites = load_json(FAVORITES_FILE)

    if word.lower() in [w.lower() for w in favorites]:
        print("\nAlready in favorites.")
        return

    favorites.append(word)

    save_json(FAVORITES_FILE, favorites)

    print("\nAdded to favorites.")


def remove_favorite(word):

    favorites = load_json(FAVORITES_FILE)

    updated = [w for w in favorites if w.lower() != word.lower()]

    save_json(FAVORITES_FILE, updated)

    print("\nFavorite removed.")


def view_favorites():

    favorites = load_json(FAVORITES_FILE)

    if not favorites:
        print("\nNo favorite words found.")
        return

    print("\n========== FAVORITE WORDS ==========\n")

    for index, word in enumerate(favorites, start=1):
        print(f"{index}. {word}")