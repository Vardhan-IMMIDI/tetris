from project import block_boundaries, can_place_block, rm_current_from_board, add_current_to_board


def sample_board():
    return [[[0, 0] for _ in range(5)] for _ in range(5)]


def test_block_boundaries():
    block = [(0, 1), (1, 1), (1, 0), (2, 2)]
    h_max, h_min, w_max, w_min = block_boundaries(block)
    assert (h_max, h_min, w_max, w_min) == (2, 0, 2, 0)


def test_can_place_block_within_bounds():
    board = sample_board()
    block = [(0, 0), (0, 1), (1, 0), (1, 1)]
    current_block_num = 1
    assert can_place_block(block, current_block_num, board, 5, 5) == True


def test_can_place_block_out_of_bounds():
    board = sample_board()
    block = [(0, 0), (0, 1), (5, 0), (1, 1)]
    current_block_num = 1
    assert can_place_block(block, current_block_num, board, 5, 5) == False


def test_can_place_block_collision():
    board = sample_board()
    board[1][1][0] = 2  # Existing block
    block = [(0, 0), (0, 1), (1, 1), (1, 2)]
    current_block_num = 1
    assert can_place_block(block, current_block_num, board, 5, 5) == False


def test_can_place_block_own_block():
    board = sample_board()
    board[1][1][0] = 3
    block = [(0, 0), (0, 1), (1, 1), (1, 2)]
    current_block_num = 3
    assert can_place_block(block, current_block_num, board, 5, 5) == True


def test_rm_current_from_board():
    board = sample_board()
    block = [(0, 0), (0, 1), (1, 0), (1, 1)]
    for r, c in block:
        board[r][c][0] = 9
        board[r][c][1] = 5
    rm_current_from_board(block, board)
    for r, c in block:
        assert board[r][c] == [0, 0]


def test_add_current_to_board():
    board = sample_board()
    block = [(0, 0), (0, 1), (1, 0), (1, 1)]
    current_block_num = 4
    current_block_color = 6
    add_current_to_board(board, block, current_block_num, current_block_color)
    for r, c in block:
        assert board[r][c] == [4, 6]
