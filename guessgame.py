from random import randint


def generatenum():
    return randint(1, 10)


def playerGuess():
    n = int(input('Enter Your Guess : '))
    return n

num = generatenum()
print('----------------GUESS THE NUMBER-------------------- ')

while(True):
    player=playerGuess()
    if(player==num):
        print('U win :)')
        play_again=input("Enter do u want play again [Y/N]")
        if(play_again=='y'):
            num=generatenum()
            player=None
        else:
            break
    elif(player>num):
        print('Too high')
    else:
        print('Too low')

print('thank u play again')
