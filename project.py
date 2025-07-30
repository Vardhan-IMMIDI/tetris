import curses
from curses import wrapper
import time
import random


def main(stdscr):
    if curses.LINES < 25 or curses.COLS < 25:
        raise SizeError()
    curses.cbreak()
    curses.noecho()
    stdscr.keypad(True)
    stdscr.nodelay(True)
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_CYAN)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_GREEN)
    curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_MAGENTA)
    curses.init_pair(5, curses.COLOR_BLACK, curses.COLOR_RED)
    curses.init_pair(6, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(7, curses.COLOR_BLACK, curses.COLOR_WHITE)
    curses.init_pair(8, curses.COLOR_BLACK, curses.COLOR_BLACK)
    curses.init_pair(9, curses.COLOR_WHITE, curses.COLOR_BLACK)

    last = time.time()
    tetris = Tetris()
    height, width = curses.LINES, curses.COLS
    height = (height // 2) - 10
    width = (width // 2) - 10

    frame = 0
    flag = False
    while True:
        try:
            key = stdscr.getkey()
            flag = True
        except curses.error:
            pass
        now = time.time()
        if now - last > 0.2:
            if tetris.game_end:
                break
            last = now
            if frame == 0:
                tetris.add_block()
            if frame % 3 == 0:
                tetris.current_block_gravity()
            frame += 1
            if flag:
                flag = False
                if key == "q" or key == "Q":
                    break
                if key == "p" or key == "P":
                    while True:
                        try:
                            if stdscr.getkey() in ["p", "P"]:
                                break
                        except curses.error:
                            pass
                if key in ["KEY_UP", "KEY_DOWN", "KEY_LEFT", "KEY_RIGHT"]:
                    tetris.input(key)

            # Print Horizontal Border
            for i in range(tetris.ROWS + 1):
                stdscr.addstr(i + height, width - 2, "  ", curses.color_pair(7))
                stdscr.addstr(i + height, width + (tetris.COLS * 2), "  ", curses.color_pair(7))
            # Print Vertical Border
            for j in range(tetris.COLS):
                stdscr.addstr(height + tetris.ROWS, (j * 2) + width, "  ", curses.color_pair(7))
            # Print Play Zone
            for i in range(tetris.ROWS):
                for j in range(tetris.COLS):
                    if tetris.board[i][j][1] > 0:
                        stdscr.addstr(i + height, (j * 2) + width, "  ",
                                      curses.color_pair(tetris.board[i][j][1]))
                    else:
                        stdscr.addstr(i + height, (j * 2) + width, "  ", curses.color_pair(8))
            stdscr.addstr(height - 2, width + 5, "Score: " +
                          str(tetris.score), curses.color_pair(7))
            stdscr.move(0, 0)
            stdscr.refresh()
    stdscr.clear()
    stdscr.nodelay(False)
    stdscr.addstr(height, width - 5, "Final Score: " + str(tetris.score))
    stdscr.addstr(height + 1, width - 7, "Press any key to Quit")
    stdscr.getch()
    stdscr.refresh()


def block_boundaries(block):
    h_max = max(i[0] for i in block)
    h_min = min(i[0] for i in block)
    w_max = max(i[1] for i in block)
    w_min = min(i[1] for i in block)
    return h_max, h_min, w_max, w_min


def can_place_block(block, current_block_num, board, ROWS, COLS):
    for r, c in block:
        if not (0 <= r < ROWS and 0 <= c < COLS):
            return False
        if board[r][c][0] not in [0, current_block_num]:
            return False
    return True


def rm_current_from_board(current_block, board):
    for i in range(len(current_block)):
        board[current_block[i][0]][current_block[i][1]][0] = 0
        board[current_block[i][0]][current_block[i][1]][1] = 0


def add_current_to_board(board, current_block, current_block_num, current_block_color):
    for i in range(len(current_block)):
        board[current_block[i][0]][current_block[i][1]][0] = current_block_num
        board[current_block[i][0]][current_block[i][1]][1] = current_block_color


class SizeError(Exception):
    def __init__(self, message="Terminal too small, please open in a new Terminal"):
        self.message = message
        super().__init__(self.message)


class Tetris:
    def __init__(self):
        self.ROWS = 20
        self.COLS = 10
        self.game_end = False
        self.current_block = []
        self.current_block_num = 0
        self.current_block_color = 0
        self.score = 0
        self.board = [[[0, 0] for _ in range(self.COLS)] for _ in range(self.ROWS)]
        self.blocks = (((0, 0), (0, 1), (1, 0), (1, 1)),  # Square
                       ((0, 0), (1, 0), (2, 0), (3, 0)),  # Line
                       ((0, 1), (1, 1), (2, 0), (2, 1)),  # J
                       ((0, 0), (1, 0), (2, 0), (2, 1)),  # L
                       ((0, 1), (0, 2), (1, 0), (1, 1)),  # S
                       ((0, 1), (1, 0), (1, 1), (1, 2)),  # T (In reverse)
                       ((0, 0), (0, 1), (1, 1), (1, 2)))  # Z

        self.rotations = (
            # 0: Line block, 2 rotations
            (
                ((2, 0), (2, 1), (2, 2), (2, 3)),
                ((0, 1), (1, 1), (2, 1), (3, 1))
            ),
            # 1: J block, 4 rotations
            (
                ((1, 0), (1, 1), (1, 2), (2, 2)),
                ((0, 1), (1, 1), (2, 0), (2, 1)),
                ((0, 0), (1, 0), (1, 1), (1, 2)),
                ((0, 1), (0, 2), (1, 1), (2, 1))
            ),
            # 2: L block, 4 rotations
            (
                ((1, 0), (1, 1), (1, 2), (2, 0)),
                ((0, 0), (0, 1), (1, 1), (2, 1)),
                ((0, 2), (1, 0), (1, 1), (1, 2)),
                ((0, 1), (1, 1), (2, 1), (2, 2))
            ),
            # 3: S block, 2 rotations
            (
                ((1, 1), (1, 2), (2, 0), (2, 1)),
                ((0, 0), (1, 0), (1, 1), (2, 1))
            ),
            # 4: T block, 4 rotations
            (
                ((1, 0), (1, 1), (1, 2), (2, 1)),
                ((0, 1), (1, 0), (1, 1), (2, 1)),
                ((0, 1), (1, 0), (1, 1), (1, 2)),
                ((0, 1), (1, 1), (1, 2), (2, 1))
            ),
            # 5: Z block, 2 rotations
            (
                ((1, 0), (1, 1), (2, 1), (2, 2)),
                ((0, 1), (1, 0), (1, 1), (2, 0))
            )
        )

        self.sizes = ((2, 2), (4, 1), (2, 3), (2, 3), (3, 2), (3, 2), (2, 3))

    def rotate(self):
        h_max, h_min, w_max, w_min = block_boundaries(self.current_block)

        if h_max - h_min == 3 or w_max - w_min == 3:
            self.rotate_line()
        if h_max - h_min == 2 or w_max - w_min == 2:
            self.rotate_everything_else()
        if h_max - h_min == 1 and w_max - w_min == 1:
            self.rotate_cube()

    def rotate_line(self):
        h_max, h_min, w_max, w_min = block_boundaries(self.current_block)
        if h_max - h_min == 3:
            rotation_block = [[i[0] + h_min, i[1] + w_min - 1] for i in self.rotations[0][0]]
            if can_place_block(rotation_block, self.current_block_num, self.board, self.ROWS, self.COLS):
                rm_current_from_board(self.current_block, self.board)
                self.current_block = rotation_block
                add_current_to_board(self.board, self.current_block,
                                     self.current_block_num, self.current_block_color)
        elif w_max - w_min == 3:
            rotation_block = [[i[0] + h_min - 2, i[1] + w_min] for i in self.rotations[0][1]]
            if can_place_block(rotation_block, self.current_block_num, self.board, self.ROWS, self.COLS):
                rm_current_from_board(self.current_block, self.board)
                self.current_block = rotation_block
                add_current_to_board(self.board, self.current_block,
                                     self.current_block_num, self.current_block_color)
        else:
            print("Error!! Logic is not possible!")

    def rotate_cube(self):
        return

    def rotate_everything_else(self):
        h_max, h_min, w_max, w_min = block_boundaries(self.current_block)
        current_block = [[i[0] - h_min, i[1] - w_min] for i in self.current_block]
        for i in range(1, len(self.rotations)):
            for j in range(len(self.rotations[i])):
                rotation_block = [[i[0], i[1]] for i in self.rotations[i][j]]
                rbh_max, rbh_min, rbw_max, rbw_min = block_boundaries(rotation_block)
                if current_block == rotation_block:
                    rotation_block = [[i[0] + h_min, i[1] + w_min]
                                      for i in self.rotations[i][(j + 1) % len(self.rotations[i])]]
                    if can_place_block(rotation_block, self.current_block_num, self.board, self.ROWS, self.COLS):
                        rm_current_from_board(self.current_block, self.board)
                        self.current_block = rotation_block
                        add_current_to_board(self.board, self.current_block,
                                             self.current_block_num, self.current_block_color)
                        return

                if rbh_min > 0:
                    rotation_block = [[i[0] - rbh_min, i[1]] for i in rotation_block]
                    if current_block == rotation_block:
                        rotation_block = [[i[0] + h_min - 1, i[1] + w_min]
                                          for i in self.rotations[i][(j + 1) % len(self.rotations[i])]]
                        if can_place_block(rotation_block, self.current_block_num, self.board, self.ROWS, self.COLS):
                            rm_current_from_board(self.current_block, self.board)
                            self.current_block = rotation_block
                            add_current_to_board(self.board, self.current_block,
                                                 self.current_block_num, self.current_block_color)

                if rbw_min > 0:
                    rotation_block = [[i[0], i[1] - rbw_min] for i in rotation_block]
                    if current_block == rotation_block:
                        rotation_block = [[i[0] + h_min, i[1] + w_min - 1]
                                          for i in self.rotations[i][(j + 1) % len(self.rotations[i])]]
                        if can_place_block(rotation_block, self.current_block_num, self.board, self.ROWS, self.COLS):
                            rm_current_from_board(self.current_block, self.board)
                            self.current_block = rotation_block
                            add_current_to_board(self.board, self.current_block,
                                                 self.current_block_num, self.current_block_color)

    def input(self, key):
        if key == "KEY_UP":
            self.rotate()
        elif key == "KEY_DOWN":
            self.soft_drop()
        elif key in ["KEY_LEFT", "KEY_RIGHT"]:
            self.move(key.split("_")[1])

    def add_block(self):
        random_block = random.randint(0, len(self.blocks) - 1)
        block = self.blocks[random_block]
        size = self.sizes[random_block]
        random_pos = random.randint(0, self.COLS - size[1] - 1)
        self.current_block_color = random.randint(1, 6)
        for i in range(len(block)):
            if self.board[block[i][0]][block[i][1] + random_pos][0] != 0:
                self.game_end = True
                break
        else:
            self.current_block_num += 1
            self.current_block = []
            for i in range(len(block)):
                self.board[block[i][0]][block[i][1] + random_pos][0] = self.current_block_num
                self.board[block[i][0]][block[i][1] + random_pos][1] = self.current_block_color
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
            rm_current_from_board(self.current_block, self.board)
            for i in range(len(self.current_block)):
                self.current_block[i][1] += move
            add_current_to_board(self.board, self.current_block,
                                 self.current_block_num, self.current_block_color)

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
            rm_current_from_board(self.current_block, self.board)
            self.current_block = [[i[0] + 1, i[1]] for i in self.current_block]
            add_current_to_board(self.board, self.current_block,
                                 self.current_block_num, self.current_block_color)

    def delete_rows(self):
        rows_deleted = 0
        for i in range(self.ROWS):
            for j in range(self.COLS):
                if self.board[i][j][0] == 0:
                    break
            else:
                rows_deleted += 1
                self.board[i] = [[0, 0] for _ in range(self.COLS)]
                for j in range(i, 0, -1):
                    self.board[j] = self.board[j - 1]
                self.board[0] = [[0, 0] for _ in range(self.COLS)]
        if rows_deleted == 1:
            self.score += 40
        elif rows_deleted == 2:
            self.score += 100
        elif rows_deleted == 3:
            self.score += 300
        elif rows_deleted == 4:
            self.score += 1200

    def soft_drop(self):
        self.current_block_gravity()


if __name__ == '__main__':
    wrapper(main)
