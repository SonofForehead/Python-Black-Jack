import random

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "Q": 10, "J": 11, "K": 12}
category = ["♣️", "♦️", "♥️", "♠️"]

dealers_hand = []
players_hand = []

for _ in range(1):
    card = random.choice(list(cards))
    dealers_hand.append(card)

for _ in range(2):
    card = random.choice(list(cards))
    players_hand.append(card)

dealers_hand_values = [cards[card] for card in dealers_hand]
players_hand_values = [cards[card] for card in players_hand]

dealers_total_value = sum(dealers_hand_values)
players_total_value = sum(players_hand_values)

money_bet = int(input("How much do you want to bet?: "))

print("Dealer's Hand:", [(random.choice(category), card) for card in dealers_hand])
print("Value:", dealers_hand_values)
print("Your Hand:", [(random.choice(category), card) for card in players_hand])
print("Value:", players_hand_values)

stand_hit = int(input("Do you want to stand (0), or hit? (1): "))

if stand_hit == 1 :
    print("Hit!")
elif stand_hit == 0 :
    print("Standing!")