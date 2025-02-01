import os
from pathlib import Path 
letters=''.join([chr(i) for i in range(65,91)])
letters+=''.join([chr(i) for i in range(97,123)])
def getMode():
    mode=None
    while mode not in ['encrypt' , 'e','decrypt','d']:
        mode=input("Do you wish to encrypt or decrypt message ?").lower()
    return mode 
def getMessage():
    print("Enter your message:")
    return input()
def getKey():
    while True:
        key=input('insert a key greater than 0 : ')
        if key.isdigit() and  int(key)>0:
            return int(key)
def main():
    while True:
        mode=getMode()
        message=getMessage()
        key=getKey()
        translate=''
        if 'e'==mode or 'encrypt'==mode:
            for letter in message:
                index=letters.find(letter)
                if index==-1:
                    translate+=letter
                else:
                    
                    translate+=letters[((key+index)%52)]
        else:
            for letter in message:
                index=letters.find(letter)
                if index==-1:
                    translate+=letter
                else:
                    if(key>=index):
                        translate+=letters[(52-((abs(index-key))%52))]
                    else:
                        translate+=letters[(index-key)]
        print('The translated text is %s'%(translate))
        if(not(input('do you want to translate again? (yes/no)').lower().startswith('y'))):
            break
if True:
    main()