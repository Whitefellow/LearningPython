import random


# Function deffinitions

def munch():
    roll = random.randint(0, 1)
    if roll == 1:
        print('you win')
    else:
        print('tough cookies stool pusher, you rolled a zero')
    print('would you like to play again?')
    getInput('yes')

    
def getInput(expected):
    if input() == expected:
        munch()
    else:
        print('Thank you for playing flip.py, see you next time!')



# Scripting code


print('Type roll when ready.')
getInput('roll')
