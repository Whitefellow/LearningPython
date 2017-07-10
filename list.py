def collatz(number):
    if number % 2 == 0:
       result = number // 2
    if number % 2 == 1:
        result = 3 * number + 1

    while result == 1:
        print(result)
        break
    while result != 1:
        print(result)
        number = result
        return collatz(number)
print('enter a number: ')
try:
    number = int(input())
    collatz(number)
except ValueError:
    print('You must enter and interger type.')
