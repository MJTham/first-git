############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

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

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.

from art import logo
import random
print(logo)
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
  """
  deal_card() is the game initial function
  1. random the player card
  2. random the computer card
  3. place both player & computer cards into dictionary
  4. return result
  """
  users_card = [random.choice(cards), random.choice(cards)]
  #computer_card = [random.choice(cards)]
  computer_card = [11]
  users_dictionary = {
    "Player": users_card, 
    "Computer": computer_card,
  }
  return f"{users_dictionary}"

def add_card(dictionary, ask):
  """
  steps in add card(dictionary) function
  1. get the dictionary from deal card
  2. convert the dictionary list into tuple
  3. read the player current card
  4. random a number in card above
  5. append the number into player tuple list
  6. return the result for new player set
  """
  all_card = list(dictionary.items())
  player_card = tuple(all_card[0])
  continue_add = True
  player_card_list = player_card[1]
  #print(f"just --- {type(card_list)}")
  if ask == "no":
    new_player_set = player_card[1]
  else:
    while continue_add:    
      #print(f"first item - {player_card}")
      new_player_card = random.choice(cards)
      #print(f"card list - {card_list}")
      player_card_list.append(new_player_card)
      new_player_set = player_card_list
      print(f"new player set - {new_player_set}")
      for i, j in enumerate(player_card_list):
        if j == 11:
          ask_11 = input("want to change 11 to 1? \n")

          if ask_11 == "y":
            player_card_list[i] = 1
            print(f"player_card_list in Ace - {player_card_list}")
      
      ask_add = input("add another card? y/n \n")
      
      if ask_add == "y":
        continue_add = True
      else:
        continue_add = False
  
  print(f"new player set - {new_player_set}")
  return new_player_set

def computer_game(dictionary):
  """
  computer_game(dictionary) is the function to help computer play the black jack
  steps
  1. retrieve the data from computer obtained in deal_card() function
  2. sum the number computer get
  3. if computer's card get lower than 17, loop the random number of card until his card bigger than 17
  4. return computer card result
  """
  #print(f"computer_game starts")
  all_card = list(dictionary.items())
  computer_card = tuple(all_card[1])
  #print(f"{computer_card}")
  computer_card_list = computer_card[1]
  computer_get = 0
  computer_get = sum(computer_card_list)
  print(f"computer get a total of - {computer_get}")

  if computer_get == 21 and len(computer_card_list) == 2:
    return "Black Jack"
  else:  
    for i, j in enumerate(computer_card_list):
      if j == 11:
          computer_card_list[i] = 1
  #enough_sum = False
  #while not enough_sum:
  for i in range(1,5):
    if computer_get < 17:
        new_computer_card = random.choice(cards)
        computer_card_list.append(new_computer_card)
        new_computer_set = computer_card_list

        if sum(new_computer_set) < 17:
          #enough_sum = False
          i += 1
        else:
          #enough_sum = True
          break
    else:
      new_computer_set = computer_card[1]
      break
      #enough_sum = True

  print(f"new computer set - {new_computer_set}")
  return new_computer_set
  
def compare_card(player_set, computer_set):
  """
  compare_card(player_set, computer_set) will start to identify the winner by checking between computer & player card
  1. retrieve the card from player_set, computer_set
  2. check the sum
  3. if player not more than 21 continue check
  4. if player = computer then return draw
  5. if player > computer then player win
  6. if player < computer then computer win
  """
  print(f"compare starts - player set = {player_set} computer set = {computer_set}")
  
  sum_player = 0
  sum_computer = 0
  sum_player = sum(player_set)
  sum_computer = sum(computer_set)

  if sum_player <= 21:
    if sum_player == sum_computer:
      return f"both of you get the same score: {sum_player}, this is a draw game"
    elif sum_player > sum_computer:
      return f"player get the score: {sum_player}, player win"
    elif sum_player < sum_computer:
      if sum_computer > 21:
        return "computer's card bigger than 21, computer lose"
      return f"computer get the score: {sum_computer}, computer win"
  else:
    return "player's card bigger than 21, player lose"

deal_card_output = {}

import ast
deal_card_output = ast.literal_eval(deal_card())
print(f"deal card - {deal_card_output}")

ask = input("Do you want to add additional card? y or n \n").lower()
if ask == "y":
  player_set = add_card(deal_card_output,"yes")
elif ask == "n":
  player_set = add_card(deal_card_output,"no")

computer_set = computer_game(deal_card_output)
compare_result = compare_card(player_set, computer_set)

print(f"{compare_result}")
#try_again = input("Play again?").lower()
