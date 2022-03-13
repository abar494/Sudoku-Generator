# Initialise sudoku board for testing
# 0 represents an empty space
testBoard = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7]
]


def solve(bo):
    # find the first empty slot in the grid
    nearestEmpty = findEmpty(bo)
    # obtain the row and column from the tuple
    # check if the there are no empty slots left, this would mean the sudoku is solved
    if not nearestEmpty:
        return True
    row, col = nearestEmpty
    # iterate through all possible values that the empty slot can have
    for i in range(1, 10):
        # check if the current value is valid within the rules of sudoku
        if isValid(bo, i, (row, col)):
            # if the current value is valid, update the entry until the sudoku is hopefully solved.
            bo[row][col] = i

            # repeat the process with the next empty slot, moving forwards to the next empty slot if
            # this is still valid.
            # If invalid, try the other options and if they fail, reverse it back to an empty slot, and go back to the
            # last empty slot (checking a different value for it).
            # this is called recursive backtracking, a common algorithm for programs such as mazes.
            # this lets us try an option, and go back to try another option if we chose the wrong one.
            if solve(bo):
                # this will return true if the grid gets filled up, returning false if none of the entries in the for
                # loop are valid
                return True

            # if true is not returned, then the current value is not valid and needs to be set back to 0, with another
            # value from the for loop being used.
            bo[row][col] = 0

    # if none of the attempts in teh for loop work, False is returned which takes you to the previous empty slot
    return False
    # this recursive backtracking process continues until the sudoku is filled up, solving it.


def findEmpty(bo):
    # Iterate through board array
    for i in range(len(bo)):
        for j in range(len(bo)):
            # At each square, check if value is 0
            if bo[i][j] == 0:
                # return i (row co-ord) and j (column co-ord)
                return i, j
    # if there are no entries with a value of zero, return None
    return None


def isValid(bo, num, pos):
    # check if it's a valid row
    # get the current row and column of the number you want to check
    row = pos[0]
    col = pos[1]
    for j in range(len(bo)):
        # for that given row, check if any of the other numbers in that row match it
        if (bo[row][j] == num) and (j != col):
            # it is not valid if there is a match (each number in a row should be unique)
            return False

    # check if it's a valid column
    # get the current row and column of the number you want to check
    for i in range(len(bo)):
        # for that given col, check if any of the other numbers in that col match it
        if (bo[i][col] == num) and (i != row):
            # it is not valid if there is a match (each number in a row should be unique)
            return False

    # check if it's a valid box
    # box(0, 0) contains rows 0,1,2 cols 0,1,2. Note these numbers
    # floor divided by 0 all equal 0, hence floor division can categorise your row and col
    # into a specific box.
    boxY = pos[0] // 3
    boxX = pos[1] // 3
    # loop through box to check if the same number exists in the box
    for y in range(boxY*3, boxY*3 + 3):
        for x in range(boxX*3, boxX*3 + 3):
            # for that given box, check if any of the other numbers in that box match it
            if (bo[y][x] == num) and ((y, x) != pos):
                return False
    return True


def printBoard(bo):
    # Set up a nested for loop to traverse the board
    for i in range(len(bo)):

        # each 3x3 box of the sudoku should be separated by lines
        # the % operator lets us check if the index at a given point is divisible by 3
        # letting us know when to place a divider
        if i % 3 == 0 and i != 0:
            # place dividers for rows
            print("- - - - - - - - - - - - - ")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                # place dividers for columns
                print(" | ", end="")
                # end is to prevent new line printing

            if j == 8:
                print(bo[i][j])
                # allow new line at the 8th column to allow new row to print
            else:
                print(str(bo[i][j]) + " ", end="")
                # otherwise we just print our numbers in between the dividers


printBoard(testBoard)
solve(testBoard)
print("\n\n\n")
printBoard(testBoard)

