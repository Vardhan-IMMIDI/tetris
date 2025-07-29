import random

class Tetris:
    def __init__(self):
        self.ROWS = 20
        self.COLS = 10
        self.game_end = False
        self.current_block = []
        self.current_block_num = 0
        self.board = [[[0,0] for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.blocks = (((0, 0), (0, 1), (1, 0), (1, 1)), # Square
                       ((0, 0), (1, 0), (2, 0), (3, 0)), # Line
                       ((0, 1), (0, 2), (1, 0), (1, 1)), # S
                       ((0, 0), (0, 1), (1, 1), (1, 2)), # Z
                       ((0, 0), (1, 0), (2, 0), (2, 1)), # L
                       ((0, 1), (1, 1), (2, 0), (2, 1)), # J
                       ((0, 1), (1, 0), (1, 1), (1, 2))) # T (In reverse)
        self.sizes = ((2, 2), (4, 1), (2, 3), (2, 3), (3, 2), (3, 2), (2, 3))

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
        random_block = random.randint(0, len(self.blocks) - 1)
        block = self.blocks[random_block]
        size = self.sizes[random_block]
        random_pos = random.randint(0, self.COLS - size[1] - 1)
        for i in range(len(block)):
            if self.board[block[i][0]][block[i][1] + random_pos][0] != 0:
                self.game_end = True
                break
        else:
            self.current_block_num += 1
            self.current_block = []
            for i in range(len(block)):
                self.board[block[i][0]][block[i][1] + random_pos][0] = self.current_block_num
                self.board[block[i][0]][block[i][1] + random_pos][1] = 1
                self.current_block.append([block[i][0], block[i][1] + random_pos])



    def move(self, direction):
        if direction == "LEFT":
            move = -1
        elif direction == "RIGHT":
            move = 1
        else:
            print("Program Working Incorrectly")
            return
        for i in range(len(self.current_block)):
            try:
                if self.current_block[i][1] + move < 0:
                    break
                if self.board[self.current_block[i][0]][self.current_block[i][1] + move][0] not in [0, self.current_block_num]:
                    break
            except IndexError:
                break
        else:
            for i in range(len(self.current_block)):
                self.board[self.current_block[i][0]][self.current_block[i][1]][0] = 0
                self.board[self.current_block[i][0]][self.current_block[i][1]][1] = 0
            for i in range(len(self.current_block)):
                self.current_block[i][1] += move
            for i in range(len(self.current_block)):
                self.board[self.current_block[i][0]][self.current_block[i][1]][0] = self.current_block_num
                self.board[self.current_block[i][0]][self.current_block[i][1]][1] = 1




    def current_block_gravity(self):
        for i in range(len(self.current_block)):
            try:
                if self.board[self.current_block[i][0] + 1][self.current_block[i][1]][0] not in [0, self.current_block_num]:
                    self.delete_rows()
                    self.add_block()
                    break
            except IndexError:
                self.delete_rows()
                self.add_block()
                break
        else:
            for i  in range(len(self.current_block)):
                self.board[self.current_block[i][0]][self.current_block[i][1]][0] = 0
                self.board[self.current_block[i][0]][self.current_block[i][1]][1] = 0
            for i in range(len(self.current_block)):
                self.current_block[i][0] += 1
            for i in range(len(self.current_block)):
                self.board[self.current_block[i][0]][self.current_block[i][1]][0] = self.current_block_num
                self.board[self.current_block[i][0]][self.current_block[i][1]][1] = 1

    def delete_rows(self):
        rows_deleted = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.board[i][j][0] == 0:
                    break
            else:
                rows_deleted += 1
                self.board[i] = [[0,0] for _ in range(self.COLS)]
                for j in range(i, 0, -1):
                    self.board[j] = self.board[j - 1]
                self.board[0] = [[0, 0] for _ in range(self.COLS)]



    def rotate(self):
        ...

    def soft_drop(self):
        ...

    def hard_drop(self):
        ...

