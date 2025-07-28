import time

from tetris import Tetris

def main():
    tetris = Tetris()
    last_frame = time.time()
    while True:
        now = time.time()
        if now - last_frame > 0.5:
            last_frame = now
