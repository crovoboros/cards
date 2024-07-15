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
        str_cards = ""
        for card in self.cards[:-1]:
            str_cards += f"{str(card)}, "
        str_cards += f"and {str(self.cards[-1])}."
        return str_cards
    
    def shuffle(self):
        random.shuffle(self.cards)
    
    def draw(self, amountCards):
        handCards = []
        for i in range(amountCards):
            handCards.append(self.cards[i])
        return Hand(handCards)

# define the standard deck of 52 playing cards
playing_cards = []
for suit in suits:
    for rank in ranks:
        playing_cards.append(Card(rank, suit))

standard_deck = Deck(playing_cards)
#

class Hand:
    def __init__(self, cards : list):
        self.cards = cards
        self.size = len(cards)
        self.count = self.rankCount()

    def rankCount(self) -> dict:
        count = {}
        for card in self.cards:
            count.setdefault(card.rank, 0)
            count[card.rank] += 1
        return count

    def findHighCard(self) -> Card:
        rank = max(self.count)
        for card in self.cards:
            if card.rank == rank:
                return card
    
    def isPair(self) -> bool:
        pass

if __name__ == "__main__":
    standard_deck.shuffle()
    myHand = standard_deck.draw(8)
    for card in myHand.cards:
        print(card)
    print(f"Your High Card is {myHand.findHighCard()}.")