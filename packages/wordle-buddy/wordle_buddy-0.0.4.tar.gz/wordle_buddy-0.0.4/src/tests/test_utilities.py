"""module for testing the utilities module"""

from wordle_buddy import utilities as utils


def test_get_words():
    word_list = utils.get_words("possible_words")
    assert len(word_list) == 2315, "length of possible words incorrect"
    first_word = word_list[0]
    assert first_word == "ABACK", "first word in possible words incorrect"
    last_word = word_list[-1]
    assert last_word == "ZONAL", "last word in possible words incorrect"

    word_list = utils.get_words("allowed_words")
    assert len(word_list) == 12972, "length of allowed words incorrect"
    first_word = word_list[0]
    assert first_word == "AAHED", "first word in allowed words incorrect"
    last_word = word_list[-1]
    assert last_word == "ZYMIC", "last word in allowed words"
