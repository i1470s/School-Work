import random

cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]

playerTotal = random.choice(cards) + random.choice(cards)
computerTotal = random.choice(cards) + random.choice(cards)

print('player total is', playerTotal)
print('computer total is', computerTotal)

if playerTotal > 21:
	print('sorry you lose!')

elif computerTotal > 21:
	print('you win, dealer busts!')

elif playerTotal == computerTotal:
	print('draw')

elif playerTotal > computerTotal:
	print('you win')
else:
	print('dealer wins')