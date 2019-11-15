# display black jack table showing one card up from dealer and one card down from dealer then two cards up for player

#create a card object
class Card:
    def __init__(self,suit,face):
        self.suit = suit
        self.face = face

#create deck of cards function- for loops to create 52 card instances with each suit/face
def create_deck():
    suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    faces = ['Ace', 2, 3, 4, 5, 6, 7, 8, 9, 10, 'Jack', 'Queen', 'King']
    Deck = []
    for suit in suits:
        for face in faces:
            card = Card(suit, face)
            Deck.append(card)
    return Deck

#create a dealer object- will need to know which cards they have and their total count
class Dealer:
    def __init__(self, cards, total):
        self.cards = cards
        self.total = total

#create a player object- will need to know the cards they have, the total count for the cards, the amount of money to bet and if you have time a win streak tracker (if they win 3 in a row)
class Player:
    def __init__(self, cards, total, account, wins):
        self.cards = cards
        self.total = total
        self.account = account
        self.wins = wins
    def bet(self, amount):
        return amount <= self.account

#function to ask the player what they would like to bet. check to ensure this does not exceed the total money in the player's account

#function to ask the player if they would like to stand or hit
def stand_hit():
    return input('Would you like to stand or hit? (s/h)')

#function to randomly draw a card from the deck
def draw(deck):
    import random
    index = random.randint(0,51)
    return deck[index]

#function to check that the randomly drawn card has not already been pulled- (check against dealer.cards and player.cards). if so re-draw

#function for dealer play (enacted if the player chooses stand) the dealer will continue to draw from the deck until their cards beat the player total or they bust. 

#function to hit. if the player chooses to hit this function will determine the count of the card to be added to the player object
def hit(card):
    if card.face == 'King':
        value = 13
    elif card.face == 'Queen':
        value = 12
    elif card.face == 'Jack':
        value = 11
    elif card.face in [2,3,4,5,6,7,8,9,10]:
        value = int(card.face)
    else:
        value = [1,11]
    return value

#function to check who wins. if the player hits 21 then they win. If the player exceeds 21 then they lose (bust) 
#once they stand and the dealer turn begins if the dealer goes over 21 then the player wins. if the deal total is closer to 21 than the player then the dealer wins else the dealer loses (bust)
