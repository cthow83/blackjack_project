from src.deck import Deck
from src.player import Player
import random
import time


def play():
    # Introduction & set-up
    print('Welcome to BBC Blackjack!')
    time.sleep(1)
    print('For your convenience, a jack, queen or king will be automatically converted')
    print('into its equivalent value. The value of an Ace will be either 11 or 1 depending')
    print('the current value of your hand')
    print()
    time.sleep(1)
    print("How many players are there? Max is 5")
    # players = int(input())
    while True:
        try:
            players = int(input())
            while players < 1 or players > 5:
                print("Please select a number between 1 and 5")
                players = int(input())
            break
        except ValueError:
            print("Invalid entry. Please start again")

    print()
    deck = Deck()
    playerlist = []

    for i in range(players):
        playerlist.append(Player("Player " + str(i + 1)))

    # Play the game
    for player in playerlist:

        time.sleep(1)
        print(player.name + "'s Turn")

        stick = False

        twist(player, deck)
        twist(player, deck)
        evaluate(player)

        if player.total == 21:
            time.sleep(1)
            print("BLACKJACK!!!!")
        else:
            while player.total < 21 and stick == False:
                option = options()
                if option == 1:
                    twist(player, deck)
                    evaluate(player)
                else:
                    # stand(player)     #Not required in current version. see stand() method below
                    stick = True
        if player.total > 21:
            player.total = 0

        time.sleep(1)
        print(player.name + " scored " + str(player.total))
        time.sleep(1)
        print("Press enter to end your turn")
        input()

    # Dealers turn
    print()
    time.sleep(1)
    print("Dealers Turn")

    dealer = Player("Dealer")
    twist(dealer, deck)
    twist(dealer, deck)
    while dealer.total < 17:
        twist(dealer, deck)
    if dealer.total <= 21:
        time.sleep(1)
        print("Dealer has " + str(dealer.total))
    else:
        time.sleep(1)
        print("Dealer has bust.")
        dealer.total = 0

    # Summary of game
    print()
    time.sleep(1)
    print("Scores:")
    for player in playerlist:
        time.sleep(1)
        print(player.name + " scored " + str(player.total))
    time.sleep(1)
    print(dealer.name + " scored " + str(dealer.total))


def return_card(deck):
    size = len(deck.cards) - 1
    a = random.randint(0, size)
    removed = deck.cards.pop(a)
    return removed


def twist(player, deck):
    card = return_card(deck)
    time.sleep(1)
    print(player.name + " has been dealt a " + str(card))

    if card == 'King':
        value = 10
    elif card == "Queen":
        value = 10
    elif card == "Jack":
        value = 10
    else:
        value = card

    player.hand.append(value)
    if 'A' in player.hand:
        player.hand.remove('A')
        if 'A' in player.hand:  # handles multiple Ace situation (only 1 can be max value)
            player.hand.remove('A')
            player.hand.append(1)
        player.total = sum(player.hand)
        if player.total < 11:
            player.total += 11
        else:
            player.total += 1
        player.hand.append('A')
    else:
        player.total = (sum(player.hand))


# Not currently needed as doesnt add anything to model. Left in for future development
# def stand(player):
#     # No more cards, no alteration in total.
#     print(player.name + ". You score " + str(player.total) + ".")


def options():
    # Provides suitable options for current game set up
    # Possible to add future options here for rule variations (splits, etc)
    time.sleep(1)
    print("Would you like to hit or stand?")
    print("For hit Press 1")
    print("For stand Press 2")
    return int(input())


def evaluate(player):
    # Evaluates the total score of the player when called.
    # Prints score to terminal
    if player.total <= 21:
        time.sleep(1)
        print(player.name + ", Your hand is", end=" ")
        print(player.hand)
        time.sleep(1)
        print("It is currently worth " + str(player.total))
    else:
        time.sleep(1)
        print("YOU ARE BUST. You lose")


if __name__ == '__main__':
    play()
