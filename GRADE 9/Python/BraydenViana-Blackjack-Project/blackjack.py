import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

playerTotal = random.choice(cards) + random.choice(cards)
computerTotal = random.choice(cards) + random.choice(cards)

print('player total is', playerTotal)
print('computer total is', computerTotal)