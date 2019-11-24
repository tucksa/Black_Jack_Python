# display black jack table showing one card up from dealer and one card down from dealer then two cards up for player
def display_initial(dealer,player):
    print('Dealer:')
    print('------------        ------------')
    print('|          |        |          |')
    if type(dealer.cards[0].face) != int:
        total_len = 8 - len(dealer.cards[0].face)
    elif dealer.cards[0].face == 10:
        total_len = 6
    else:
        total_len = 7
    face_print = f'|  {dealer.cards[0].face}'
    for _ in range(0,total_len):
        face_print += ' '
    print(f'{face_print}|        |          |')
    print('|  of      |        |          |')
    total_len = 8 - len(dealer.cards[0].suit)
    suit_print = f'|  {dealer.cards[0].suit}'
    for _ in range(0,total_len):
        suit_print += ' '
    print(f'{suit_print}|        |          |')
    print('|          |        |          |')
    print('------------        ------------')
    
    print('Player:')
    for i in player.cards:
        print('------------')
        print('|          |')
        if type(i.face) != int:
            total_len = 8 - len(i.face)
        elif i.face == 10:
            total_len = 6
        else:
            total_len = 7
        face_print = f'|  {i.face}'
        for _ in range(0,total_len):
            face_print += ' '
        print(f'{face_print}|')
        print('|  of      |')
        total_len = 8 - len(i.suit)
        suit_print = f'|  {i.suit}'
        for _ in range(0,total_len):
            suit_print += ' '
        print(f'{suit_print}|')
        print('|          |')
        print('------------')

# create a second display function for when its the dealers turn
def dealer_turn_display(dealer, player_total):
    print(f'Player total- {player_total}')
    for i in dealer.cards:
        print('------------')
        print('|          |')
        if type(i.face) != int:
            total_len = 8 - len(i.face)
        elif i.face == 10:
            total_len = 6
        else:
            total_len = 7
        face_print = f'|  {i.face}'
        for _ in range(0,total_len):
            face_print += ' '
        print(f'{face_print}|')
        print('|  of      |')
        total_len = 8 - len(i.suit)
        suit_print = f'|  {i.suit}'
        for _ in range(0,total_len):
            suit_print += ' '
        print(f'{suit_print}|')
        print('|          |')
        print('------------')
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
    def __init__(self, cards):
        self.cards = cards
    def total(self):
        total = 0
        for card in self.cards:
            if card.face == 'King':
                total += 13
            elif card.face == 'Queen':
                total += 12
            elif card.face == 'Jack':
                total += 11
            elif card.face in [2,3,4,5,6,7,8,9,10]:
                total += card.face
            else:
                continue
        return total

#create a player object- will need to know the cards they have, the total count for the cards, the amount of money to bet and if you have time a win streak tracker (if they win 3 in a row)
class Player:
    def __init__(self, cards, account, wins):
        self.cards = cards
        self.account = account
        self.wins = wins

    def total(self):
        total = 0
        for card in self.cards:
            if card.face == 'King':
                total += 13
            elif card.face == 'Queen':
                total += 12
            elif card.face == 'Jack':
                total += 11
            elif card.face in [2,3,4,5,6,7,8,9,10]:
                total += card.face
            else:
                continue
        return total

#function to ask the player what they would like to bet. check to ensure this does not exceed the total money in the player's account
def bet(player):
    amount = int(input('How much would you like to bet? '))
    while amount > player.account:
        amount = int(input(f'Sorry, this amount exceeds your funds of {player.account}. What would you like to bet? '))
    return amount 

#function to ask the player if they would like to stand or hit
def stand_hit():
    return input('Would you like to stand or hit? (s/h)')

#function to randomly draw a card from the deck
def draw(deck, existing):
    import random
    index = random.randint(0,51)
    while deck[index] in existing:
        index = random.randint(0,51)
    existing.append(deck[index])
    return deck[index], existing

#function to check that the randomly drawn card has not already been pulled- (check against dealer.cards and player.cards). if so re-draw

#function for dealer play (enacted if the player chooses stand) the dealer will continue to draw from the deck until their cards beat the player total or they bust. 
def dealer_turn(dealer, player_total, deck, existing_cards):
    dealer_total = ace(dealer)
    while dealer_total <= player_total and dealer_total < 21:
        card, added_card = draw(deck, existing_cards)
        existing_cards.append(added_card)
        dealer.cards.append(card)
        dealer_total = ace(dealer)
        dealer_turn_display(dealer, player_total)
    return dealer_total


#function to determine which Ace value to use
def ace(player):
    ace_count = 0
    value = 0
    player_total = player.total()
    for card in player.cards:
        if card.face == 'Ace':
            ace_count += 1
    if ace_count == 1:
        if player_total + 11 <= 21:
            value = 11
        else:
            value = 1
    elif ace_count == 2:
        if player_total + 12 <= 21:
            value = 12
        else:
            value = 2
    elif ace_count == 3:
        if player_total + 13 <= 21:
            value = 13
        else:
            value = 3
    elif ace_count == 4:
        if player_total + 14 <= 21:
            value = 14
        else:
            value = 4
    player_total += value
    return player_total

#function to check who wins. if the player hits 21 then they win. If the player exceeds 21 then they lose (bust) 
#once they stand and the dealer turn begins if the dealer goes over 21 then the player wins. if the deal total is closer to 21 than the player then the dealer wins else the dealer loses (bust)
def win_check(dealer,player):
    winner = ''
    if 21 - dealer < 21 - player and dealer <= 21:
        winner = 'dealer'
    else:
        winner = 'player'
    return winner

card1 = Card('Hearts', 'King')
card2 = Card('Hearts', 5)

Sarah = Player([card1, card2], 100, 0)

def play():
    deck = create_deck()
    existing_cards = []
    dealer_card1, added_card = draw(deck, existing_cards)
    existing_cards.append(added_card)
    dealer_card2, added_card = draw(deck, existing_cards)
    existing_cards.append(added_card)
    player_card1, added_card = draw(deck, existing_cards)
    existing_cards.append(added_card)
    player_card2, added_card = draw(deck, existing_cards)
    existing_cards.append(added_card)
    dealer = Dealer([dealer_card1,dealer_card2])
    player = Player([player_card1, player_card2], 100, 0)
    bet_amount = bet(player)
    winner = ''
    print(f'Great, there is {bet_amount} on the table')
    display_initial(dealer, player)
    player_turn = stand_hit()
    player_total = ace(player)
    while player_turn == 'h':
        card, added_card = draw(deck, existing_cards)
        existing_cards.append(added_card)
        player.cards.append(card)
        display_initial(dealer, player)
        player_total = ace(player)
        if player_total < 21:
            player_turn = stand_hit()
        elif player_total == 21: 
            print(f'Congrantulations!!! You hit 21. You won ${bet_amount}')
            player_turn = 's'
            winner = 'player'
            player.wins += 1
            player.account += bet_amount
        else:
            print(f'BUST.... you lost ${bet_amount}')
            player_turn = 's'
            winner = 'dealer'
            player.account -= bet_amount
    if winner == '' and player_total <= 21:
        print('Ok, time for the dealer to go')
        dealer_turn_display(dealer, player_total)
        dealer_total = dealer_turn(dealer, player_total, deck, existing_cards)
        print(f'Dealer- {dealer_total}')
        winner = win_check(dealer_total, player_total)
        print(f'The winner is the {winner}')
        if winner == 'player':
            player.wins += 1
            print(f'You won ${bet_amount}')
            player.account += bet_amount
        else:
            print(f'You lost ${bet_amount}')
            player.account -= bet_amount  
    elif winner == '' and player_total == 21:
        print(f'Wow, lady luck is on your side- WINNER ${bet_amount}')
        winner = 'player'
        player.wins += 1
        player.account += bet_amount
    elif winner == '' and player_total > 21:
        print(f'You should rethink this game.... started out with a bust- you lost ${bet_amount}')
        player.account -= bet_amount
    else:
        print(f'The winner is the {winner}')
        if winner == 'player':
            player.wins += 1
            print(f'You won ${bet_amount}')
            player.account += bet_amount
        else:
            print(f'You lost ${bet_amount}')
            player.account -= bet_amount  
    replay = input('Would you like to play again? y/n ')
    while replay == 'y':
        existing_cards = []
        dealer_card1, added_card = draw(deck, existing_cards)
        existing_cards.append(added_card)
        dealer_card2, added_card = draw(deck, existing_cards)
        existing_cards.append(added_card)
        player_card1, added_card = draw(deck, existing_cards)
        existing_cards.append(added_card)
        player_card2, added_card = draw(deck, existing_cards)
        existing_cards.append(added_card)
        player.cards = [player_card1, player_card2]
        dealer.cards = [dealer_card1, dealer_card2]
        bet_amount = bet(player)
        winner = ''
        print(f'Great, there is {bet_amount} on the table')
        display_initial(dealer, player)
        player_turn = stand_hit()
        player_total = ace(player)
        while player_turn == 'h':
            card, added_card = draw(deck, existing_cards)
            existing_cards.append(added_card)
            player.cards.append(card)
            display_initial(dealer, player)
            player_total = ace(player)
            if player_total < 21:
                player_turn = stand_hit()
            elif player_total == 21: 
                print(f'Congrantulations!!! You hit 21. You won ${bet_amount}')
                player_turn = 's'
                winner = 'player'
                player.wins += 1
                player.account += bet_amount
            else:
                print(f'BUST.... you lost ${bet_amount}')
                player_turn = 's'
                winner = 'dealer'
                player.account -= bet_amount
        if winner == '' and player_total <= 21:
            print('Ok, time for the dealer to go')
            dealer_turn_display(dealer, player_total)
            dealer_total = dealer_turn(dealer, player_total, deck, existing_cards)
            print(f'Dealer- {dealer_total}')
            winner = win_check(dealer_total, player_total)
            print(f'The winner is the {winner}')
            if winner == 'player':
                player.wins += 1
                print(f'You won ${bet_amount}')
                player.account += bet_amount
            else:
                print(f'You lost ${bet_amount}')
                player.account -= bet_amount  
        elif winner == '' and player_total == 21:
            print(f'Wow, lady luck is on your side- WINNER ${bet_amount}')
            winner = 'player'
            player.wins += 1
            player.account += bet_amount
        elif winner == '' and player_total > 21:
            print(f'You should rethink this game.... started out with a bust- you lost ${bet_amount}')
            player.account -= bet_amount
        else:
            print(f'The winner is the {winner}')
            if winner == 'player':
                player.wins += 1
                print(f'You won ${bet_amount}')
                player.account += bet_amount
            else:
                print(f'You lost ${bet_amount}')
                player.account -= bet_amount  
        replay = input('Would you like to play again? y/n ')
play()
