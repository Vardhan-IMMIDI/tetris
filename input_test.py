import curses
from curses import wrapper
import time

def main(stdscr):
    stdscr.nodelay(True)
    curses.cbreak()
    last = time.time()
    flag = False
    while True:
        try:
            key = stdscr.getkey()
            flag = True
        except curses.error:
            pass
        now = time.time()
        if now - last > 0.1:
            last = now
            stdscr.clear()
            if flag:
                stdscr.addstr(key)
                key = None
                flag = False
            stdscr.refresh()

if __name__ == '__main__':
    wrapper(main)