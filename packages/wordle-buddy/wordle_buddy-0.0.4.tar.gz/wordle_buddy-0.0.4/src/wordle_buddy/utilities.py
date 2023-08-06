"""
Functions for downloading and reading word lists
"""
import requests
import os
import pkg_resources


def download_word_lists() -> None:
    """
    Downloads both word lists from 3blue1brown's github page
    """
    base_url = (
        "https://raw.githubusercontent.com/3b1b/videos/master/"
        + "2022/wordle/data/"
    )
    word_lists = ["allowed_words", "possible_words"]
    for word_list in word_lists:
        url = base_url + word_list + ".txt"
        r = requests.get(url)
        if os.path.exists("data") is False:
            os.makedirs("data")
        with open(f"data/{word_list}.txt", "wb") as f:
            f.write(r.content)


def get_words(list_name: str):
    """
    Reads the given word list from file into a list of capitalized words
    """
    resource_package = __name__
    resource_path = "/".join(("data", f"{list_name}.txt"))
    word_list = pkg_resources.resource_string(resource_package, resource_path)
    word_list = [word.decode("UTF-8") for word in word_list.split(b"\n")]
    word_list = [w[:5].upper() for w in word_list]
    return word_list
