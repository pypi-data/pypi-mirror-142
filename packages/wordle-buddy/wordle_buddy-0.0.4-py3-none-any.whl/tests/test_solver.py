"""module for testing the solver module"""

from wordle_buddy.solver import safe_log2, get_color_pattern, calculate_entropy


def test_safe_log2():
    assert safe_log2(-1) == 0, "Safe log2 of -1 doesn't produce zero"
    assert safe_log2(0) == 0, "Safe log2 of 0 doesn't produce zero!"
    assert safe_log2(1) == 0, "Safe log2 of 1 doesn't produce zero!"
    assert safe_log2(2) == 1, "Safe log2 of 2 doesn't produce one!"


def test_get_color_pattern():
    input_word = "EAGLE"
    solution = "EGRET"
    assert (
        get_color_pattern(input_word, solution) == "20101"
    ), "Incorrect color pattern"


def test_calculate_entropy():
    input_word = "EAGLE"
    word_list = ["ABACK", "ABASE", "ABATE"]
    entropy = 0.9182958340544896
    assert calculate_entropy(input_word, word_list) == entropy
