import random
import sys
import os
import time


def clear():
    os.system("cls" if os.name == "nt" else "clear")


deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10,
        1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
playerHand = []
dealerHand = []
playerCount = 0
dealerCount = 0
playerDone = False
playerBust = False
dealerDone = False
dealerBust = False
playerNatural = False
dealerNatural = False
validBet = False
balance = 0
startingBalance = 0
bet = 0

balance = int(input("Enter starting balance> "))
startingBalance = balance
time.sleep(1)

while len(deck) > 11:
    while not validBet:
        clear()
        bet = int(
            input(f"Enter amount to bet (Current balance: {balance}): "))
        if bet > balance:
            print("Bet cannot be greater than balance")
            time.sleep(2)
        else:
            balance -= bet
            validBet = True

    for x in range(2):
        card = random.choice(deck)
        if card == 1:
            if playerCount <= 10:
                playerHand.append(11)
            else:
                playerHand.append(1)
        else:
            playerHand.append(card)
        deck.remove(card)
        playerCount = sum(playerHand)

    for x in range(2):
        card = random.choice(deck)
        if card == 1:
            if dealerCount <= 10:
                dealerHand.append(11)
            else:
                dealerHand.append(1)
        else:
            dealerHand.append(card)
        deck.remove(card)
        dealerCount = sum(dealerHand)

    print(f"Your hand: {", ".join(map(str, playerHand))
                        }. Current count: {playerCount}")
    print(f"Dealer's hand: {dealerHand[0]
                            }, *. Dealer's Count: {dealerHand[0]}")

    if playerCount == 21:
        print("Player wins with natural 21")
        playerNatural = True
    if dealerCount == 21:
        print("Dealer wins with natural 21")
        dealerNatural = True

    while not playerDone:
        if not playerNatural:
            playerAction = input("(S)tand or (H)it> ").lower()
            if playerAction == "h":
                card = random.choice(deck)
                if card == 1:
                    if playerCount <= 10:
                        playerHand.append(11)
                    else:
                        playerHand.append(1)
                else:
                    playerHand.append(card)
                deck.remove(card)
                playerCount = sum(playerHand)
            clear()

            print(f"Your hand: {", ".join(
                map(str, playerHand))}. Current count: {playerCount}")

            print(f"Dealer's hand: {dealerHand[0]
                                    }, *. Dealer's Count: {dealerHand[0]}")

        if playerCount > 21:
            print("Player busts.")
            playerDone = True
            playerBust = True
        if playerAction == "s" and not dealerNatural:
            playerDone = True
    if not playerBust:
        while dealerCount < 17:
            card = random.choice(deck)
            if card == 1:
                if dealerCount <= 10:
                    dealerHand.append(11)
                else:
                    dealerHand.append(1)
            else:
                dealerHand.append(card)
            deck.remove(card)
            dealerCount = sum(dealerHand)
        clear()

        print(f"Your hand: {", ".join(map(str, playerHand))
                            }. Current count: {playerCount}")

        print(f"Dealer's hand: {", ".join(
            map(str, dealerHand))}. Dealer's Count: {dealerCount}")

        if dealerCount > 21:
            print("Dealer busts.")
            dealerBust = True

    clear()
    print(f"Your hand: {", ".join(map(str, playerHand))
                        }. Current count: {playerCount}")

    print(f"Dealer's hand: {", ".join(
        map(str, dealerHand))}. Dealer's Count: {dealerCount}")

    if playerCount > dealerCount:
        if playerBust:
            print("Dealer wins!")
        else:
            print("Player wins!")
            balance = balance + (bet * 2)
    elif dealerCount > playerCount:
        if dealerBust:
            print("Player wins!")
            balance += bet * 2
        else:
            print("Dealer Wins!")
    if playerCount == dealerCount:
        print("Push!")
        balance += bet
    if balance <= 0:
        print("You ran out of money!")
        deck = []

    playerHand = []
    dealerHand = []
    playerCount = 0
    dealerCount = 0
    playerBust = False
    dealerBust = False
    playerDone = False
    dealerDone = False
    validBet = False
    bet = 0
    time.sleep(3)

print("Cut card reached, shoe is over") if balance > 0 else print(
    "You went bankrupt!")
print(f"Your starting balance was {
      startingBalance} and your ending balance was {balance}")
sys.exit()
