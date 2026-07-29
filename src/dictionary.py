import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def search_word(word):
    """
    Search for a word using the Free Dictionary API.
    Returns JSON data if found, otherwise None.
    """

    try:
        response = requests.get(BASE_URL + word, timeout=10)

        if response.status_code != 200:
            return None

        data = response.json()

        if not data:
            return None

        return data[0]

    except requests.exceptions.RequestException:
        return None


def format_result(data):
    """
    Convert API response into a clean dictionary.
    """

    if not data:
        return None

    result = {
        "word": data.get("word", "N/A"),
        "phonetic": data.get("phonetic", "Not Available"),
        "meanings": []
    }

    for meaning in data.get("meanings", []):

        part = meaning.get("partOfSpeech", "Unknown")

        for definition in meaning.get("definitions", []):

            result["meanings"].append({

                "part_of_speech": part,

                "definition":
                    definition.get("definition", "Not Available"),

                "example":
                    definition.get("example", "No example available."),

                "synonyms":
                    definition.get("synonyms", []),

                "antonyms":
                    definition.get("antonyms", [])

            })

    return result