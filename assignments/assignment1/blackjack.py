import time
import random

import cardprint

def new_deck():
    return [i for i in range(52)]


def shuffle(deck):
    random.shuffle(deck)


def deal_card(deck):
    assert len(deck) > 0
    return deck.pop()


def deal_hand(deck):
    card1 = deal_card(deck)
    card2 = deal_card(deck)
    return [card1, card2]


# TODO(student): implement
def score_card(card):
    """
    Takes an integer in range [0,51] representing a card, and returns card's score if it were in a hand.
    Note that we treat aces as always 1 (and never 11).
    """
    return card


# TODO(student): implement
def score_hand(hand):
    """
    Takes a list of integers representing a hand of cards, and returns the score of the hand.
    """ 
    return 0


# TODO(student): implement
def will_dealer_hit(hand):
    """
    Takes a list of integers representing a hand of cards, and returns True if the dealer would hit on the hand. 
    Returns False otherwise. 
    """
    return False


# TODO(student): implement
def is_bust_hand(hand):
    """
    Takes a list of integers representing a hand of cards, and returns True if the hand is busted. Otherwise False.
    """
    return False


# TODO(student): implement
def card_suite_to_str(card):
    """
    Takes an integer representing a card, and returns the suite of that card as a string (i.e. 'spades',
    'hearts', 'diamonds', or 'clubs').
    """
    return 'spades'


# TODO(student): implement
def card_name_to_str(card):
    """
    Takes an integer representing a card, and returns the string representation of that card's name (e.g. 
    ace -> 'ace', 7 -> '7', queen -> 'queen').
    """
    return str(card)


def card_to_str(card):
    return card_name_to_str(card) + ' of ' + card_suite_to_str(card)


def print_game_state(player_hand, dealer_hand, deck):
    player_hand_str = [card_to_str(card) for card in player_hand]
    print('[Player]: %s' % ', '.join(player_hand_str))
    print(cardprint.pretty_hand_str(player_hand_str))
    dealer_hand_str = [card_to_str(card) for card in dealer_hand]
    print('[Dealer]: %s' % ', '.join(dealer_hand_str))
    print(cardprint.pretty_hand_str(dealer_hand_str))


def play_game():
    deck = new_deck()
    shuffle(deck)

    dealer_hand = deal_hand(deck)
    player_hand = deal_hand(deck)

    print_game_state(player_hand, dealer_hand, deck)

    choice = input('??? What will you do? Hit - H, Stand - S. Player choice: ')
    while choice != 'S':
        if choice not in ['H', 'S']:
            print('!!! You must choose from one of the following: Hit - H, Stand - S')
        elif choice == 'S':
            break
        else:
            print('>>> PLAYER HITS')
            player_hand.append(deal_card(deck))
            print_game_state(player_hand, dealer_hand, deck)
            if is_bust_hand(player_hand):
                print('=== PLAYER BUSTED, DEALER WINS ===')
                return
        choice = input('??? What will you do? Hit - H, Stand - S. Player choice: ')

    print('>>> PLAYER STAYS')
            
    while will_dealer_hit(dealer_hand):
        print('>>> DEALER HITS')
        time.sleep(1.0)
        dealer_hand.append(deal_card(deck))
        print_game_state(player_hand, dealer_hand, deck)
        if is_bust_hand(dealer_hand):
            print('=== DEALER BUSTED, PLAYER WINS! ===')
            return

    print('>>> DEALER STAYS')

    player_score = score_hand(player_hand)
    dealer_score = score_hand(dealer_hand)

    if player_score > dealer_score:
        print('===        PLAYER WINS!         ===')
    elif player_score < dealer_score:
        print('===        DEALER WINS!         ===')
    else:
        print('===            TIE!             ===')
    

if __name__ == '__main__':
    play_game()
