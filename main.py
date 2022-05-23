#tic tac toe 



board = [" " for i in range(10)]

def insertLetter (letter, pos): 
    board[pos] = letter


def spaceisFree(pos):
    return board[pos] == " "

def printBoard(board):
    print("------------")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("------------")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("------------")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("------------")

def isWinner(bo, le):
    return (bo[7]  == le and bo[8] == le and bo [9] == le) or (bo[4]  == le and bo[5] == le and bo [6] == le) or (bo[1]  == le and bo[2] == le and bo [3] == le) or    (bo[1]  == le and bo[4] == le and bo [7] == le) or (bo[2]  == le and bo[5] == le and bo [8] == le) or (bo[3]  == le and bo[6] == le and bo [9] == le) or (bo[1]  == le and bo[5] == le and bo [9] == le) or (bo[3]  == le and bo[5] == le and bo [7] == le)


def playerMove():
    run = True 
    while run:
        move = input("select 1-9 to place X: ")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceisFree(move):
                    run = False
                    insertLetter("X", move)
                else:
                    print("pos taken please type another number between 1-9")
            else:
                print("please type a number")
        except:
            print("pleae type a number!")



def compMove():
    posMove = [i for i, letter in enumerate(board) if letter == " " and i != 0]
    move = 0

    for let in ["O", "X"]: 
        for x in posMove:
            boardCopy = board[:]
            boardCopy[x] = let
            if isWinner (boardCopy, let):
                move = x 
                return move

    openCorner = []
    for x in posMove:
        if x in [1,3,7,9]:
            openCorner.append(x)
        
    if len(openCorner) > 0:
        move = selectRandom(openCorner)
        return move

    if 5 in posMove:
        move = 5
        return move

    openEdge = []
    for x in posMove:
        if x in [2,4,6,8]:
            openEdge.append(x)
        
    if len(openEdge) > 0:
        move = selectRandom(openEdge)
            
    return move

def selectRandom(li):
    import random

    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]



def isBoardFull(board):
    if board.count(" ") > 1:
        return False
    else:
        return True

def main():
    print("welcome to tic tac toe select 1-9")
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, "O")):
            playerMove()
            printBoard(board)
        else:
            print("sorry computer won this time")
            break

        if not(isWinner(board, "X")):
            move = compMove()
            if move == 0:
                print("tie game")
            else:
                insertLetter("O", move)
                print("computer placed an O in position", move , ":")
                printBoard(board)
            
        else:
            print("you won")
            break


    


    if isBoardFull(board):
        print("tie game")
     
    

main()























