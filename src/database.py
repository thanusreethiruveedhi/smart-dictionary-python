import json
import os
from datetime import datetime

FILE_NAME = "data/history.json"


def save_history(word):
    history = []

    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            try:
                history = json.load(file)
            except:
                history = []

    history.append({
        "word": word,
        "time": datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    })

    with open(FILE_NAME, "w") as file:
        json.dump(history, file, indent=4)


def view_history():
    if not os.path.exists(FILE_NAME):
        print("\nNo search history found.")
        return

    with open(FILE_NAME, "r") as file:
        history = json.load(file)

    if len(history) == 0:
        print("\nNo search history.")
        return

    print("\n========== SEARCH HISTORY ==========\n")

    for item in history:
        print(f"{item['word']}  ({item['time']})")


def clear_history():
    with open(FILE_NAME, "w") as file:
        json.dump([], file)

    print("\nHistory cleared successfully.")