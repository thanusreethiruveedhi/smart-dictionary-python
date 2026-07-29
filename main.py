from src.dictionary import search_word
from src.database import save_history, view_history, clear_history


def search():

    word = input("\nEnter a word: ").strip().lower()

    result = search_word(word)

    if not result:
        print("\nWord not found.")
        return

    save_history(word)

    entry = result[0]

    print("\n" + "=" * 60)
    print("Word :", entry["word"])

    if entry.get("phonetic"):
        print("Pronunciation :", entry["phonetic"])

    print("=" * 60)

    for meaning in entry["meanings"]:

        print("\nPart of Speech :", meaning["partOfSpeech"])

        for definition in meaning["definitions"]:

            print("\nMeaning :", definition["definition"])

            if definition.get("example"):
                print("Example :", definition["example"])


def main():

    while True:

        print("\n")
        print("=" * 50)
        print("SMART DICTIONARY PRO")
        print("=" * 50)
        print("1. Search Word")
        print("2. View Search History")
        print("3. Clear History")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            search()

        elif choice == "2":
            view_history()

        elif choice == "3":
            clear_history()

        elif choice == "4":
            print("\nThank you for using Smart Dictionary Pro.")
            break

        else:
            print("\nInvalid choice.")


if __name__ == "__main__":
    main()