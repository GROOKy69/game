import random
def drawBoard(board):
    print(board[7]+' | '+board[8]+' | '+board[9])
    print('_________')
    print(board[4]+' | '+board[5]+' | '+board[6])
    print('_________')
    print(board[1]+' | '+board[2]+' | '+board[3])
def inputPlayLetter():
    letter=''
    while not(letter=='X' or letter=='Y'):
        letter=input("Do you want to be X or O?").upper()
        if letter=='X':
           return['X','O']
        else:
            return['O','X'] 
def whoGoesFirst():
    if random.randint(0,1)==0:
        return 'computer'
    else:
        return 'player'
def makeMove(board,letter,move):
    board[move]=letter
def isWinner(bo,le):
    return (bo[7]==le and bo[8]==le and bo[9])==le or (bo[4]==le and bo[5]==le and bo[6]==le) or (bo[1]==le and bo[2]==le and bo[3]==le ) or (bo[1]==le and bo[4]==le and bo[7]==le ) or (bo[2]==le and bo[5]==le and bo[8]==le )or (bo[3]==le and bo[6]==le and bo[9]==le )or (bo[7]==le and bo[5]==le and bo[3]==le ) or (bo[1]==le and bo[5]==le and bo[9]==le)
def getBoardCopy(board):
    boardCopy=[]
    for i in board:
        boardCopy.append(i)
    return boardCopy
def isSpaceFree(board,move):
    return board[move]==' '
def getPlayerMove(board):
    move=' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        move=input('What is your next move ?(1-9)')
    return int(move)
def chooseRandomMoveFromList(board,moveList):
        possibleMoves=[]
        for i in moveList:
            if isSpaceFree(board,i):
                possibleMoves.append(i)
        if possibleMoves!=1:
            return random.choice(possibleMoves)
        else:
            return None
def getComputerMove(board,computerLetter):
    if computerLetter=='x':
        playLetter='o'
    else:
        playLetter='x'
    for i in range(1,10):
        boardCopy=getBoardCopy(board)
        makeMove(boardCopy,computerLetter,i)
        if isWinner(boardCopy,computerLetter):
            return i
    for i in range(1,10):
        boardCopy=getBoardCopy(board)
        makeMove(boardCopy,playLetter,i)
        if isWinner(boardCopy,playLetter):
            return i 
    move=chooseRandomMoveFromList(board,[1,3,7,9])
    if move!=None:
        return move
    if isSpaceFree(board,5):
        return 5
    return chooseRandomMoveFromList(board,[2,4,6,8])
def isBoardFull(board):
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False

    return True
print('Welcome to Tic Tac Toe')
while True:
    theBoard=[' ']*10
    playerLetter, computerLetter =inputPlayLetter()
    turn =whoGoesFirst()
    print('The '+turn+'will go first')
    gameIsPlaying=True
    while gameIsPlaying:
        if turn=='player':
            drawBoard(theBoard)
            move=getPlayerMove(theBoard)
            makeMove(theBoard,playerLetter,move)
            if isWinner(theBoard,playerLetter):
                drawBoard(theBoard)
                print("you have won,congratulations")
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print("You have a tie")
                    gameIsPlaying=False
                else:
                    turn="computer"
        else:
            move=getComputerMove(theBoard,computerLetter)
            makeMove(theBoard,computerLetter,move)
            if isWinner(theBoard,computerLetter):
                drawBoard(theBoard)
                print("Computer have won")
                gameIsPlaying=False
            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('you have a tie')
                    gameIsPlaying=False
                else:
                    turn='player'

    if input("Do you want to play again?(yes/no)").lower().startswith('y'):
        continue
    else:
        print("Have a nice day:)")
        break