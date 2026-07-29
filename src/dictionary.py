import requests

BASE_URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"


def search_word(word):
    try:
        response = requests.get(BASE_URL + word)

        if response.status_code == 200:
            return response.json()
        else:
            return None

    except requests.exceptions.RequestException:
        return None