import pyglet
import numpy as np
from pyglet.window import key
from pyglet import shapes
import pkg_resources
from .solver import calculate_entropy, get_color_pattern, \
                    get_possible_words, get_allowed_words
                    
CELL_WIDTH = 200
CELL_HEIGHT = 200

alphabet = [key.A, key.B, key.C, key.D,
            key.E, key.F, key.G, key.H,
            key.I, key.J, key.K, key.L,
            key.M, key.N, key.O, key.P,
            key.Q, key.R, key.S, key.T,
            key.U, key.V, key.W, key.X,
            key.Y, key.Z]

# COLORS
BLACK = (0, 0, 0)
GREY = (120, 124, 126)
GREEN = (106, 170, 100)
YELLOW = (201, 180, 88)
WHITE = (255, 255, 255)


class WordleGame(pyglet.window.Window):

    def __init__(self, mode='play'):
        self.wordle = Wordle(mode=mode)
        super().__init__(width=CELL_WIDTH * 10, 
                         height=CELL_HEIGHT * 6,
                         visible=False)
        self.event_loop = pyglet.app.event_loop

    def run(self):
        self.set_visible()
        pyglet.app.run()

    def on_draw(self):
        self.clear()
        self.wordle.grid.draw()
        self.wordle.print_suggestions()
        if self.wordle.finished:
            if self.wordle.won:
                end_text = "You won!"
            else:
                end_text = "You lost!"
            r = pyglet.shapes.Rectangle(x = 0,
                                        y = 0,
                                        width = CELL_WIDTH * 5,
                                        height = CELL_HEIGHT * 6,
                                        color = BLACK)
            r.opacity = 128
            r.draw()
            l = pyglet.text.Label(text=end_text,
                                    x = CELL_WIDTH * 2.5,
                                    y = CELL_HEIGHT * 3,
                                    font_size = 50,
                                    anchor_x='center',
                                    anchor_y='center')
            l.draw()


    def on_key_press(self, symbol, modifiers):
        if self.wordle.finished is False:
            if symbol in alphabet:
                self.wordle.enter_letter(symbol)
            if symbol == key.BACKSPACE:
                self.wordle.backspace()
            if symbol == key.ENTER:
                self.wordle.enter()
        if symbol == key.ESCAPE:
            self.event_loop.exit()


    def on_mouse_press(self, x, y, button, modifiers):
        row, col = self.get_cell_at_position(x, y)
        self.wordle.click(row, col)


    def on_window_close(self, window):
        self.event_loop.exit()

    def get_cell_at_position(self, x, y):
            if x > CELL_WIDTH * 5:
                return (None, None)
            col = (x // CELL_WIDTH) 
            row = 5 - y // CELL_HEIGHT
            return (row, col)

class Cell():
    def __init__(self, row, col):
        self.x = col * CELL_WIDTH
        self.y = 5 * CELL_HEIGHT - row * CELL_HEIGHT
        self.in_active_row = False
        self.active = False
        self.entered = False
        self.letter = "NONE"
        self.correct = False
        self.elsewhere = False
        self.missing = False

    def set_letter(self, n):
        self.letter = n

    def delete_letter(self):
        self.letter = "NONE"

    def set_in_active_row(self, active):
        self.in_active_row = active
    
    def set_active(self, active):
        self.active(self, active)

    def draw(self):
        if self.entered is False:
            if self.in_active_row:
                if self.active:
                    color = WHITE
                else:
                    color = GREY
            else:
                color = BLACK
        else:
            if self.correct is True:
                color = GREEN
            elif self.elsewhere is True:
                color = YELLOW
            else:
                color = GREY

        scale = 0.92
        rb = shapes.Rectangle(self.x, self.y,
                                width=CELL_WIDTH*scale,
                                height=CELL_HEIGHT*scale,
                                color=color)

        if self.entered:
            if self.correct is True:
                color = GREEN
            elif self.elsewhere is True:
                color = YELLOW
            else:
                color = GREY
        else:
            color = BLACK

        shift = 20
        r = shapes.Rectangle(self.x + shift, 
                             self.y + shift, 
                             width=CELL_WIDTH * scale - 2 * shift, 
                             height=CELL_HEIGHT * scale - 2 * shift,
                             color=color)
        rb.draw()
        r.draw()
        if self.letter != "NONE":
            l = pyglet.text.Label(text=self.letter.upper(), 
                                  x=self.x + CELL_WIDTH / 2, 
                                  y=self.y + CELL_HEIGHT / 2,
                                  font_size=100,
                                  color=(255,255,255,255),
                                  anchor_x='center',
                                  anchor_y='center')
            l.draw()

class Row():
    def __init__(self, row):
        self.cells = [Cell(row, col) for col in range(5)]
    
    def draw(self):
        return [cell.draw() for cell in self.cells]

    def activate_row(self):
        for cell in self.cells:
            cell.set_in_active_row(True)
    
    def deactivate_row(self):
        for cell in self.cells:
            cell.set_in_active_row(False)


class Grid():
    def __init__(self):
        self.rows = [Row(row) for row in range(6)]
        self.rows[0].activate_row()

    def draw(self):
        return [row.draw() for row in self.rows]


class Wordle():
    n_simulations = 0
    n_guesses = 0

    def __init__(self, mode='play', solution=None):
        self.mode = mode
        self.solution = solution
        if self.solution is None:
            self.solution = self.get_random_solution()
        self.word_list = get_possible_words()
        self.grid = Grid()
        self.current_row = 0
        self.current_col = 0
        self.won = False
        self.finished = False

        allowed_words = get_allowed_words()
        resource_package = __name__
        resource_path = '/'.join(('data', 'allowed_words_entropies.txt'))
        entropies = pkg_resources.resource_string(resource_package, 
                                                  resource_path)
        entropies = entropies.split(b'\n')
        entropies = [float(entropy.decode('UTF-8')) 
                     for entropy in entropies[:-1]]
        zipped = list(zip(allowed_words, entropies))
        sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        self.suggestions = [x[0] for x in sorted_zipped[:10]]
        self.entropies = [x[1] for x in sorted_zipped[:10]]

        if mode == 'simulate':
            WordleGame.n_simulations += 1
            self.autoplay()

        #pyglet.app.run()

    def autoplay(self):
        n_guesses = 0
        while self.finished == False:
            guess = list(self.suggestions[0])
            for letter in guess:
                self.enter_letter(letter)
            self.enter()
            n_guesses += 1
            #self.grid.draw()

        WordleGame.n_guesses += n_guesses


    def get_suggestions(self):
        entropies = []
        N = len(self.word_list)
        for index, word in enumerate(self.word_list):
            entropies.append(calculate_entropy(word, self.word_list))
            if self.mode != 'simulate':
                print(f'Calculating suggestions: {index+1} / {N}', end='\r')
        if self.mode != 'simulate':
            print('\n', end='\r')
        zipped = list(zip(self.word_list, entropies))
        sorted_zipped = sorted(zipped, key=lambda x: x[1], reverse=True)
        self.suggestions = [x[0] for x in sorted_zipped[:10]]
        self.entropies = [x[1] for x in sorted_zipped[:10]]

    def print_suggestions(self):
        suggestions = self.suggestions
        entropies = self.entropies
        l = pyglet.text.Label(text="Suggestions:",
                    x = 5 * CELL_WIDTH,
                    y = 5.5 * CELL_HEIGHT,
                    font_size = 50)
        l.draw()
        for index, suggestion in enumerate(suggestions):
            l = pyglet.text.Label(text=suggestion,
                                    x = 5 * CELL_WIDTH,
                                    y = 5 * CELL_HEIGHT - index * 100,
                                    font_size = 50)
            l.draw()
            l = pyglet.text.Label(text=f'{entropies[index]:.3f}',
                        x = 6.5 * CELL_WIDTH,
                        y = 5 * CELL_HEIGHT - index * 100,
                        font_size = 50)
            l.draw()

    def get_random_solution(self):
        resource_package = __name__
        resource_path = '/'.join(('data', 'possible_words.txt'))
        word_list = pkg_resources.resource_string(resource_package, resource_path)
        word_list = [word.decode('UTF-8') for word in word_list.split(b'\n')]
        index = np.random.randint(len(word_list))
        solution = word_list[index][:5]
        solution = solution.upper()
        return solution

    def enter_letter(self, n):
        row = self.grid.rows[self.current_row]
        cell = row.cells[self.current_col]
        if self.mode != 'simulate':
            n = chr(n)
        cell.set_letter(n)
        self.increment_letter()
    
    def increment_letter(self):
        if self.current_col < 4:
            self.current_col += 1

    def enter(self):
        row = self.grid.rows[self.current_row]
        cell = row.cells[self.current_col]
        if self.current_col < 4 or \
            self.current_col == 4 and cell.letter == "NONE":
            print("Not enough letters")
        elif self.mode == 'manual' and \
            any([cell.entered is False for cell in row.cells]):
            print("Enter colors by clicking on the boxes")
        else:
            if self.mode != 'manual':
                self.check()
            self.trim_word_list()
            if self.won is False:
                self.grid.rows[self.current_row].deactivate_row()
                self.current_row += 1
                self.get_suggestions()
                if self.current_row <= 5:
                    self.grid.rows[self.current_row].activate_row()
                    self.current_col = 0
                else:
                    self.finished = True
    
    def trim_word_list(self):
        row = self.grid.rows[self.current_row]
        input_word = "".join([cell.letter for cell in row.cells])
        input_word = input_word.upper()
        if self.mode == 'manual':
            current_color_pattern = self.get_current_color_pattern()
        else:
            current_color_pattern = get_color_pattern(input_word, 
                                                      self.solution)
        trimmed_word_list = []
        for word in self.word_list:
            color_pattern = get_color_pattern(input_word, word)
            if color_pattern == current_color_pattern:
                trimmed_word_list.append(word)
        self.word_list = trimmed_word_list

    def get_current_color_pattern(self):
        current_color_pattern = []
        for cell in self.grid.rows[self.current_row].cells:
            if cell.missing:
                current_color_pattern += "0"
            if cell.elsewhere:
                current_color_pattern += "1"
            if cell.correct:
                current_color_pattern += "2"
        current_color_pattern = "".join([c for c in current_color_pattern])
        return current_color_pattern

    def check(self):
        row = self.grid.rows[self.current_row]
        input_word = "".join([cell.letter for cell in row.cells])
        input_word = input_word.upper()
        color_pattern = get_color_pattern(input_word, self.solution)
        num_correct = 0
        for index, c in enumerate(list(color_pattern)):
            cell = row.cells[index]
            cell.entered = True
            if c == '2':
                cell.correct = True
                num_correct += 1
            elif c == '1':
                cell.elsewhere = True
            else:
                cell.missing = True
        if color_pattern == '22222':
            self.won = True
            self.finished = True
    
    def click(self, clicked_row, clicked_col):
        if self.current_row == clicked_row:
            row = self.grid.rows[self.current_row]
            cell = row.cells[clicked_col]
            if cell.entered == False:
                cell.entered = True
                cell.missing = True
            elif cell.missing == True:
                cell.missing = False
                cell.elsewhere = True
            elif cell.elsewhere == True:
                cell.correct = True
                cell.elsewhere = False
            elif cell.correct == True:
                cell.missing = True
                cell.correct = False
            cell.entered = True
            
    def backspace(self):
        row = self.grid.rows[self.current_row]
        cell = row.cells[self.current_col]
        if self.current_col == 4 and cell.letter != "NONE":
            cell = row.cells[self.current_col]
            cell.delete_letter()
        else:
            cell = row.cells[self.current_col - 1]
            cell.delete_letter()
            self.decrement_letter()
        
    def decrement_letter(self):
        if self.current_col > 0:
            self.current_col -= 1

