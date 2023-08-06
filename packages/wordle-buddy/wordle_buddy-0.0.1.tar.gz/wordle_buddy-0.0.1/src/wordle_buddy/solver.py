import numpy as np
import time
from typing import List
import math
import pkg_resources


def safe_log2(x):
    return math.log2(x) if x > 0 else 0


def get_color_pattern(input_word: str, solution: str) -> str:
    """
    Given an input word and a solution, generates the resulting
    color pattern.

    2.71 microseconds

    Note: this might optimized by using a ternary representation
    of the color pattern.
    """
    color_pattern = [0 for _ in range(5)]
    sub_solution = list(solution)
    for index, letter in enumerate(list(input_word)):
        if letter == solution[index]:
            color_pattern[index] = 2
            sub_solution[index] = '_'
    for index, letter in enumerate(list(input_word)):
        if letter in sub_solution and color_pattern[index] != 2:
            color_pattern[index] = 1
            sub_solution[sub_solution.index(letter)] = "_"
    color_pattern = "".join([str(c) for c in color_pattern])
    return color_pattern


def calculate_entropy(input_word: str, word_list: List[str]) -> float:
    """
    Given an input word and a list of possible solutions (word_list),
    calculates the expected information gain from the guess:

    sum_{c \in color_patterns} [-P(c) * Log2(P(c))]

    where P(c) is the probability that the input word yields color pattern c.
    """

    # Get counts for each color pattern (5 ^ 3 possibilities)
    color_patterns = [np.base_repr(n, base=3).zfill(5) for n in range(3 ** 5)]
    counts = {cp: 0 for cp in color_patterns}
    for word in word_list:
        color_pattern = get_color_pattern(input_word, word)
        counts[color_pattern] += 1

    # Using the counts, calculate the entropy
    entropy = 0
    N = len(word_list)
    for _, value in counts.items():
        prob = value / N
        entropy += -(prob) * safe_log2(prob)
    return entropy


def get_allowed_words():
    resource_package = __name__
    resource_path = '/'.join(('data', 'allowed_words.txt'))
    allowed_words = pkg_resources.resource_string(resource_package, 
                                                  resource_path)
    allowed_words = [word.decode('UTF-8') 
                     for word in allowed_words.split(b'\n')]
    allowed_words = [w[:5].upper() for w in allowed_words]
    return allowed_words


def get_possible_words():
    resource_package = __name__
    resource_path = '/'.join(('data', 'possible_words.txt'))
    possible_words = pkg_resources.resource_string(resource_package, 
                                                  resource_path)
    possible_words = [word.decode('UTF-8') 
                     for word in possible_words.split(b'\n')]
    possible_words = [w[:5].upper() for w in possible_words]
    return possible_words

if __name__ == "__main__":
    tic = time.perf_counter()
    words = get_possible_words()
    entropies = {w:0 for w in words}
    for word in words:
        entropies[word] = calculate_entropy(word, words)
    toc = time.perf_counter()
    print(f"Elapsed time: {toc-tic:.3f} seconds")

    sorted_entropies = {k:v for k,v in sorted(entropies.items(), 
                                            key=lambda item: item[1],
                                            reverse=True)}

    print("Top 10 Words (by entropy):")
    for word, entropy in list(sorted_entropies.items())[:10]:
        print(f'{word} : {entropy:.2f}')
    

            




