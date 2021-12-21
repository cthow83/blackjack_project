class Player:
    # Potential to add further information in the future, such as more player details or
    # a wager amount
    def __init__(self, name):
        self.name = name
        self.hand = []
        self.total = 0
