# -*- coding: utf-8 -*-
# @Time       : 2019/7/25 11:03
# @Author     : Philly
# @File       : 21.py
# @Description: 33 lines: "Guess the Number" Game
import random
guesses_made = 0
name = input('Hello! What is your name?\n')

number = random.randint(1, 20)
print('Well, {0}, I am thinking of a number between 1 and 20.'.format(name))

while guesses_made < 6:
    guess = int(input('Take a guess: '))
    guesses_made += 1
    if guess < number:
        print('Your guess is too low.')
    if guess > number:
        print('Your guess is too high.')
    if guess == number:
        break

if guess == number:
    print('Good job, {0}! You guessed my number in {1} guesses!'.format(name, guesses_made))
else:
    print('Nope. The number I was thinking of was {0}'.format(number))


