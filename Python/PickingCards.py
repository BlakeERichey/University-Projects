import random as r
cards = [i for i in range(2, 11)] + ["Jack", "Queen", "King", "Ace"]
suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
deck  = r.sample(range(0, 52), 52) #make and shuffle deck
drawn = [ deck.pop( r.choice(range(len(deck))) ) for i in range(2) ] #draw 2 cards from shuffled deck and remove
print(", ".join(str(cards[card%13]) + " of " + suits[int(card/13)] for card in drawn))