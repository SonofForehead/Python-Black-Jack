import random
from random import shuffle

cards = {"A": 11, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "Q": 10,  "J": 11, "K": 12}
category = ["♣️", "♦️", "♥️", "♠️"]

money_bet = int(input("How much do you want to bet?: \n"))

print("Dealers Hand: ", random.choice(category), random.choice(list(cards)))

