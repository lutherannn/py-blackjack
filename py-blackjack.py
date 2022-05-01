import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dealerHand = []
userHand = []
dealerCount = 0
userCount = 0
chars = "[],"
dealerStand = False
userStand = False

def dealDealer():
    global dealerCount
    global dealerHand
    for _ in range(2):
        card = random.choice(cards)
        if card in [1, 11]:
            if dealerCount < 11:
                dealerHand.append(11)
            else:
                dealerHand.append(1)
        else:
            dealerHand.append(card)
        dealerCount = sum(dealerHand)
    print(f"Dealer hand: {dealerHand[0]}, *")
    print(f"Dealer count: {dealerCount}\n")
def dealUser():
    global userCount
    global userHand
    for _ in range(2):
        card = random.choice(cards)
        if card in [1, 11]:
            if userCount < 12 and userCount != 11:
                userHand.append(11)
            else:
                userHand.append(1)
        else:
            userHand.append(card)
        userCount = sum(userHand)
    print("Your hand: " + ", ".join(map(str, userHand)))
    print(f"Your count: {userCount}\n")
def hit(player):
    global userCount, userHand, dealerCount, dealerHand, userDone
    if player == "user":
        card = random.choice(cards)
        userHand.append(card)
        userCount = sum(userHand)
        print("Your hand: " + ", ".join(map(str, userHand)))
        print(f"Count: {userCount}")
        if userCount > 21:
            userDone = True
            print("Bust")
        if userCount == 21:
            print("Blackjack")

    if player == "dealer":
        card = random.choice(cards)
        dealerHand.append(card)
        dealerCount = sum(dealerHand)
        if dealerCount >= 16 and dealerCount <= 21:
            print("Dealer Stands")
        if dealerCount == 21:
            print("Blackjack")
            dealerStand = True
        else:
            print("Dealer Busts")
            dealerStand = True
        print("Dealer hand: " + ", ".join(map(str, dealerHand)))
        print(f"Dealer count: {dealerCount}")


def dealerActions():
    global dealerHand, dealerCount, dealerStand
    while not dealerStand:
        if dealerCount < 16:
            hit("dealer")
        else:
            dealerStand = True

def gameLoop():
    global userStand, dealerStand
    while not userStand:
        action = input("(s)tand or (h)it: ")
        if action == "s" or action == "stand":
            userStand = True
            dealerActions()
        if action == "h" or action == "hit":
            hit("user")
dealDealer()
dealUser()
gameLoop()
