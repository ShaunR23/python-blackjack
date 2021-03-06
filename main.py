import random

start_game = input("Do you want to play a game of blackjack? type 'y' or 'n'")
is_game_over = False

user_cards = []
cpu_cards = []


def deal_card():
  """Return a random card from the deck"""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  random.shuffle(cards)
  return cards.pop(0)


for x in range(2):
  user_cards.append(deal_card())
  cpu_cards.append(deal_card())

print(user_cards)
print(cpu_cards)


def calculate_score(cards):
  """Takes a list of cards and calculates the sum of the list of cards"""
  if 11 in user_cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)

  if len(cards) == 2 and sum(cards) == 21:
    return 0
  return sum(cards)

def compare(user_score, cpu_score):
  #Bug fix. If you and the computer are both over, you lose.
  if user_score > 21 and cpu_score > 21:
    return "You went over. You lose 😤"
  if user_score == cpu_score:
    return "Draw 🙃"
  elif cpu_score == 0:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 0:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif cpu_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > cpu_score:
    return "You win 😃"
  else:
    return "You lose 😤"



while not is_game_over:
  user_score = calculate_score(user_cards)
  cpu_score = calculate_score(cpu_cards)

  print(f"Your cards: {user_cards}, Current Score: {user_score}")
  print(f"Computer first card: {cpu_cards[0]}")

  if user_score == 0 or cpu_score == 0 or user_score > 21:
    is_game_over = True

  else:
    draw = input("Would you like to draw another card? 'y' or 'n'")
    if draw == 'y':
      user_cards.append(deal_card())
    else:
      is_game_over = True
while cpu_score != 0 or cpu_score < 17:
  cpu_cards.append(deal_card())
  cpu_score = calculate_score(cpu_cards)

print(f"   Your final hand: {user_cards}, final score: {user_score}")
print(f"   Computer's final hand: {cpu_cards}, final score: {cpu_score}")
print(compare(user_score, cpu_score))

def play_game(): 
    user_cards = []
    computer_cards = []
    is_game_over = False

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    play_game()
