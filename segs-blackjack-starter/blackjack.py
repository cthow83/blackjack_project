from src.deck import Deck
import random


def play():
    print('Welcome to BBC Blackjack!')
    print('For your convenience, a jack, queen or king will be automatically converted')
    print('into its equivalent value. The value of an Ace will be either 11 or 1 depending')
    print('the current value of your hand')
    print()
    scores = []
    print("How many players are there?")
    players = input()
    deck = Deck()

    for i in range(int(players)):

        hand = []
        stick = False

        twist(hand, deck)
        total = twist(hand, deck)
        print("Player " + str(i + 1) + ", Your hand is", end=" ")
        print(hand)
        print("It is currently worth " + str(total))
        if total == 21:
            print("BLACKJACK!!!!")
        else:
            while total < 21 and stick == False:
                option = options()
                if option == 1:
                    total = twist(hand, deck)
                    print("Player " + str(i + 1) + ", Your hand is", end=" ")
                    print(hand)
                    print("It is currently worth " + str(total))
                else:
                    stick = True
        evaluate(i, total, scores)

    print("Scores:")
    for i in range(int(players)):
        print("Player " + str(i + 1) + " scored " + str(scores[i]))


def return_card(deck):
    size = len(deck.cards) - 1
    print(size)
    a = random.randint(0, size)
    removed = deck.cards.pop(a)
    return removed


def twist(hand, deck):
    card = return_card(deck)
    print("You have been dealt a " + str(card))

    if card == 'King':
        value = 10
    elif card == "Queen":
        value = 10
    elif card == "Jack":
        value = 10
    else:
        value = card

    hand.append(value)
    if 'A' in hand:
        hand.remove('A')
        if 'A' in hand:  # handles multiple Ace situation (only 1 can be max value)
            hand.remove('A')
            hand.append(1)
        total = sum(hand)
        if total < 11:
            total += 11
        else:
            total += 1
        hand.append('A')
    else:
        total = (sum(hand))
    return total


def stick(player, total):
    print("Player " + str(player) + ". You score " + str(total) + ".")


def options():
    print("Would you like to hit or stand?")
    print("For hit Press 1")
    print("For stand Press 2")
    return int(input())


def evaluate(player, total, scores):
    print("Player " + str(player + 1) + ". Your total is " + str(total))
    if total <= 21:
        scores.append(total)
        print("Good Luck")
    else:
        scores.append(0)
        print("YOU ARE BUST. You lose")
    print("Press enter to end your turn")
    input()


if __name__ == '__main__':
    play()
