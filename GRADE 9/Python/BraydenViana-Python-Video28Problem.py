import random

target_num, number = random.randint(1, 10), 0

while target_num != number:
   
    number = int(input('Guess a number between 1 and 10: '))

print('Well guessed!')