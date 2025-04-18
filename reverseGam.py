import random
WIDTH=8
HEIGHT=8
def printBoard(board):
        print('   12345678')
        print('  +--------+')
        for i in range(0,len(board)):
                print(i+1,'|',end="")
                for j in range(0,len(board[i])):
                        print(board[i][j],end="")
                print('|',i+1)
        print('  +--------+')
        print('   12345678')
def makeBoard():
        board=[ [' ' for i in range(WIDTH)] for i in range(HEIGHT)]
        return board
def isOnBoard(xstart,ystart):
        return xstart>=0 and xstart<=WIDTH-1 and ystart>=0 and ystart<=HEIGHT-1
def isValidMove(board,tile,xstart,ystart):
        if board[xstart][ystart] != ' ' or not isOnBoard(xstart,ystart):
                return False
        if tile=='X':
                otherTile='O'
        else:
                otherTile='X'
        tilesToFlip=[]
        for xdirection,ydirection in [[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1]]:
                x,y=xstart,ystart
                x+=xdirection
                y+=ydirection
                while isOnBoard(x,y) and board[x][y]==otherTile:
                        x+=xdirection
                        y+=ydirection
                        if isOnBoard(x,y) and board[x][y]==tile:
                                while True:
                                        x-=xdirection
                                        y-=ydirection
                                        if x==xstart and y==ystart:
                                                break
                                        tilesToFlip.append([x,y])
        if len(tilesToFlip)==0:
                return False
        return tilesToFlip
def getBoardCopy(board):
        newBoard=makeBoard()
        for x in range(WIDTH):
                for y in range(HEIGHT):
                        newBoard[x][y]=board[x][y]
        return newBoard
def getBoardWithValidMoves(board,tile):
        boardCopy=getBoardCopy(board)
        for x,y in getValidMoves(boardCopy,tile):
                boardCopy[x][y]='.'
        return boardCopy
def getValidMoves(board,tile):
        validMoves=[]
        for x in range(WIDTH):
                for y in range(HEIGHT):
                        if isValidMove(board,tile,x,y) !=False:
                                validMoves.append([x,y])
        return validMoves
def getScoreOfBoard(board):
        xscore=0
        oscore=0 
        for x in range(WIDTH):
                for y in range(HEIGHT):
                        if board[x][y]=='X':
                                xscore+=1
                        if board[x][y]=='Y':
                                oscore+=1
        return {'X':xscore,'O':oscore}
def enterPlayerTile():
        tile=''
        while not(tile=='X' or tile=='O'):
                print('Do you want to be X or O ? ') 
                tile= input().upper()
        if tile=='X':
                return ['X','O']
        else:
                return ['O','X']
def whoGoesFirst():
        if random.randint(0,1)==0:
                return 'computer'
        else:
                return 'player'

