import random

user = int(input('choose a number: '))
computer = random.randint(1, 10)

if user == computer:
    print('Congratulations, you guessed right!')
else:
    print('Sorry you didn\'t guess')

