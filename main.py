from src.dictionary import search_word, format_result
from src.database import (
    initialize_database,
    save_history,
    view_history,
    clear_history,
    add_favorite,
    view_favorites,
)

LINE = "=" * 70


def display_result(result):
    print("\n" + LINE)
    print("SMART DICTIONARY PRO")
    print(LINE)

    print(f"Word         : {result['word']}")
    print(f"Pronunciation: {result['phonetic']}")

    print(LINE)

    for i, meaning in enumerate(result["meanings"], start=1):

        print(f"\nMeaning {i}")
        print(f"Part of Speech : {meaning['part_of_speech']}")
        print(f"Definition     : {meaning['definition']}")
        print(f"Example        : {meaning['example']}")

        synonyms = meaning["synonyms"]
        antonyms = meaning["antonyms"]

        if synonyms:
            print("Synonyms      :", ", ".join(synonyms[:5]))
        else:
            print("Synonyms      : None")

        if antonyms:
            print("Antonyms      :", ", ".join(antonyms[:5]))
        else:
            print("Antonyms      : None")

        print("-" * 70)


def search():

    word = input("\nEnter a word: ").strip().lower()

    data = search_word(word)

    if data is None:
        print("\nWord not found.")
        return

    save_history(word)

    result = format_result(data)

    display_result(result)

    choice = input("\nAdd this word to favorites? (y/n): ").lower()

    if choice == "y":
        add_favorite(result["word"])


def menu():

    initialize_database()

    while True:

        print("\n")
        print(LINE)
        print("SMART DICTIONARY PRO")
        print(LINE)
        print("1. Search Word")
        print("2. View Search History")
        print("3. Clear Search History")
        print("4. View Favorite Words")
        print("5. Exit")
        print(LINE)

        choice = input("Enter your choice: ")

        if choice == "1":
            search()

        elif choice == "2":
            view_history()

        elif choice == "3":
            clear_history()

        elif choice == "4":
            view_favorites()

        elif choice == "5":
            print("\nThank you for using Smart Dictionary Pro.")
            break

        else:
            print("\nInvalid choice. Please try again.")


if __name__ == "__main__":
    menu()