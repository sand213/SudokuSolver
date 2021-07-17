# This is the start of the Sudoku Solver program
# SudokuSolver Functions
import numpy as np
import math 

def main():
    puzzle = CreateBoard()
    displayPuzzle(puzzle)
    boo = input("Would you like this puzzle to be solved? : ")
    if boo == "Yes":
        solveSudoku(puzzle)
    return
    # use this function to execute the code

def solveSudoku(puzzle):
    nums = [1,2,3,4,5,6,7,8,9]
    pos = []
    notSolved = True
    i = 1
    j = 1
    # loops through whole puzzle
    while notSolved and i < 10:
        if j == 10:
            j = 1
            i += 1
        if puzzle[i][j] != 0:
            j += 1
        if puzzle[i][j] == 0:
            pos.append((i,j))
            Solved = False
            index = 0
            num = 0
            while not Solved:
                if num == 9 and (Solved is False):
                    pos.pop(-1)
                    problemSolve(puzzle, i , j, pos)
                    pos.append((i,j))
                    index = 0
                num = nums[index]
                if Allowed(puzzle, i, j, num) == True:
                    puzzle[i][j] = num
                    Solved = True
                    displayPuzzle(puzzle)
                else:
                    index += 1
    return

def problemSolve(puzzle, i, j, pos):
    Solved = False
    nums = [1,2,3,4,5,6,7,8,9]
    i, j = pos[-1]
    numbers = nums[int(puzzle[i][j])::]
    while not Solved:
        if len(numbers) == 0:
            pos.pop(-1)
            puzzle[i][j] = 0
            displayPuzzle(puzzle)
            problemSolve(puzzle, i, j, pos)
            pos.append((i,j))
            numbers = [1,2,3,4,5,6,7,8,9]
        num = numbers.pop(0)
        if Allowed(puzzle, i, j, num) == True:
                puzzle[i][j] = num
                Solved = True
                displayPuzzle(puzzle)
    return

def Allowed(puzzle, i, j, num):
    Allow = True
    for k in range(1,10):
        if (puzzle[i][k] == num) or (puzzle[k][j] == num):
            Allow = False
        rowpos = math.ceil(i / 3)
        colpos = math.ceil(j / 3)
        rows = puzzle[(rowpos * 3) - 2 : (rowpos * 3) + 1]
        for row in rows:
            if num in row[(colpos * 3) - 2 : (colpos * 3) + 1]:
                Allow = False
    return Allow

def displayPuzzle(puzzle):
    for row in range(1,len(puzzle)):
        s = ''
        if ((row - 1) % 3 == 0):
            s+= '- ' * 11
            s+= '\n'
        for col in range(1,len(puzzle) - 1):
            if row != 0 and row != 10:
                if puzzle[row][col] == 10:
                    s+= '| '
                if col % 3 == 0 and col != 9:
                    s+= str(int(puzzle[row][col])) + ' | '
                else:
                    s+= str(int(puzzle[row][col])) + ' '
        print(s)
    return

def CreateBoard():
    # generates the starting sudoku board 
    board = np.zeros((11,11))
    # adds borders to the board
    for i in range(11):
        for j in range(11):
            if i == 0 or i == 10:
                board[i][j] = 10
            if j == 0 or j == 10:
                board[i][j] = 10
    # gets a random position on the board to place a number between 1 and 9
    amount = int(input("Enter how many numbers you want to start of with: "))
    
    pos = []
    while amount > 0:
        row = np.random.randint(low = 1, high = 10)
        col = np.random.randint(low = 1, high = 10)
        num = np.random.randint(low = 1, high = 10)
        match = False
        for pair in pos:
            if pair == [row,col]:
                row = 0
                col = 0
                match = True
                num = 10
        if match == False:
            pos.append([row,col])
        
    
    # check if we can place the number in this position
        rowpos = math.ceil(row / 3)
        colpos = math.ceil(col / 3)
        for j in range((rowpos*3), ((rowpos*3) - 3), -1):
            for k in range((colpos*3),((colpos*3) - 3), -1):
                if board[j][k] == num:
                    num = 0
        for i in range(1,10):
            if board[row][i] == num:
                num = 0
            if board[i][col] == num:
                num = 0
        

        if (match is False) and num != 0:
            board[row][col] = num
            amount = amount - 1
    return board

if __name__ == "__main__":
    main()
