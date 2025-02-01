import random
MAX_GUESS=10
def generateNumber():
    li=list(range(10))
    f=shuffleAndChoose(li)
    li.append(0)
    s=shuffleAndChoose(li)
    t=shuffleAndChoose(li)
    return  str(f)+str(s)+str(t)
def shuffleAndChoose(li ):
    random.shuffle(li)
    v=random.choice(li)
    li.remove(v)
    return v
def isFalseInput(guess):
    li=[str(i) for i in range(0,10)]
    if len(guess)==3:
        for l in guess:
            if l not in li:
                return True
        return False
    else:
        return True 
def inputGuess():
    inpute=''
    c=0
    while isFalseInput(inpute):
        if c!=0:
            print("You have inserted an incorrect input! \n")
        c+=1
        inpute=input("Please insert a 3-digit number ")
    return inpute 
while True:
    originalNumber=generateNumber()
    answer=[]
    counter=0
    while True:
        counter+=1
        if counter>MAX_GUESS:
            print(f'You have lost, the number was {originalNumber}')
            break
        guessNumber=inputGuess()
        if guessNumber==originalNumber:
            print("Congrats, You have won!")
            break
        for o in range(3):
            if(originalNumber[o]==guessNumber[o]):
                answer.append('fermi')
            else:
                for g in range(3):
                    if(originalNumber[o]==guessNumber[g]):
                        answer+=['pico']
        if len(answer)==0:
            answer.append('bagel')
        random.shuffle(answer)
        print(' '.join(answer))
        answer.clear(
        )
    if not input('Do you want to play again (yes/no)').lower().startswith('y'):
        break

