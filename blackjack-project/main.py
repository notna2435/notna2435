############### Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import random
from replit import clear
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
  return cards[random.randint(0, len(cards) - 1)]


def calculate_score(card_list):
  if sum(card_list) == 21:
    return 0
  elif sum(card_list) > 21:
    for card in card_list:
      if card == 11:
        card_list.remove(card)
        card_list.append(1)
  return sum(card_list)


def blackjack():
  user_cards = []
  computer_cards = []
  for i in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  end_game = False
  if user_score > 21 or computer_score == 0 or user_score == 0:
    end_game = True
  print(f"Your cards: {user_cards}, current score: {user_score}\n computer's first card: {computer_cards[0]}")
 
  while end_game == False:
    hit = input("Do you want to draw another card? Type 'y' or 'n'. ")
    if hit == 'y':
      user_cards.append(deal_card())
      user_score = calculate_score(user_cards)
      print(f"Your cards: {user_cards}, current score: {user_score}")
      if user_score >= 21:
        end_game = True
    else:
      break
  
 
  if end_game == False:
    while computer_score < 17:
      computer_cards.append(deal_card())
      computer_score = calculate_score(computer_cards)
    print(f"dealer's cards: {computer_cards}, dealer's score: {computer_score}")
      

  def compare(user_score, computer_score):
    if user_score == computer_score:
      print("It's a draw.")
    elif computer_score == 0:
      print("The dealer got blackjack. You lose.")
    elif user_score == 0:
      print("Blackjack! You win.")
    elif user_score > 21:
      print("Bust! You lose.")
    elif computer_score > 21:
      print("The dealer busted! You win.")
    elif user_score > computer_score:
      print("You win!")
    else:
      print("You lose.")

  compare(user_score, computer_score)
    
play = input("Do you want to play a game of blackjack? Type 'y' or 'n'. ")
if play == 'y':
  print(logo)
  blackjack()
  restart = input("Do you want to play again? Type 'yes' or 'no'. ")
  while restart == 'yes':
    clear()
    print(logo)
    blackjack()
    restart = input("Do you want to play again? Type 'yes' or 'no'. ")
  
