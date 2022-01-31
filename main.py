############### Blackjack Project #####################

############### Our Blackjack House Rules #####################

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

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return cards[random.randint(0,len(cards))-1]





def calculate_score(card_list):
    score = sum(card_list)
    if len(card_list) == 2 and score == 21:
        return 0
    
    if score > 21 and 11 in card_list:
        card_list.remove(11)
        card_list.append(1)
        score = sum(card_list)
    return score

def compare(user_score,computer_score):
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"
    elif user_score == computer_score:
        return "Game is a DRAW!"
    elif computer_score == 0:
        return "Dealer BLACKJACK, you LOSE"
    elif user_score == 0: 
        return "User BLACKJACK, you WIN!"
    elif user_score > 21:
        return "Bust! Went over 21, you LOSE."
    elif computer_score > 21:
        return "Dealer BUSTS! You WIN."
    elif computer_score > user_score:
        return "Dealer has higher hand. You LOSE"
    elif user_score > computer_score:
        return "You have a higher score. You WIN"
    else:
        return "You lose.."
    
    
def get_score(computer_cards,user_cards):
  user_score = calculate_score(user_cards)
  computer_score = calculate_score(computer_cards)
  return user_score,computer_score

def play_game():
  print(logo)
    
  user_cards = []
  computer_cards = []
  game_over = False
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not game_over:
        
    user_score,computer_score = get_score(computer_cards,user_cards)
    print(f'YOUR CARDS: {user_cards}')
    print(f'Current Score: {calculate_score(user_cards)}')

    if len(computer_cards) == 2:
      print(f'COMPUTER FIRST CARD: {computer_cards[0]}')
    else:
      print(f'COMPUTER CARDS {computer_cards}')
        

    if user_score == 0 or computer_score == 0 or user_score > 21:
      game_over = True
      print("Game Over!")
    else: 
      user_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            
      if user_deal == 'y':
        user_cards.append(deal_card())
      else:
        game_over = True
    
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
        
    print(computer_cards)
        
  print(f'Your final hand: {user_cards}')
  print(f'Your final score is: {calculate_score(user_cards)}')
  print(f'Computer final hand: {computer_cards}')
  print(f'Computer final score is: {calculate_score(computer_cards)}')
    
  print(compare(user_score, computer_score))
    
while input("Do you want to play a game of Blackjack? Type y or n: ") == 'y':
    clear()
    play_game()
          
  
    
          
      
    
