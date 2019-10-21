import random

def assignPlayer():
    ''' returns a tuple of player, computer, success
        where success is True if player is either X or O
        returns tuple of 2 empty strings and False otherwise
    '''
    # TODO
    return "", "", True
 
    
def gameOver(boardData, freeSpaces):
    ''' returns the winner if there is one or " " if a tie
        return False otherwise
    '''
    # TODO
    return False


def win(boardData):
    ''' checks for row, column, or diagonal wins in that order
        return the winner if there is one or False if none
    '''
    # boardData for testing
    # [[" ", "O", "X"], ["O", "X", "O"], ["X", " ", " "]] -> diag / win
    # [["X", "O", " "], ["O", "X", "O"], [" ", " ", "X"]] -> diag \ win
    # [["X", "O", " "], ["X", "X", "O"], ["X", "O", " "]] -> column 1 win
    # [["X", "O", "X"], ["O", "O", "O"], ["X", " ", " "]] -> row 2 win
    # [[" ", "O", "X"], ["O", "X", "O"], [" ", "X", " "]] -> False no win
    # [["X", "O", " "], ["O", "X", "O"], ["X", " ", " "]] -> False no win

    return False
        
def printBoard(boardData):
    ''' prints out
        1|2|3
        - - -
        4|5|6
        - - -
        7|8|9
        where the numbers are where X's and O's can be
    '''
    rowNum = 1
    colNum = 1
    horizWallWidth = 6
    for row in boardData:
        for col in row:
            if (colNum % 3 == 0):
                end = "\n"
            else:
                end = "|"
            print(col, end=end)
            
            colNum += 1
        if (rowNum < 3):
            print("- - -")
        rowNum += 1
    print("\n")


def main():
    boardData = [[" "," "," "],[" "," "," "],[" "," "," "]]
    
    # assign player character

    # create list of board's empty coordinates
    freeSpaces = [(n, m) for n in range(1,4) for m in range(1, 4)]
    turn = 1

    while (True):
        # print the board

        # check for winner or tie

        # move (turns should alternate between player and computer)

        break # TODO placeholder to prevent infinite loop (remove this when done)
