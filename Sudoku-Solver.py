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


def findEmpty(bo):

    # Iterate through board array
    for i in range(len(bo)):
        for j in range(len(bo)):
            # At each square, check if value is 0
            if bo[i][j] == 0:
                # return i (row co-ord) and j (column co-ord)
                return i, j

    return None


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
