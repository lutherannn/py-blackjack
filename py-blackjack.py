import random, os

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dealerHand = []
userHand = []
dealerCount = 0
userCount = 0
chars = "[],"
dealerStand = False
userStand = False
dealerBust = False
userBust = False

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
    #print(f"Dealer count: {dealerCount}\n")
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
    global userCount, userHand, dealerCount, dealerHand
    if player == "user":
        card = random.choice(cards)
        userHand.append(card)
        userCount = sum(userHand)
        print("Your hand: " + ", ".join(map(str, userHand)))
        print(f"Count: {userCount}")
        if userCount > 21:
            userBust = True
            print("Bust")
        if userCount == 21:
            print("Blackjack")

    if player == "dealer":
        if dealerCount <= 16 and not dealerCount == 21:
            while dealerCount  <= 16:     
                card = random.choice(cards)
                dealerHand.append(card)
                dealerCount = sum(dealerHand)
                print("Dealer hand: " + ", ".join(map(str, dealerHand)))
                print(f"Dealer count: {dealerCount}")
        if dealerCount >= 16 and not dealerCount <= 21:
            dealerStand = True
        if dealerCount > 21:
            dealerBust = True
            dealerCount = 0

def dealerActions():
    global dealerHand, dealerCount, dealerStand, dealerBust
    hit("dealer")
    clear()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"Dealer hand: {dealerHand[0]}, *")
    print("Your hand: " + ", ".join(map(str, userHand)))
    print(f"Count: {userCount}")

def gameLoop():
    global userStand
    while not userStand:
        action = input("(s)tand or (h)it: ")
        if action == "s" or action == "stand":
            userStand = True
        if action == "h" or action == "hit":
            hit("user")
            clear()
    dealerActions()

    if dealerCount > userCount and not dealerBust:
        print("Dealer wins")
        print(f"Dealer count: {dealerCount}")
    if userCount > dealerCount and not userBust:
        print(f"Dealer count: {dealerCount}")
        print("User wins")
    if dealerCount == userCount and not userBust and not dealerBust:
        print("Split pot")
dealDealer()
dealUser()
gameLoop()
