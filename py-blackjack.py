# Module imports
import random, sys, os, time

# Variables
cards = [
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
    1,
    2,
    3,
    4,
    5,
    6,
    7,
    8,
    9,
    10,
    11,
]
userHand = []
userCount = 0
userBust = False
userStand = False
dealerHand = []
dealerCount = 0
dealerBust = False
dealerStand = False
bal = 0
bet = 0


def clear():
    global userHand, userCount, dealerHand, dealerCount
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Dealer hand: {dealerHand}")
    print(f"Dealer count: {dealerCount}\n")
    print(f"Your hand: {userHand}")
    print(f"Your count: {userCount}")


def main():
    global cards, usedCards, userHand, userCount, userBust, userStand, dealerHand, dealerCount, dealerBust, dealerStand, bal, bet

    # Get bet from user
    print(f"Current balance: {bal}")
    bet = int(input("Enter bet: "))
    if bet > bal or bet <= 0:
        print("Invalid bet.")
    bal = bal - bet

    # Dealing dealer
    for _ in range(2):
        card = random.choice(cards)
        if card == 1 or card == 11:
            if dealerCount >= 11:
                dealerHand.append(1)
                cards.remove(1)
                dealerCount = sum(dealerHand)
            else:
                dealerHand.append(11)
                cards.remove(11)
                dealerCount = sum(dealerHand)
        else:
            dealerHand.append(card)
            cards.remove(card)
        dealerCount = sum(dealerHand)
    print(dealerHand, dealerCount, "\n")

    # Dealing user
    for _ in range(2):
        card = random.choice(cards)
        if card == 1 or card == 11:
            if userCount >= 11:
                userHand.append(1)
                cards.remove(1)
                userCount = sum(userHand)
            else:
                userHand.append(11)
                cards.remove(11)
                userCount = sum(userHand)
        else:
            userHand.append(card)
            cards.remove(card)
        userCount = sum(userHand)
    print(userHand, userCount)

    # User actions
    while not userStand or userBust:
        action = input("(s)tand or (h)it: ")
        if action == "s" or action == "stand":
            userStand = True
        if action == "h" or action == "hit":
            card = random.choice(cards)
            userHand.append(card)

            clear()
            if userCount > 21:
                print("Bust")
                userBust = True
                break
            if userCount == 21:
                print("Blackjack")
                userStand = True

    # Dealer actions
    if dealerCount > 15 and dealerCount < 22:
        clear()
    while dealerCount < 16:
        card = random.choice(cards)
        dealerHand.append(card)
        cards.remove(card)
        dealerCount = sum(dealerHand)
        time.sleep(2)
        clear()
        if dealerCount > 21:
            print("Dealer busts")
            dealerBust = True
            break
        elif dealerCount == 21:
            print("Dealer blackjack")
            dealerStand = True
        clear()
        dealerStand = True

    # Determine winner and give winnings
    if userCount > dealerCount and userBust == False:
        print("You win")
        bal = bal + (bet * 2)
    elif dealerCount > userCount and dealerBust == False:
        print("Dealer wins")
    elif userCount == dealerCount and userBust == False and dealerBust == False:
        print("Split pot")
        bal = bal + bet
    # Reset variables for next game
    userHand = []
    userCount = 0
    dealerHand = []
    dealerCount = 0
    userStand = False
    userBust = False
    dealerStand = False
    dealerBust = False
    time.sleep(3)


# Run games specified times
if len(sys.argv) == 2:
    bal = int(input("Enter starting balance: "))

    for _ in range(int(sys.argv[1])):
        os.system("cls" if os.name == "nt" else "clear")
        main()
else:
    print("Not enough arguments")
    print("Usage: python py-blackjack.py <num of games>")
