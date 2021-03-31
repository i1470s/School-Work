import random

def ace():
	if newCard == 11:
		valueAce = input('Do you want your ace to count as one? Y/N ')
		if valueAce.lower() == 'y':
			newCard = 1
		return newCard

def dealCard():
	cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
	card = random.choice(cards)
	return card

def playGame():
	newCard = dealCard()
	print('Player Card is : ', newCard)
	if newCard == 11:
		newCard = ace()
	playerTotal = newCard
	newCard = dealCard()
	print('Player Card is: ', newCard)
	if newCard == 11:
		newCard = ace()
	playerTotal = newCard + playerTotal
	print('Player Total is: ', playerTotal)


	newCard = dealCard()
	print('Dealer Card is: ', newCard)
	dealerTotal = newCard

	Stay = False
	while playerTotal < 22 and not Stay:
		answer = input('Do you want another card? Y/N: ')
		if answer.lower() == 'y':
			newCard = dealCard()
			print('Player card is: ', newCard)
			playerTotal = newCard + playerTotal
			print('Player Total is: ', playerTotal)
		else:
			Stay = True

	if playerTotal < 22:
		while dealerTotal < 17:
			newCard = dealCard()
			print('Dealer Card is: ', newCard)
			dealerTotal = newCard + dealerTotal
			print('Dealer Total is: ', dealerTotal)

			if newCard == 11 and ((dealerTotal + 11) > 21):
				newCard = 1
			dealerTotal = newCard + dealerTotal
			print('Dealer Total: ', dealerTotal)

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

def main():
	playMore = True
	while playMore:
		playGame()
		playMore = False
		again = input('Do you want to play again? Y/N ')
		if again.lower() == 'y':
			playMore = True
		else:
			playMore = False
main()