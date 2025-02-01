import random
import math
def printBoard(board):
    print(f'{board[7]} | {board[8]} | {board[9]}')
    print('---'*3)
    print(f'{board[4]} | {board[5]} | {board[6]}')
    print('---'*3)
    print(f'{board[1]} | {board[2]} | {board[3]}')
def doYouWantToBeXOrO():
    userXOrO=input('Do you want to be x or o ? ')
    while not(userXOrO=='x' or userXOrO=='o'):
        userXOrO=input('Do you want to be x or o ? ')
    if(userXOrO=='x'):
        return 'x','o'
    else:
        return 'o','x'
def whoGoesFirst():
    if random.randint(0,1)==0:
        print('Computer will go first')
        return 0
    else:
        print("You will go first")
        return 1
def makeMove(move,board,xOrO):
    board[move]=xOrO
def makeBoard():
    board=[' ' for _ in range(0,10) ]
    board[0]=''
    return board
def makeBoardCopy(board):
    boardCopy=['']
    for element in board:
        boardCopy+=element
    return boardCopy
def isMoveOnTheBoard(move,board):
    if(board[move]==' '):
        return True
    else:
        return False
def getMove(board):
    movesList=[str(i) for i in range(1,10)]
    move=input('What is your next move? (1-9)')
    while(not (move in movesList  and isMoveOnTheBoard(int(move),board))  ):
        print('Your move is not rigth!')
        move=input('What is your next move? (1-9)')
    return int(move)

def isWinner(xOrO,board):
    return board[1]==xOrO and board[2]==xOrO and board[3]==xOrO or board[4]==xOrO and board[5]==xOrO and board[6]==xOrO or board[7]==xOrO and board[8]==xOrO and board[9]==xOrO or board[1]==xOrO and board[4]==xOrO and board[7]==xOrO or board[2]==xOrO and board[5]==xOrO and board[8]==xOrO or board[3]==xOrO and board[6]==xOrO and board[9]==xOrO or board[1]==xOrO and board[5]==xOrO and board[9]==xOrO or board[3]==xOrO and board[5]==xOrO and board[7]==xOrO
def isBoardFull(board):
    for i in range(1,10):
        if board[i]==' ':
            return False
    return True 
def possibleMoveGen(board):
    possibleMovesList=[]
    for i in range(1,10):
        if board[i]==' ':
            possibleMovesList.append(i)
    return possibleMovesList
def returnComputerMove(xOrO,board):
    possibleMoves=possibleMoveGen(board)
    for possibleMove in possibleMoves:
        copyBoard=makeBoardCopy(board)
        makeMove(possibleMove,copyBoard,xOrO)
        if(isWinner(xOrO,copyBoard)):
            return possibleMove
    if xOrO=='x':
        opponentXorO='o'
    else:
        opponentXorO='x'
    for possibleMove in possibleMoves:
        copyBoard=makeBoardCopy(board)
        makeMove(possibleMove,copyBoard,opponentXorO)
        if(isWinner(opponentXorO,copyBoard)):
            return possibleMove
    if(board[5]==' '):
        return 5
    cornerMoves='2 4 6 8'.split()
    for cornerMove in cornerMoves:
        if(board[int(cornerMove)]==' '):
            return int(cornerMove)
    return possibleMoves[random.randint(0,len(possibleMoves)-1)]
def main():
    while  True:
        board=makeBoard()
        printBoard(board)
        userXOrO,computerXOrO= doYouWantToBeXOrO()
        userOrComputer=whoGoesFirst()
        while True:
            if userOrComputer==1 :
                move=getMove(board)
                print('move type:',type(move))
                makeMove(move,board,userXOrO)
                printBoard(board)
                if(isWinner(userXOrO,board)):
                    print("You have won congratulations")
                    break
                if(isBoardFull(board)):
                    print('You have a tie')
                    break
                userOrComputer=0
            else :
                move=returnComputerMove(computerXOrO,board)
                makeMove(move,board,computerXOrO)
                print("It's computer! Hi opponent")
                printBoard(board)
                if(isWinner(computerXOrO,board)):
                    print("Computer has won !")
                    break
                if(isBoardFull(board)):
                    print('You have a tie')
                    break
                userOrComputer=1
        if not(input('Do you want to play again ? (yes/no)').lower().startswith('y')):
            break
if True:
    main()