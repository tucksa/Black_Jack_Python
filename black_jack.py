# display black jack table showing one card up from dealer and one card down from dealer then two cards up for player
def display_initial(dealer,player):
    print('Dealer:')
    print('---------        ---------')
    print('|        |        |        |')
    print(f'|     {dealer.cards[0].face}     |        |        |')
    print('|   of   |        |        |')
    print(f'|     {dealer.cards[0].suit}     |        |        |')
    print('|         |        |        |')
    print('---------        ---------')
    #insert loop through player cards and display all face up

# create a second display function for when its the dealers turn

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
def bet(player):
    amount = int(input('How much would you like to bet? '))
    while amount > player.account:
        input(f'Sorry, this amount exceeds your funds of {player.account}. What would you like to bet? ')
    return amount 

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
def dealer_turn(player, dealer, deck):
    while True:
        if dealer.total <= player.total and dealer.total < 21:
            card = draw(deck)
            value = hit(card)
            if value != [1,11]:
                dealer.total += value
            else:
                value = ace(dealer,deck)
                dealer.total += value
        else:
            return dealer.total

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

#function to determine which Ace value to use
def ace(player, deck):
    value = [1,11]
    if player.total + 11 > 21:
        value = 1
    else:
        value = 11
    return value

#function to check who wins. if the player hits 21 then they win. If the player exceeds 21 then they lose (bust) 
#once they stand and the dealer turn begins if the dealer goes over 21 then the player wins. if the deal total is closer to 21 than the player then the dealer wins else the dealer loses (bust)
def win_check(dealer,player):
    winner = ''
    if dealer.total == 21 and player.total != 21:
        winner = 'dealer'
    elif player.total > 21:
        winner = 'dealer'
    elif 21 - dealer.total < 21 - player.total:
        winner = 'dealer'
    else:
        winner = 'player'
    return winner