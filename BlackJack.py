# This project milestone2
# Do a game named BackJack
# Game rules: https://en.wikipedia.org/wiki/Blackjack

import random

# suits is a variant of Cards
suits = ("Hearts","Diamonds","Spades","Clubs")
#Rank 
ranks =("Two","Three","Four","Five","Six","Seven","Eight","Nine","Ten","Jack","Queen","King","Aces")
values = {"Two":2,"Three":3,"Four":4,"Five":5,"Six":6,"Seven":7,"Eight":8,"Nine":9,"Ten":10,"Jack":10,"Queen":10,"King":10,"Aces":11}

playing = True

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
        return self.deck.pop()
    
# test_Deck = Deck()
# test_Deck.shuffle()
# print(test_Deck)

# print("Deal: ",test_Deck.deal())
# print("Deal: ",test_Deck.deal())

class Hand:
    
    def __init__(self):
        self.card = []
        self.value = 0
        self.aces = 0
    
    def add_card(self,card):
        self.card.append(card)
        
        self.value += values[card.rank]
        
        if card.rank == "Aces":
           self.aces += 1
    
    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces   -= 1
            
            
class Chip:
    
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def winbet(self):
        self.total += self.bet
        
    def losebet(self):
        self.total -= self.bet
        
def take_bet(chips):
    
    while True:
        try:
            chips.bet = int(input("Bet : "))
        except ValueError:
            print("Sorry !! Invalid value !")
        else:
            if chips.bet > chips.total:
                print("Not enough chips !! You only have {} $".format(chips.total))
            else:
                break
                    
def hit(deck,hand):
    single_card = deck.deal()
    hand.add_card(single_card)
    hand.adjust_for_ace()
                
def hit_or_stand (deck,hand):
    global playing
    while True:
        choose = input("Hit or Stand, men ? Press 'h' for HIT and 's' for STAND: ")
        if choose[0].lower() == 'h':
            hit(deck,hand)
        elif choose[0].lower() == 's':
            print("Player stand and Dealer's turn")
            playing = False
        else: 
            print("Can understand your choose")
            continue
        break
 
def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.card[0])  
    print("\nPlayer's Hand:", *player.card, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.card, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.card, sep='\n ')
    print("Player's Hand =",player.value)           

def player_busts(player, dealer, chips):
    print("BUSTS PLAYER !") 
    chips.losebet()
    
def player_wins(player,dealer,chips):
    print("PLAYER WIN !")
    chips.winbet()

def dealer_busts(player,dealer,chips):
    print("BUSTS DEALER !") 
    chips.winbet()

def dealer_wins(player,dealer,chips):
    print("DEALER WIN !")
    chips.losebet()

def push(player,dealer):
    print("Dealer and player tie ! PUSH ")
    
     
###################################################
########         Playing Game           ###########

# while True:
    
#     print("WELCOME TO BLACK JACK")
#     deck = Deck()
#     deck.shuffle()
    
#     player_hand = Hand()
#     player_hand.add_card(deck.deal())
#     player_hand.adjust_for_ace()
    
#     dealer_hand = Hand()
#     dealer_hand.add_card(deck.deal())
#     dealer_hand.adjust_for_ace()
    
#     player_chips = Chip()
    
#     take_bet(player_chips)

#     show_some(player_hand, dealer_hand)
    
while True:
    # Print an opening statement
    print('Welcome to BlackJack! Get as close to 21 as you can without going over!\n\
    Dealer hits until she reaches 17. Aces count as 1 or 11.')
    
    # Create & shuffle the deck, deal two cards to each player
    deck = Deck()
    deck.shuffle()
    
    player_hand = Hand()
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())
    
    dealer_hand = Hand()
    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())
            
    # Set up the Player's chips
    player_chips = Chip()  # remember the default value is 100    
    
    # Prompt the Player for their bet
    take_bet(player_chips)
    
    # Show cards (but keep one dealer card hidden)
    show_some(player_hand,dealer_hand)
    
    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
        hit_or_stand(deck,player_hand) 
        
        # Show cards (but keep one dealer card hidden)
        show_some(player_hand,dealer_hand)  
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
        if player_hand.value > 21:
            player_busts(player_hand,dealer_hand,player_chips)
            break        


    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17 
    if player_hand.value <= 21:
        
        while dealer_hand.value < 17:
            hit(deck,dealer_hand)    
    
        # Show all cards
        show_all(player_hand,dealer_hand)
        
        # Run different winning scenarios
        if dealer_hand.value > 21:
            dealer_busts(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_wins(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_wins(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    
    # Ask to play again
    new_game = input("Would you like to play another hand? Enter 'y' or 'n' ")
    
    if new_game[0].lower()=='y':
        playing=True
        continue
    else:
        print("Thanks for playing!")
        break
