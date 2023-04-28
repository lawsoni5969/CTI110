# A program that asks the user to pick a math game
# to either correctly add or subtract numbers.
# 4/27/2023
# CTI-110 P5HW - Math Quiz
# Isaac Lawson
#
import random

while 0 == 0:
    print('\n\nWelcome to Math Quiz')
    print('\nMAIN MENU')
    print('-------------------------')
    print('1. Adding Random Numbers')
    print('2. Subtracting Random Numbers')
    print('3. Exit')
    print('\nPlease choose one of the menu options: ', end='')
    menuChoice = int(input())
    if menuChoice == 1:
        print('')
        randOne = random.randint(1, 300)
        randTwo = random.randint(1, 300)
        correctAns = randOne + randTwo
        print(' ', randOne)
        print('+', randTwo)
        print('——————')
        print('\nEnter answer: ', end='')
        userAns = int(input())
        numGuesses = 0
        while userAns != correctAns:
            if userAns > correctAns:
                print('\nToo High!')
                print('Try Again: ', end='')
                numGuesses = numGuesses + 1
                userAns = int(input())
                continue
            elif userAns < correctAns:
                print('\nToo Low!')
                print('Try Again: ', end='')
                userAns = int(input())
                numGuesses = numGuesses + 1
                continue
        else:
            if userAns == correctAns:
                print('\nCorrect Answer. Congratulations!')
                numGuesses = numGuesses + 1
                print('Number of guesses: ', numGuesses)
                continue
            continue
    elif menuChoice == 2:
        print('')
        randOne = random.randint(0, 300)
        randTwo = random.randint(0, 300)
        while randTwo >= randOne:
            randTwo = random.randint(1, 300)
        correctAns = randOne - randTwo
        print(' ', randOne)
        print('-', randTwo)
        print('——————')
        print('\nEnter answer: ', end='')
        userAns = int(input())
        numGuesses = 0
        while userAns != correctAns:
            if userAns > correctAns:
                print('\nToo High!')
                print('Try Again: ', end='')
                numGuesses = numGuesses + 1
                userAns = int(input())
                continue
            elif userAns < correctAns:
                print('\nToo Low!')
                print('Try Again: ', end='')
                numGuesses = numGuesses + 1
                userAns = int(input())
                continue
        else:
            if userAns == correctAns:
                print('\nCorrect Answer. Congratulations!')
                numGuesses = numGuesses + 1
                print('Number of guesses: ', numGuesses)
                continue
            continue
    elif menuChoice == 3:
        print('\n\nThanks for playing!')
        print('Goodbye')
        break
    else:
        print('Invalid option: Please enter 1, 2, or 3')
        continue
