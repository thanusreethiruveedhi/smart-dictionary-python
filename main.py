from src.dictionary import search_word


def main():
    print("=" * 50)
    print("SMART DICTIONARY PRO")
    print("=" * 50)

    word = input("Enter a word: ").strip().lower()

    result = search_word(word)

    if result:
        print("\nWord found successfully!")
    else:
        print("\nWord not found.")


if __name__ == "__main__":
    main()