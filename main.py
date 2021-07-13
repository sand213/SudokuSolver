# This is the start of the Sudoku Solver program
# SudokuSolver Functions
import numpy as np
def main():
    puzzle = CreateBoard()
    print(puzzle)
    return
    # use this function to execute the code

def CreateBoard():
    # generates the starting sudoku board 
    board = np.zeros((10,10))
    # adds borders to the board
    for i in range(10):
        for j in range(10):
            if i == 0 or i == 9:
                board[i][j] = 10
            if j == 0 or j == 9:
                board[i][j] = 10
    # gets a random position on the board to place a number between 1 and 9
    #row = np.random.randint(low = 1, high = 8)
    #col = np.random.randint(low = 1, high = 8)
    row = 1
    col = 1
    board[1][3] = 1
    board[2][1] = 1
    num = 1
    
    # check if we can place the number in this position
    for i in range(1,9):
        if board[row][i] == num:
            num = 0
        if board[i][col] == num:
            num = 0


    board[row][col] = num
    return board

if __name__ == "__main__":
    main()
