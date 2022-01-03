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


def score_card(card):
    value = (card % 13) + 1
    return min(value, 10)


def score_hand(hand):
    s = 0
    for card in hand:
        s += score_card(card)
    return s


def will_dealer_hit(hand):
    return score_hand(hand) < 17


def is_bust_hand(hand):
    return score_hand(hand) > 21


def card_suite_to_str(card):
    sector = card // 13
    if sector == 0:
        return 'spades'
    elif sector == 1:
        return 'hearts'
    elif sector == 2:
        return 'diamonds'
    else:
        return 'clubs'


def card_name_to_str(card):
    value = (card % 13) + 1
    if value == 1:
        return 'ace'
    elif value == 11:
        return 'jack'
    elif value == 12:
        return 'queen'
    elif value == 13:
        return 'king'
    else:
        return str(value)


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
