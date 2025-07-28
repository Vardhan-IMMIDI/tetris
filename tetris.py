class Tetris:
    def __init__(self):
        self.ROWS = 20
        self.COLS = 10
        self.board = [[[0,0] for x in range(self.COLS)] for y in range(self.ROWS)]

    def input(self, key):
        if key == "KEY_UP":
            self.rotate()
        elif key == "KEY_DOWN":
            self.soft_drop()
        elif key in ["KEY_LEFT", "KEY_RIGHT"]:
            self.move(key.split("_")[1])
        elif key == " ":
            self.hard_drop()

    def add_block(self):
        ...

    def move(self, direction):
        ...

    def gravity(self):
        ...

    def rotate(self):
        ...

    def soft_drop(self):
        ...

    def hard_drop(self):
        ...