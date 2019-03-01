# -*- coding:UTF-8 -*-
import itertools
import random
import pprint

# Card Difinition
suits = ('Heart', 'Spade', 'Diamond', 'Club')
rank = {'A':11, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, '10':10, 'J':10, 'Q':10, 'K':10}
cards = list(itertools.product(suits, rank))

wallet = -1
bet = -1
p_hand = [] # Player's hand
d_hand = [] # Dealer's hand

while True:
  wallet = int(input('How much money do you HAVE?\t'))
  if wallet>0:
    break
  print('You can\'t start the game unless you have money.')

# for calclate Score
def calcScore(hand):
  sum = 0
  ace = 0
  for card in hand:
    sum += rank[card[1]]
    if card[1] == 'A':
      ace += 1
  while True:
    if sum > 21 and ace > 0:
      sum -= 10
      ace -= 1
      continue
    break
  return sum

# for display each Hands
def showHands():
  print('Player: {0} ( {1} Point)'.format(pprint.pformat(p_hand), str(calcScore(p_hand))))
  print('Dealer: {0} ( {1} Point)'.format(pprint.pformat(d_hand), str(calcScore(d_hand))))

# a body of BlackJack
def game():
  # Initialize Hands
  p_hand.clear()
  d_hand.clear()

  # To shuffle the deck
  stock = random.sample(cards, len(cards))

  print('\n***** Start the Game. *****')
  print('Dealing...')

  # Draw cards
  p_hand.append(stock.pop())
  d_hand.append(stock.pop())
  p_hand.append(stock.pop())
  d_hand.append(stock.pop())

  showHands()

  # Player's turn
  while True:
    if calcScore(p_hand) > 21:
      return -1
    hitFlag = -1
    hitFlag = input('Hit(1) or Stand(0)?\t')
    if hitFlag == '0':
      print('You choose a Stand.')
      break
    elif hitFlag != '1':
      print('Please input 1 or 0')
      continue

    print('You choose a Hit.\nDealing...')
    p_hand.append(stock.pop())
    showHands()

  # Computer's turn
  while True:
    if calcScore(d_hand) > 21:
      return 1
    if calcScore(d_hand) <= 16:
      print('Dealer chooses a Hit.\nDealing...')
      d_hand.append(stock.pop())
      showHands()
    else:
      print('Dealer chooses a Stand.')
      break

  if calcScore(p_hand) < calcScore(d_hand):
    return -1
  elif calcScore(p_hand) > calcScore(d_hand):
    return 1
  else:
    return 0

# Game Driver
while True:

  while True:
    bet = int(input('How much money do you BET?\t'))
    if bet>0 and wallet>=bet:
      break
    elif bet<=0:
      print('You can\'t start the game without a wager.')
    elif wallet<bet:
      print('You don\'t have enough money!')

  result = game()
  if result == -1:
    print('You Lose. The wager was forfeited.')
    wallet -= bet
    print('Wallet: {0} (-{1})'.format(str(wallet), str(bet)))
  elif result == 1:
    print('You Win! You got a prize.')
    wallet += bet
    print('Wallet: {0} (+{1})'.format(str(wallet), str(bet)))
  else:
    print('It\'s a Draw. We will return a wager.')
    print('Wallet: {0} (+-0)'.format(str(wallet)))

  if wallet <= 0:
    print('Your wallet is empty.')
    print('***** GAME OVER *****')
    break
  else:
    if input('Continue?(Y/n)\t') == 'n':
      print('Bye!')
      break
