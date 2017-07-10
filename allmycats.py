myPets = ['zophie', 'pooka', 'fatty']
print('enter a pet name:')
name = input()
if  name not in mypets:
    print('I do not have a pet name ' + name)
else:
    print(name + ' is my pet.')
