import curses
from curses import wrapper
import time
from tetris import Tetris

class SizeError(Exception):
    def __init__(self, message="Terminal too small, please open in a new Terminal"):
        self.message = message
        super().__init__(self.message)

def main(stdscr):
    if curses.LINES < 25 or curses.COLS < 25:
        raise SizeError()
    stdscr.nodelay(True)
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLUE)
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_YELLOW)
    curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)
    last = time.time()
    tetris = Tetris()
    height, width = curses.LINES, curses.COLS
    height = (height // 2) - 10
    width = (width // 2) - 10

    frame = 0
    while True:
        key = stdscr.getkey()
        now = time.time()
        if now - last > 0.5:
            frame += 1
            last = now
            # Print Horizontal Border
            for i in range(tetris.ROWS + 1):
                stdscr.addstr(i + height, width - 2, "  ", curses.color_pair(3))
                stdscr.addstr(i + height, width + (tetris.COLS * 2), "  ", curses.color_pair(3))
            # Print Vertical Border
            for j in range(tetris.COLS):
                stdscr.addstr(height + tetris.ROWS, (j * 2) + width, "  ", curses.color_pair(3))
            # Print Play Zone
            for i in range(tetris.ROWS):
                for j in range(tetris.COLS):
                    if tetris.board[i][j] > 0:
                        stdscr.addstr(i + height, (j * 2) + width, "  ", curses.color_pair(1))
                    else:
                        stdscr.addstr(i + height, (j * 2) + width, "  ", curses.color_pair(2))
            stdscr.refresh()


if __name__ == '__main__':
    wrapper(main)