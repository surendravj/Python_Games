from random import randint

def computer_choice():
    a=['rock','paper','scissor']
    return a[randint(0,2)]



def player_choice():
    choice=input("Enter Your Move : ")
    return choice


def who_wins():
    if(computer_wins==player_wins):
        print('Its a tie break')
    elif(computer_wins<player_wins):
        print('U won Hurray :)')
    else:
        print('U lost :(')

computer_wins=0
player_wins=0

def game_started():
    global computer_wins
    global player_wins
    state=3
    while(state>0):
        print(f"Computer Score [{computer_wins}]  Player Score [{player_wins}]")
        playerChoice=player_choice()
        computerChoice=computer_choice()
        if(computerChoice==playerChoice):
            print('Its tie')
        elif(computerChoice=='rock' and playerChoice=='scissor'):
            computer_wins+=1
        elif(computerChoice=='paper' and playerChoice=='rock'):
            computer_wins+=1
        elif(computerChoice=='scissor' and playerChoice=='paper'):
            computer_wins+=1
        elif(playerChoice=='rock' and computerChoice=='scissor'):
            player_wins+=1
        elif(playerChoice=='paper' and computerChoice=='rock'):
            player_wins+=1
        elif(playerChoice=='scissor' and computerChoice=='paper'):
            player_wins+=1
        else:
            print('something  went wrong :(')
            break
        state-=1
        


def startGame():
    game_started()
    who_wins()