import random

def dealCard():
	cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	card = random.choice(cards)
	return card

newCard = dealCard()
print('Player Card is :', newCard)
playerTotal = newCard
newCard = dealCard()
print('Player Card is:', newCard)
playerTotal = newCard + playerTotal
print('PLyaer Total is:', playerTotal)


newCard = dealCard()
print('Dealer Card is:', newCard)
dealerTotal = newCard
newCard = dealCard()
print('Dealer Card is:', newCard)
dealerTotal = newCard + dealerTotal
print('Dealer Total is:', dealerTotal)


if playerTotal > 21:
	print('sorry you lose!')

elif dealerTotal > 21:
	print('you win, dealer busts!')

elif playerTotal == dealerTotal:
	print('draw')

elif playerTotal > dealerTotal:
	print('you win')
else:
	print('dealer wins')