# Sudoku Puzzle solver using backtracking and recursion

sudoku = [
    [0, 0, 5, 0, 0, 2, 1, 3, 8],
    [0, 4, 0, 8, 0, 0, 0, 2, 9],
    [0, 0, 0, 0, 0, 1, 4, 5, 0],
    [0, 5, 3, 2, 1, 0, 0, 0, 0],
    [0, 0, 7, 0, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 6, 5, 2, 8, 0],
    [0, 2, 1, 9, 0, 0, 0, 0, 0],
    [4, 3, 0, 0, 0, 6, 0, 7, 0],
    [5, 7, 8, 1, 0, 0, 9, 0, 0]
]


def printBoard(board):
    # prints the board out
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - - - ")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end=" ")

    return True


def check(y, x, n):
    # y is row , x is column, n is number inserted
    for i in range(9):
        if sudoku[y][i] == n:
            return False
    for i in range(9):
        if sudoku[i][x] == n:
            return False
    # check the squares to determine if n is already present
    x0 = (x // 3) * 3
    y0 = (y // 3) * 3

    for i in range(0, 3):
        for j in range(0, 3):
            if sudoku[y0 + i][x0 + j] == n:
                return False
    return True


def solution(sudoku):
    # two for loops for the row and col [y][x]
    for y in range(9):
        for x in range(9):
            if sudoku[y][x] == 0:
                for n in range(1, 10):
                    if check(y, x, n):
                        # backtracking and recursion, set value to 0 if it doesnt work
                        sudoku[y][x] = n
                        solution(sudoku)
                        sudoku[y][x] = 0
                return
    printBoard(sudoku)


printBoard(sudoku)
print("\n Here is the solution: \n")
solution(sudoku)
