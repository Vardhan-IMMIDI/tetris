import curses
from curses import wrapper
import time

from tetris import Tetris


def main(stdscr):
    curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLUE)
    # stdscr.addstr(0, 0, "Hello World!", curses.color_pair(1))
    # stdscr.refresh()
    # stdscr.getch()
    last = time.time()
    tetris = Tetris()
    height, width = curses.LINES, curses.COLS
    height = (height // 2) - 10
    width = (width // 2) - 10
    frame = 0
    while True:
        now = time.time()
        if now - last > 0.5:
            frame += 1
            last = now
            for i in range(tetris.ROWS):
                for j in range(tetris.COLS):
                    if tetris.board[i][j] > 0:
                        stdscr.addstr(i + height, (j * 2) + width, " ", curses.color_pair(1))
                    else:
                        stdscr.addstr(i + height, (j * 2) + width, " ")
            stdscr.refresh()


if __name__ == '__main__':
    wrapper(main)