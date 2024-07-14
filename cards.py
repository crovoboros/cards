# Ace will be defined as 14
import random
ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
suits = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

def isFaceCard(rank : int) -> bool:
    return rank in [11, 12, 13]

def nameRank(rank : int) -> str:
    match rank:
        case 11:
            return "Jack"
        case 12:
            return "Queen"
        case 13:
            return "King"
        case 14:
            return "Ace"
        case _:
            return str(rank)

class Card:
    def __init__(self, rank : int, suit : str):
        self.rankName = nameRank(rank)
        self.rank = rank
        self.suit = suit
        self.isFaceCard = isFaceCard(self.rank)

    def __str__(self) -> str:
        return f"{self.rankName} of {self.suit}"

class Deck:
    def __init__(self, cards : list):
        self.cards = cards
    
    def __str__(self) -> str:
        return f"{self.cards}"

# define the standard deck of 52 playing cards
playing_cards = []
for suit in suits:
    for rank in ranks:
        playing_cards.append(Card(rank, suit))

standard_deck = Deck(playing_cards)

for card in standard_deck.cards:
    print(card)
#

class Hand:
    def __init__(self, cards : list):
        self.cards = cards
        self.size = len(cards)

    def findHighCard() -> Card:
        pass
    
    def isPair() -> bool:
        pass