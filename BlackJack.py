# This project milestone2
# Do a game named BackJack
# Game rules: https://en.wikipedia.org/wiki/Blackjack

import random

# suits is a variant of Cards
suits = ("Hearts","Diamonds","Spades","Clubs")
#Rank 
ranks =("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Aces")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Aces":11}


# Declare Card Class
class Card:
    
    
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    def __str__(self):
        return self.rank + " " + self.suit
    
# Declare Deck Class
class Deck:
    
    #Init a deck with default 
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
     
    # Deck all cards            
    def __str__(self):
        dect_comp = ''
        for card in self.deck:
            dect_comp +='\n' + card.__str__()
        return dect_comp
     
     #Make a randon card position           
    def shuffle(self):
        random.shuffle(self.deck)
    
    # Deal card    
    def deal(self):
        return self.deck.pop();  
    
test_Deck = Deck()
test_Deck.shuffle()
print(test_Deck)

print("Deal: ",test_Deck.deal())
print("Deal: ",test_Deck.deal())



