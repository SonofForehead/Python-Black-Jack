import random

while True:
    suits = ['♥', '♦', '♣', '♠']

    def generate_card():
        value = random.randint(1, 12)
        suit = random.choice(suits)
        return f"{value}{suit}"

    def calculate_hand_value(hand):
        return sum(int(card[:-1]) for card in hand)

    def play_turn(player_hand):
        while True:
            answer = input("Hit or Stand? ").strip().lower()
            if answer == "hit":
                player_hand.append(generate_card())
                print("\033[31mYour hand:\033[0m", *player_hand)
                player_value = calculate_hand_value(player_hand)
                print("\033[31mValue:\033[0m", player_value)

                if player_value > 21:
                    print("You lost, sad :(")
                    return player_value
            elif answer == "stand":
                print("Standing...")
                return calculate_hand_value(player_hand)
            else:
                print("Wrong input, `hit` or `stand` only!!!")

    def main():
        player_value = 0
        dealer_value = 0

        bet_money = int(input("How much do you want to bet? "))
        dealer_hand = []
        player_hand = []

        dealer_hand.append(generate_card())
        print("\033[35mDealer's hand:\033[0m", dealer_hand[0])
        dealer_value = calculate_hand_value(dealer_hand)
        print("\033[35mValue:\033[0m", dealer_value)

        player_hand.append(generate_card())
        player_hand.append(generate_card())
        print("\033[31mYour hand:\033[0m", *player_hand)
        player_value = calculate_hand_value(player_hand)
        print("\033[31mValue\033[0m", player_value)

        player_value = play_turn(player_hand)

        if player_value <= 21:
            while dealer_value < 17:
                dealer_hand.append(generate_card())
                dealer_value = calculate_hand_value(dealer_hand)

        print("\nResults:")
        print("\033[35mDealer's hand:\033[0m", *dealer_hand)
        print("\033[35mValue:\033[0m", dealer_value)
        print("\033[31mYour hand:\033[0m", *player_hand)
        print("\033[31mValue:\033[0m", player_value)

        if player_value > 21:
            print("Dealer won! You lost your money... :(")
        elif dealer_value > 21 or player_value > dealer_value:
            print("You won!!")
            print("You now have:", bet_money * 2)
        elif player_value < dealer_value:
            print("Dealer won :(, lost your money..")
        else:
            print("Tied, you get your money back!")

    if __name__ == "__main__":
        main()

    answer = str(input("Restart?('Yes'/'No') ")).strip().lower()

    if answer == "no":
        break
    elif answer == "yes":
        continue