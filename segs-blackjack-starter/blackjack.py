from src.deck import Deck
import random

def play():
    print('Hello, potential future BBC developer!')  # execution starts here! delete this line and add your game code.
    deck = Deck()
    hand = []
    total = 0

    total = twist(hand, deck)
    total = twist(hand, deck)
    if (total < 21):
        print(total)
    else:
        print("BLACKJACK!!!!")
    total = twist(hand, deck)
    options(total)
    total = twist(hand, deck)
    options(total)


def return_card(deck):
    a = random.randint(0, 51)
    return deck.cards[a]

def twist(hand, deck):
    card = return_card(deck)
    hand.append(card)
    print(hand)
    if ('A' in hand):
        hand.remove('A')
        if('A' in hand):            #handles multiple Ace situation (only 1 can be max value)
            hand.remove('A')
            hand.append(1)
        total = sum(hand)
        if (total < 11):
            total += 11
        else:
            total += 1
        hand.append('A')
    else:
        total = (sum(hand))
    return total

def options(total):
    if (total <= 21):
        print(total)
    else:
        print(str(total) + " BUST!!!")
if __name__ == '__main__':
    play()
