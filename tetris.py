class Tetris:
    def __init__(self, ROWS=20, COLS=10):
        self.ROWS = ROWS
        self.COLS = COLS
        self.board = [[0 for x in range(COLS)] for y in range(ROWS)]

    def move(self, direction):
        ...

    def gravity(self):
        ...

    def rotate(self):
        ...