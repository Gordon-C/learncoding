import blackjack


def test_score_card_9_of_spades():
    card = 8
    score = blackjack.score_card(card)
    assert score == 9, 'Expected 9, got %d' % score


def test_score_card_ace_of_clubs():
    card = 39
    score = blackjack.score_card(card)
    assert score == 1, 'Expected 1, got %d' % score

def test_score_card_queen_of_hearts():
    card = 24
    score = blackjack.score_card(card)
    assert score == 10, 'Expected 10, got %d' % score

def test_score_hand_9_of_spades_ace_of_clubs():
    hand = [8, 39]
    score = blackjack.score_hand(hand)
    assert score == 10, 'Expected 10, got %d' % score

def test_will_dealer_hit_yes():
    hand = [0, 1, 2]
    will_dealer_hit = blackjack.will_dealer_hit(hand)
    assert will_dealer_hit, 'Expected True, got False'


def test_will_dealer_hit_no():
    hand = [9, 6]
    will_dealer_hit = blackjack.will_dealer_hit(hand)
    assert not will_dealer_hit, 'Expected False, got True'


def test_is_bust_hand_yes():
    hand = [8, 39, 24, 2]
    is_bust_hand = blackjack.is_bust_hand(hand)
    assert is_bust_hand, 'Expected True, got False'

    
def test_is_bust_hand_no():
    hand = [8, 39, 24]
    is_bust_hand = blackjack.is_bust_hand(hand)
    assert not is_bust_hand, 'Expected False, got True'


def test_card_to_str_9_of_spades():
    card = 8
    card_str = blackjack.card_to_str(card)
    assert card_str == '9 of spades', 'Expected \'9 of spades\', got \'%s\'' % card_str


def test_card_to_str_ace_of_clubs():
    card = 39
    card_str = blackjack.card_to_str(card)
    assert card_str == 'ace of clubs', 'Expected \'ace of clubs\', got \'%s\'' % card_str


def test_card_to_str_queen_of_hearts():
    card = 24
    card_str = blackjack.card_to_str(card)
    assert card_str == 'queen of hearts', 'Expected \'queen of hearts\', got \'%s\'' % card_str


if __name__ == '__main__':
    test_score_card_9_of_spades()
    test_score_card_ace_of_clubs()
    test_score_card_queen_of_hearts()
    test_score_hand_9_of_spades_ace_of_clubs()
    test_will_dealer_hit_yes()
    test_will_dealer_hit_no()
    test_is_bust_hand_yes()
    test_is_bust_hand_no()
    test_card_to_str_9_of_spades()
    test_card_to_str_ace_of_clubs()
    test_card_to_str_queen_of_hearts()
