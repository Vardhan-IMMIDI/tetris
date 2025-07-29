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
                       ((0, 1), (1, 1), (2, 0), (2, 1)), # J
                       ((0, 0), (1, 0), (2, 0), (2, 1)), # L
                       ((0, 1), (0, 2), (1, 0), (1, 1)), # S
                       ((0, 1), (1, 0), (1, 1), (1, 2)), # T (In reverse)
                       ((0, 0), (0, 1), (1, 1), (1, 2))) # Z

        self.rotations_v1 = ((((2, 0), (2, 1), (2, 2), (2, 3)),  # Line
                              ((0, 1), (1, 1), (2, 1), (3, 1))),

                             (((1, 0), (1, 1), (1, 2), (2, 2)), # J
                           ((0, 1), (1, 1), (2, 0), (2, 1)),
                           ((0, 0), (1, 0), (1, 1), (1, 2)),
                           ((0, 1), (0, 2), (1, 1), (2, 1))),

                             (((1, 0), (1, 1), (1, 2), (2, 0)), # L
                           ((0, 0), (0, 1), (1, 1), (2, 1)),
                           ((0, 2), (1, 0), (1, 1), (1, 2)),
                           ((0, 1), (1, 1), (2, 1), (2, 2))),

                             (((1, 1), (1, 2), (2, 0), (2, 1)), # S
                          ((0, 0), (1, 0), (1, 1), (2, 1))),

                             (((1, 0), (1, 1), (1, 2), (2, 1)),
                           ((0, 1), (1, 0), (1, 1), (2, 1)), # T
                           ((0, 1), (1, 0), (1, 1), (1, 2)),
                           ((0, 1), (1, 1), (1, 2), (2, 1))),

                             (((1, 0), (1, 1), (2, 1), (2, 2)), # Z
                           ((0, 1), (1, 0), (1, 1), (2, 0))))
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
        h_max = max(i[0] for i in self.current_block)
        h_min = min(i[0] for i in self.current_block)
        w_max = max(i[1] for i in self.current_block)
        w_min = min(i[1] for i in self.current_block)

        if h_max - h_min == 3 or w_max - w_min == 3:
            self.rotate_line()
        if h_max - h_min == 2 or w_max - w_min == 2:
            self.rotate_everything_else()
        if h_max - h_min == 1 and w_max - w_min == 1:
            self.rotate_cube()

    def rotate_line(self):
        h_max = max(i[0] for i in self.current_block)
        h_min = min(i[0] for i in self.current_block)
        w_max = max(i[1] for i in self.current_block)
        w_min = min(i[1] for i in self.current_block)

        if h_max - h_min == 3:
            rotation_block = [[i[0] + h_min, i[1] + w_min - 1] for i in self.rotations[0][0]]
            for i in range(len(rotation_block)):
                if rotation_block[i][0] not in range(self.ROWS) or rotation_block[i][1] not in range(self.COLS):
                    break
                if self.board[rotation_block[i][0]][rotation_block[i][1]][0] not in [0, self.current_block_num]:
                    break
            else:
                self.rm_current_from_board()
                self.current_block = rotation_block
                self.add_current_to_board()
        elif w_max - w_min == 3:
            rotation_block = [[i[0] + h_min - 2, i[1] + w_min] for i in self.rotations[0][1]]
            for i in range(len(rotation_block)):
                if rotation_block[i][0] not in range(self.ROWS) or rotation_block[i][1] not in range(self.COLS):
                    break
                if self.board[rotation_block[i][0]][rotation_block[i][1]][0] not in [0, self.current_block_num]:
                    break
            else:
                self.rm_current_from_board()
                self.current_block = rotation_block
                self.add_current_to_board()
        else:
            print("Error!! Logic is not possible!")

    def rotate_cube(self):
        return

    def rotate_everything_else(self):
        h_max = max(i[0] for i in self.current_block)
        h_min = min(i[0] for i in self.current_block)
        w_max = max(i[1] for i in self.current_block)
        w_min = min(i[1] for i in self.current_block)
        current_block = [[i[0] - h_min, i[1] - w_min] for i in self.current_block]
        for i in range(1, len(self.rotations)):
            for j in range(len(self.rotations[i])):
                rotation_block = [[i[0], i[1]] for i in self.rotations[i][j]]
                rbh_max = max(i[0] for i in rotation_block)
                rbh_min = min(i[0] for i in rotation_block)
                rbw_max = max(i[1] for i in rotation_block)
                rbw_min = min(i[1] for i in rotation_block)
                if current_block == rotation_block:
                    rotation_block = [[i[0] + h_min, i[1] + w_min] for i in self.rotations[i][(j + 1) % len(self.rotations[i])]]
                    for k in range(len(rotation_block)):
                        if rotation_block[k][0] not in range(self.ROWS) or rotation_block[k][1] not in range(self.COLS):
                            break
                        if self.board[rotation_block[k][0]][rotation_block[k][1]][0] not in [0, self.current_block_num]:
                            break
                    else:
                        self.rm_current_from_board()
                        self.current_block = rotation_block
                        self.add_current_to_board()
                        return
                if rbh_min > 0:
                    rotation_block = [[i[0] - rbh_min, i[1]] for i in rotation_block]
                    if current_block == rotation_block:
                        rotation_block = [[i[0] + h_min, i[1] + w_min] for i in self.rotations[i][(j + 1) % len(self.rotations[i])]]
                        for k in range(len(rotation_block)):
                            if rotation_block[k][0] not in range(self.ROWS) or rotation_block[k][1] not in range(self.COLS):
                                break
                            if self.board[rotation_block[k][0]][rotation_block[k][1]][0] not in [0, self.current_block_num]:
                                break
                        else:
                            self.rm_current_from_board()
                            self.current_block = rotation_block
                            self.add_current_to_board()
                if rbw_min > 0:
                    rotation_block = [[i[0], i[1] - rbw_min] for i in rotation_block]
                    if current_block == rotation_block:
                        rotation_block = [[i[0] + h_min, i[1] + w_min] for i in self.rotations[i][(j + 1) % len(self.rotations[i])]]
                        for k in range(len(rotation_block)):
                            if rotation_block[k][0] not in range(self.ROWS) or rotation_block[k][1] not in range(self.COLS):
                                break
                            if self.board[rotation_block[k][0]][rotation_block[k][1]][0] not in [0, self.current_block_num]:
                                break
                        else:
                            self.rm_current_from_board()
                            self.current_block = rotation_block
                            self.add_current_to_board()




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
        # random_block = 2
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
            self.rm_current_from_board()
            for i in range(len(self.current_block)):
                self.current_block[i][1] += move
            self.add_current_to_board()




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
            self.rm_current_from_board()
            self.current_block = [[i[0] + 1, i[1]] for i in self.current_block]
            self.add_current_to_board()

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



    def rotate_v1(self):
        found = False
        rotation_block = self.current_block
        h_min = min(i[0] for i in rotation_block)
        h_max = max(i[0] for i in rotation_block)
        w_min = min(i[1] for i in rotation_block)
        w_max = max(i[1] for i in rotation_block)

        # Square, No rotation needed
        if h_max - h_min == 1 and w_max - w_min == 1:
            found = True
            return

        # line
        if h_max - h_min == 3:
            found = True
            rotation_block = [[i[0] + h_min, i[1] + w_min - 1] for i in self.rotations_v1[0][0]]
            for i in range(len(rotation_block)):
                if rotation_block[i][0] not in range(self.ROWS) or rotation_block[i][1] not in range(self.COLS):
                    break
                if self.board[rotation_block[i][0]][rotation_block[i][1]][0] not in [0, self.current_block_num]:
                    break
            else:
                self.rm_current_from_board()
                self.current_block = rotation_block
                self.add_current_to_board()

        elif w_max - w_min == 3:
            found = True
            rotation_block = [[i[0] + h_min - 2, i[1] + w_min] for i in self.rotations_v1[0][1]]
            for i in range(len(rotation_block)):
                if rotation_block[i][0] not in range(self.ROWS) or rotation_block[i][1] not in range(self.COLS):
                    break
                if self.board[rotation_block[i][0]][rotation_block[i][1]][0] not in [0, self.current_block_num]:
                    break
            else:
                self.rm_current_from_board()
                self.current_block = rotation_block
                self.add_current_to_board()


        # everything else
        elif h_max - h_min == 2 or w_max - w_min == 2:
            block = [[i[0] - h_min, i[1] - w_min] for i in self.current_block]
            for index_1 in range(1, len(self.rotations_v1)):
                for index_2 in range(len(self.rotations_v1[index_1])):
                    print(f"i = {index_1}, j = {index_2}")
                    print(self.rotations_v1[index_1][index_2])
                    rotation_block = [[i[0], i[1]] for i in self.rotations_v1[index_1][index_2]]
                    print(rotation_block)
                    rbh_max = max(i[0] for i in rotation_block)
                    rbh_min = min(i[0] for i in rotation_block)
                    rbw_max = max(i[1] for i in rotation_block)
                    rbw_min = min(i[1] for i in rotation_block)

                    if rotation_block == block:
                        found = True
                        rotated_block = [[i[0], i[1]] for i in self.rotations_v1[index_1][(index_2 + 1) % len(self.rotations_v1[index_1])]]
                        for i in range(len(rotated_block)):
                            if self.board[rotated_block[index_1][0] + h_min][rotated_block[index_2][1] + w_min][0] not in [0, self.current_block_num]:
                                break
                        else:
                            self.rm_current_from_board()
                            self.current_block = [[i[0] + h_min, i[1] + w_min] for i in rotated_block]
                            self.add_current_to_board()
                    if rbh_min > 0:
                        if block == [[i[0] - rbh_min, i[1]] for i in rotation_block]:
                            found = True
                    if rbw_min > 0 :
                        if block == [[i[0], i[1] - rbw_min] for i in rotation_block]:
                            found = True
        if not found:
            print(h_max, h_min, w_max, w_min, self.current_block)
            print(*[[i[0] - h_min, i[1] - w_min] for i in self.current_block])
            raise ValueError("Block not found")





    def rm_current_from_board(self):
        for i in range(len(self.current_block)):
            self.board[self.current_block[i][0]][self.current_block[i][1]][0] = 0
            self.board[self.current_block[i][0]][self.current_block[i][1]][1] = 0

    def add_current_to_board(self):
        for i in range(len(self.current_block)):
            self.board[self.current_block[i][0]][self.current_block[i][1]][0] = self.current_block_num
            self.board[self.current_block[i][0]][self.current_block[i][1]][1] = 1

    def soft_drop(self):
        ...

    def hard_drop(self):
        ...

