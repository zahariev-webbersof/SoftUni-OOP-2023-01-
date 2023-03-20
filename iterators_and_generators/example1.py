def sudoku_solver(board):
    def is_valid(num, row, col):
        # Check row and column for duplicates
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False

        # Check 3x3 square for duplicates
        box_row, box_col = row // 3 * 3, col // 3 * 3
        for i in range(box_row, box_row + 3):
            for j in range(box_col, box_col + 3):
                if board[i][j] == num:
                    return False

        # If no duplicates found, number is valid
        return True

    def get_empty_cell():
        for i in range(9):
            for j in range(9):
                if board[i][j] == 0:
                    return i, j
        return None

    def backtrack():
        empty_cell = get_empty_cell()

        if empty_cell is None:
            return True

        row, col = empty_cell

        for num in range(1, 10):
            if is_valid(num, row, col):
                board[row][col] = num

                if backtrack():
                    return True

                board[row][col] = 0

        return False

    if backtrack():
        return board
    else:
        return None

board = [
    [0, 9, 0, 0, 5, 0, 8, 0, 0],
    [8, 0, 3, 0, 0, 0, 0, 0, 2],
    [0, 4, 0, 3, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 5, 0, 0, 4],
    [6, 0, 8, 7, 0, 0, 5, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 3, 0, 0, 0, 0, 0, 0, 0],
    [5, 0, 7, 6, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 2, 0, 0, 1, 0]
]

for row in sudoku_solver(board):
    print(row)