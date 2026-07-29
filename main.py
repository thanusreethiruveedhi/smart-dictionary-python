from src.dictionary import search_word


def main():
    print("=" * 50)
    print("        SMART DICTIONARY PRO")
    print("=" * 50)

    word = input("Enter a word: ").strip().lower()

    result = search_word(word)

    if not result:
        print("\n❌ Word not found!")
        return

    entry = result[0]

    print("\n" + "=" * 50)
    print(f"Word: {entry['word']}")

    if "phonetic" in entry:
        print(f"Pronunciation: {entry['phonetic']}")

    print("=" * 50)

    meanings = entry["meanings"]

    for meaning in meanings:
        print(f"\nPart of Speech: {meaning['partOfSpeech']}")

        for definition in meaning["definitions"]:
            print(f"\nMeaning: {definition['definition']}")

            if "example" in definition:
                print(f"Example: {definition['example']}")


if __name__ == "__main__":
    main()