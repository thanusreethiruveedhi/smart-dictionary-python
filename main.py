from src.dictionary import search_word


def main():
    print("=" * 60)
    print("            SMART DICTIONARY PRO")
    print("=" * 60)

    word = input("Enter a word: ").strip().lower()

    result = search_word(word)

    if not result:
        print("\n❌ Word not found!")
        return

    entry = result[0]

    print("\n" + "=" * 60)
    print(f"📖 Word : {entry['word']}")

    if entry.get("phonetic"):
        print(f"🔊 Pronunciation : {entry['phonetic']}")

    print("=" * 60)

    for meaning in entry["meanings"]:

        print(f"\n📚 Part of Speech : {meaning['partOfSpeech']}")

        for definition in meaning["definitions"]:

            print(f"\n✅ Meaning : {definition['definition']}")

            if definition.get("example"):
                print(f"💡 Example : {definition['example']}")

            if definition.get("synonyms"):
                print("⭐ Synonyms :")
                for synonym in definition["synonyms"][:5]:
                    print(f"   • {synonym}")

            if definition.get("antonyms"):
                print("🚫 Antonyms :")
                for antonym in definition["antonyms"][:5]:
                    print(f"   • {antonym}")

        print("-" * 60)


if __name__ == "__main__":
    main()