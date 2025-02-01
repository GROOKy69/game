import random
import math
import sys
def tenS():
    space=' '*4
    for i in range(1,6):
        space+=' '*9+str(i)
    return space
def xAxis():
    space=' '*3
    for i in range(0,6):
        for j in range(0,10):
            space+=str(j)
    return space
def board():
    board=[]
    for y in range(15):
        row=[]
        for x in range(60):
            if random.randint(0,1)==0:
                row.append('`')
            else:
                row.append('~')
        board.append(row)
    return board
def displayOcean(ocean):
    print()
    print(tenS())
    print(xAxis())
    for i in range(15):
        if i<10:
            print(' %s %s %s'%(i,''.join(ocean[i]),i))
        else:
            print('%s %s %s'%(i,''.join(ocean[i]),i))
    print(xAxis())
    print(tenS())
    print()
def isInputCorrect(inp):
    return len(inp.split())==2 and inp.split()[0].isdigit() and inp.split()[1].isdigit()
def isInputProper(inp):
    return    0<=int(inp.split()[0])<=59  and 0<=int(inp.split()[1])<=14

def takeInput(option=1):
    if option==1:
        print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
        inp=input()
        if inp=='quit':
            sys.exit()
        while not(isInputCorrect(inp) and isInputProper(inp)):
            print('Please insert x between 0 and 59,y between 0 and 14 ')
            inp=input()
    else:
        print('You have inserted this x and y position before!')
        print('Where do you want to drop the next sonar device? (0-59 0-14) (or type quit)')
        inp=input()
        if inp=='quit':
            sys.exit()
        while not(isInputCorrect(inp) and isInputProper(inp)):
            print('Please insert x between 0 and 59,y between 0 and 14 ')
            inp=input()
    return int(inp.split()[0]), int(inp.split()[1])
def isInputRepeated(y,x,guesses):
    for guess in guesses:
        if(guess[0]==y and guess[1]==x):
            return True
def result(treasureNumber,sonarNumber,distance,x='',y=''):
    if distance==0:
         print("You have found the  treasure,which was at %s %s "%(x,y))
    else:
        print('Treasure detected at a distance of %s from the sonar device.'%(distance))
    print('You have %s sonar device(s) left. %s treasure chest(s) remaining.'%(sonarNumber,treasureNumber))
    

def treasureGen():
    xArray=[i for i in range(60)]
    yArray=[i for i in range(15)]
    random.shuffle(xArray)
    random.shuffle( yArray)
    xTreasure=xArray[0:3]
    yTreasure=yArray[0:3]
    treasure=[[xTreasure[i],yTreasure[i]] for i in range(3)]
    return treasure

def main():    
    while True:
        sonarNumber=20
        treasureNumber=3
        guesses=[['','','']]
        treasureArray=treasureGen()
        ocean=board()
        while  sonarNumber>0:
            print(treasureArray)
            x,y=takeInput()
            while isInputRepeated(y,x,guesses):
                x,y=takeInput(2)
            distance=100
            for xT,yT in treasureArray:
                newDistance=math.floor(math.sqrt((x-xT)**2+(y-yT)**2))
                if newDistance<distance:
                    distance=newDistance
            if distance==0:
                treasureNumber-=1
                sonarNumber-=1
                for treasure in treasureArray:
                    if (treasure[0]==x and treasure[1]==y):
                        treasureArray.remove(treasure)
                guesses.append([y,x,''])
                for guess in guesses:
                    if (guess[2]).isdigit():
                        ocean[guess[0]][guess[1]]='X'
                ocean[y][x]='T'
                result(treasureNumber,sonarNumber,distance,x,y)
            elif (distance<10):
                sonarNumber-=1
                guesses.append([y,x,str(distance)])
                ocean[y][x]=str(distance)
                result(treasureNumber,sonarNumber,distance)

            else:
                sonarNumber-=1
                guesses.append([y,x,'X'])
                ocean[y][x]='X'
                result(treasureNumber,sonarNumber,distance)

            displayOcean(ocean)
            if treasureNumber==0:
                print("You have won, congratulations!")
                break
        if sonarNumber==0:
            print('You have lost ,but you can try it again:)')
            print('The treasures were at:')
            for x,y in treasureArray:
                print('   x: %s y: %s'%(x,y))
        if not(input("Do you want to play again? (yes/no)").lower().startswith('y')):
            break
        else:
            continue  
if True:
    main()