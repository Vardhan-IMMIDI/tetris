class Tetris:
    def __init__(self):
        self.ROWS = 20
        self.COLS = 10
        self.board = [[0 for x in range(self.COLS)] for y in range(self.ROWS)]

    def move(self, direction):
        ...

    def gravity(self):
        ...

    def rotate(self):
        ...