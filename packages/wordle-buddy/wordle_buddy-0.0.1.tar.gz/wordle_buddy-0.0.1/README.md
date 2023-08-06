# A Python package to play Wordle

My reproduction of the popular game (the real one [here](https://www.nytimes.com/games/wordle/index.html)), along with suggested words (based on entropy).

## Installation

```bash
pip install wordle-buddy
```

## Play a game

To play via the command line, simply run the `wordle_oden` command. To play in "manual mode", where you enter in the resulting colors, run `wordle_oden_manual`.

To play a game in a python terminal, instantiate a `WordleGame` object and use the `run()` method.

```python
from wordle_oden import WordleGame
game = WordleGame()
game.run()
```

To exit, press Esc.
