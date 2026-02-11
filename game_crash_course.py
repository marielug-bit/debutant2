# Build a fun Number Guessing Game in Python! 🐍 
# The program picks a random number between 1-100, 
# and you have 7 attempts to guess it. 
# Get hints if you’re too high 📈 or too low 📉! 
# Perfect for practicing loops 🔄, conditionals ❓, and user input ⌨️.

import random as r

def game(number):
    count = 1
    guessing_number = int(input('Guess which number I chose between 1 and 100?'))
    while count <= 6 and guessing_number != number : 
        if guessing_number < number :
            print('The number you chose is too low')
            guessing_number = int(input('Try again'))
            count +=1
        elif guessing_number > number :
            print ('The number you chose it too high')
            guessing_number = int(input('Try again'))
            count+=1
    if guessing_number == number :
        print(f'Congrats! you find it, the correct number is {number}')
    if count == 7:
        print(f'You do not have any chance to guess anymore, the number was{number}')

number = r.randint(1,100)
game(number)








