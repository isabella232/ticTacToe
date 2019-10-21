import random

def assignPlayer():
    ''' returns a tuple of player, computer, success
        where success is True if player is either X or O
        returns tuple of 2 empty strings and False otherwise
    '''
    player = input("Pick X or O: ")
    if (player == "X"):
        return "X", "O", True
    elif (player == "O"):
        return "O", "X", True
    else:
        return "", "", False
 
    
def checkGameOver(boardData, freeSpaces):
    ''' returns the winner if there is one or " " if a tie
        return False otherwise
    '''
    winner = checkWin(boardData)

    # X or O won
    if (winner):
        print(winner + " won!")
        return True

    # Tie
    if (len(freeSpaces) == 0):
        print("Stalemate!")
        return True

    # Game not finished
    return False


def checkWin(boardData):
    ''' checks for row, column, or diagonal wins in that order
        return the winner if there is one or False if none
    '''
    # check row win
    for row in boardData:
        # remove duplicates
        testRowWin = set(row)
        
        # check if any player chose this row and entire row was the same
        if (" " not in testRowWin and len(testRowWin) == 1):
            return row[0] # return winner

    # check column win
    for colNum in range(0, 3):
        # remove duplicates
        testColWin = set(row[colNum] for row in boardData)

        # check if any player chose this col and entire col was the same
        if (" " not in testColWin and len(testColWin) == 1):
            return row[colNum] # return winner

    # check diagonal win
    if (not boardData[1][1] == " " and # check center is not " "
        # check \ win
        ((boardData[0][0] == boardData[1][1] == boardData[2][2]) or
        # check / win
        (boardData[2][0] == boardData[0][2] == boardData[1][1]))):
        return boardData[1][1]
    
    return False


def moveComp(boardData, freeSpaces, compChar):
    row, col = random.choice(freeSpaces)
    print("Computer: " + str(row) + " " + str(col))
    boardData[row - 1][col - 1] = compChar
    freeSpaces.remove((row, col))


def moveUser(boardData, freeSpaces, userChar):
    userPos = input("Player: ")
    if (len(userPos.split()) != 2):
        print("Enter two values separated by a space")
        return False

    row, col = userPos.split()
    if (not row.isdigit() or not col.isdigit()):
        print("Enter numerical values")
        return False
    
    row, col = [int(row), int(col)]
    if ((row, col) not in freeSpaces):
        print("Invalid choice!")
        return False
    boardData[row - 1][col - 1] = userChar
    freeSpaces.remove((row, col))
    return True

            
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
    random.seed(3)
    
    # empty board data of which squares are taken by which players
    boardData = [[" "," "," "],[" "," "," "],[" "," "," "]]
    while (True):
        userChar, compChar, success = assignPlayer()
        if (success):
            break

    # create list of board's empty coordinates
    freeSpaces = [(n, m) for n in range(1,4) for m in range(1, 4)]
    turn = 1
    print("How to Play:")
    print("Enter a row 1-3 and a column 1-3 separated by a space when it is your turn!")
    input("Press enter to start!")
    while (True):
        # print the board
        printBoard(boardData)
        
        # check for winner or tie
        if (checkGameOver(boardData, freeSpaces)):
            break

        # move
        if (turn % 2 == 0):
            moveComp(boardData, freeSpaces, compChar)
            turn += 1
        else:
            if (moveUser(boardData, freeSpaces, userChar)):
                turn += 1

main()
