import random

player_value = 0
dealer_value = 0

bet_money = int(input("How much do you want to bet? "))
dealer_hand = []
player_hand = []

suits = ['♥', '♦', '♣', '♠']

def generate_card():
    value = random.randint(1, 12)
    suit = random.choice(suits)
    return f"{value}{suit}"

dealer_hand.append(generate_card())
print("\033[35mDealer's hand:\033[0m", dealer_hand[0])
dealer_value = sum(int(card[:-1]) for card in dealer_hand)
print("\033[35mValue:\033[0m", dealer_value)

player_hand.append(generate_card())
player_hand.append(generate_card())
print("\033[31mYour hand", *player_hand, sep=", ""\033[0m")
player_value = sum(int(card[:-1]) for card in player_hand)
print("\033[31mValue:\033[0m", player_value)

while True:
    answer = input("Hit or Stand? ").strip().lower()
    if  answer == "hit":
        player_hand.append(generate_card())
        print("\033[31mYour hand", *player_hand, sep=", ""\033[0m")
        player_value = sum(int(card[:-1]) for card in player_hand)
        print("\033[31mValue:\033[0m", player_value)

        if player_value > 21:
            print("You lost!")
            break

    elif answer == "stand":
        print("Standing...")
        break

    else:
        print("Wrong input, `hit` or `stand` only!!!")

while dealer_value < 17:
    dealer_hand.append(generate_card())
    dealer_value = sum(int(card[:-1]) for card in dealer_hand)

print("\nResults:")
print("\033[35mdealers hand\033[0m", *dealer_hand, sep=", ")
print("\033[35mValue:\033[0m", dealer_value)
print("\033[31myour hand\033[0m", *player_hand, sep=", ")
print("\033[31mValue:\033[0m", player_value)

if player_value > 21:
    print("Dealer won! You lost your money... :(")
    bet_money = -bet_money
elif dealer_value > 21 or player_value > dealer_value:
    print("You won!!")
    print("You now have:", bet_money * 2)
elif player_value < dealer_value:
    print("Dealer won :(, lost your money..")
    bet_money =- bet_money
else:
    print("Tied, you get your money back!")