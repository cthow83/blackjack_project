from src.deck import Deck
from src.player import Player
import random


def play():
    # Introduction & set-up
    print('Welcome to BBC Blackjack!')
    print('For your convenience, a jack, queen or king will be automatically converted')
    print('into its equivalent value. The value of an Ace will be either 11 or 1 depending')
    print('the current value of your hand')
    print()
    print("How many players are there? Max is 5")
    # players = int(input())
    while True:
        try:
            players = int(input())
            while not players > 1 or not players < 5:
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

        print(player.name + "'s Turn")

        stick = False

        twist(player, deck)
        twist(player, deck)
        evaluate(player)

        if player.total == 21:
            print("BLACKJACK!!!!")
        else:
            while player.total < 21 and stick == False:
                option = options()
                if option == 1:
                    twist(player, deck)
                    evaluate(player)
                else:
                    stick = True
        if player.total > 21:
            player.total = 0

        print(player.name + " scored " + str(player.total))
        print("Press enter to end your turn")
        input()

    # Dealers turn
    print()
    print("Dealers Turn")

    dealer = Player("Dealer")
    twist(dealer, deck)
    twist(dealer, deck)
    while dealer.total < 17:
        twist(dealer, deck)
    if dealer.total <= 21:
        print("Dealer has " + str(dealer.total))
    else:
        print("Dealer has bust.")
        dealer.total = 0

    # Summary of game
    print()
    print("Scores:")
    for player in playerlist:
        print(player.name + " scored " + str(player.total))
    print(dealer.name + " scored " + str(dealer.total))


def return_card(deck):
    size = len(deck.cards) - 1
    a = random.randint(0, size)
    removed = deck.cards.pop(a)
    return removed


def twist(player, deck):
    card = return_card(deck)
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


def stick(player, total):
    print("Player " + str(player) + ". You score " + str(total) + ".")


def options():
    print("Would you like to hit or stand?")
    print("For hit Press 1")
    print("For stand Press 2")
    return int(input())


def evaluate(player):
    if player.total <= 21:
        print(player.name + ", Your hand is", end=" ")
        print(player.hand)
        print("It is currently worth " + str(player.total))
    else:
        print("YOU ARE BUST. You lose")


if __name__ == '__main__':
    play()
