import blackjack


def run_test(t):
    test_result, test_msg = t()

    if test_result:
        print('PASSED: %s.' % t.__name__)
    else:
        print('FAILED: %s. %s' % (t.__name__, test_msg))
        
    return test_result


def test_score_card_9_of_spades():
    card = 8
    score = blackjack.score_card(card)
    return (score == 9, 'Expected 9, got %d' % score)


def test_score_card_ace_of_clubs():
    card = 39
    score = blackjack.score_card(card)
    return (score == 1, 'Expected 1, got %d' % score)


def test_score_card_queen_of_hearts():
    card = 24
    score = blackjack.score_card(card)
    return (score == 10, 'Expected 10, got %d' % score)


def test_score_hand_9_of_spades_ace_of_clubs():
    hand = [8, 39]
    score = blackjack.score_hand(hand)
    return (score == 10, 'Expected 10, got %d' % score)


def test_will_dealer_hit_yes():
    hand = [0, 1, 2]
    will_dealer_hit = blackjack.will_dealer_hit(hand)
    return (will_dealer_hit, 'Expected True, got False')


def test_will_dealer_hit_no():
    hand = [9, 6]
    will_dealer_hit = blackjack.will_dealer_hit(hand)
    return (not will_dealer_hit, 'Expected False, got True')


def test_is_bust_hand_yes():
    hand = [8, 39, 24, 2]
    is_bust_hand = blackjack.is_bust_hand(hand)
    return (is_bust_hand, 'Expected True, got False')

    
def test_is_bust_hand_no():
    hand = [8, 39, 24]
    is_bust_hand = blackjack.is_bust_hand(hand)
    return (not is_bust_hand, 'Expected False, got True')


def test_card_to_str_9_of_spades():
    card = 8
    card_str = blackjack.card_to_str(card)
    return (card_str == '9 of spades', 'Expected \'9 of spades\', got \'%s\'' % card_str)


def test_card_to_str_ace_of_clubs():
    card = 39
    card_str = blackjack.card_to_str(card)
    return (card_str == 'ace of clubs', 'Expected \'ace of clubs\', got \'%s\'' % card_str)


def test_card_to_str_queen_of_hearts():
    card = 24
    card_str = blackjack.card_to_str(card)
    return (card_str == 'queen of hearts', 'Expected \'queen of hearts\', got \'%s\'' % card_str)


if __name__ == '__main__':
    tests = [test_score_card_9_of_spades,
             test_score_card_ace_of_clubs,
             test_score_card_queen_of_hearts,
             test_score_hand_9_of_spades_ace_of_clubs,
             test_will_dealer_hit_yes,
             test_will_dealer_hit_no,
             test_is_bust_hand_yes,
             test_is_bust_hand_no,
             test_card_to_str_9_of_spades,
             test_card_to_str_ace_of_clubs,
             test_card_to_str_queen_of_hearts]
    
    passed_tests = 0
    for test in tests:
        if run_test(test):
            passed_tests += 1

    print('%d / %d tests passed' % (passed_tests, len(tests)))
