# Day 11 - Blackjack

from itertools import filterfalse
from art import logo
import random, sys

cardDeck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10 ,10, 10, 10]

def DealHand():
    hand = []
    for i in range(2):
        AddCard(hand)
    return hand

def AddCard(hand):
    hand.append(random.choice(cardDeck))

def DisplayFullScore(hand, owner):
    print(f"{owner}'s' cards are:", end = " ")
    for card in hand:
        print(card, end = " ")
    print(f". {owner}'s Score: {sum(hand)}.")


def DisplayFirstCardOnly(hand, owner):
    print(f"{owner}'s first card is {hand[0]}.")
  

def CalculateScores():
    global dealerHand
    global playerHand
    global dealerScore
    global playerScore

    playerScore = sum(playerHand)
    dealerScore = sum(dealerHand)
    if dealerScore > 21 and 11 in dealerHand:
        CheckAcesLow(dealerHand)
        dealerHand = sum(dealerHand)
    if playerScore > 21 and 11 in playerHand:
        CheckAcesLow(playerHand)
        playerScore = sum(playerHand)
        
    if  playerScore > 21:
        LoseOver21()
    elif playerScore == 21 and dealerScore == 21:
        Draw()
    elif dealerScore == 21:
        LoseDealer21()
    elif playerScore == 21:
        Win21()
    else:
        return True

def CheckAcesLow(hand):
      while 11 in hand:
            hand.remove(11)
            hand.append(1)
      print("ACES LOW!")


def HitOrStick():
    takeAnotherCard = input("(H)it or (S)tick? ").lower()
    if takeAnotherCard == "h":
        AddCard(playerHand)
        DisplayFullScore(playerHand, "Player")
        if CalculateScores():
            HitOrStick()
    else:
        CalculateFinalScores()
    
def CalculateFinalScores():
    global dealerHand
    global playerHand
    global dealerScore
    global playerScore

    DisplayFullScore(playerHand, "Player")
    DisplayFullScore(dealerHand, "Dealer")
    DealerPlays()

    if dealerScore > 21:
        WinDealerBust()
    elif dealerScore == 21:
        LoseDealer21()
    elif dealerScore == playerScore:
        Draw()
    elif dealerScore > playerScore:
        LoseUnder21()
    else:
        WinUnder21()

def DealerPlays():
    global dealerHand
    global dealerScore
    
    while dealerScore < 17:
        print("Dealer takes another card...")
        AddCard(dealerHand)
        dealerScore = sum(dealerHand)
        DisplayFullScore(dealerHand, "Dealer")

def Win21():
    print(f"Congratulations! You won with a Blackjack!")

def WinDealerBust():
    print(f"Congratulations! You won, as the dealer went bust with a score of {dealerScore}!")

def LoseOver21():
    print(f"You're bust, with a score of {playerScore}!")

def LoseDealer21():
    print("Unfortunately, the dealer got a Blackjack!")

def WinUnder21():
    print(f"Your score of {playerScore} wins against the dealer's {dealerScore}!")

def LoseUnder21():
    print(f"The dealer wins, scoring {dealerScore} against your {playerScore}.")

def Draw():
    print(f"It's a draw! You both scored {dealerScore}!")

   
        

print(logo)

wantToPlay = True
while wantToPlay:
    playerScore = 0
    dealerScore = 0


    playerHand = DealHand()
    dealerHand = DealHand()

    DisplayFullScore(playerHand, "Player")
    DisplayFirstCardOnly(dealerHand, "Dealer")

    _ = CalculateScores()
    if playerScore != 21 and dealerScore != 21:
        HitOrStick()
    wantToPlayPrompt = input("Want to play? (Y) or (N): ")
    if wantToPlayPrompt.lower() == "n":
        wantToPlay = False
        print("Thanks for playing!")
   

        
 