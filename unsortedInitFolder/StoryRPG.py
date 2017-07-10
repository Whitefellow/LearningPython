import random

print('What is thy name?')
name = input()
print('What is thy assistant?')
name2 = input()

print('Welcome ' + name + ' and ' + name2)

nameHp = 10
nameHp2 = 5
foe = 25

print('A foe appears brandishing a knife')

def attack():
    global foe, nameHp, nameHp2
    foe = foe - random.randint(0, 5)
    nameHp = nameHp - random.randint(0, 2)
    nameHp2 = nameHp2 - random.randint(0, 1)
if nameHp < 0:
        print('You are dead.')
if nameHp2 < 0:
        print('Your friend has died.')
while foe >= 0:
    if nameHp < 0:
        print('You are dead.')
    if nameHp2 < 0:
        print('Your friend has died.')
    if foe > 0:
        print('What would you like to do?')
        if input('') == 'attack':
              attack()
              print (foe, nameHp, nameHp2)
              continue
    elif foe < 0:
        print('Victory')
    elif nameHp and nameHp2 <= 0:
        print('You have failed')
        end
