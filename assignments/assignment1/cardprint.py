def card_suite_to_symbol_str(suite):
    assert suite in ['spades', 'hearts', 'diamonds', 'clubs']
    
    if suite == 'spades':
        return '♠'
    elif suite == 'hearts':
        return '♥'
    elif suite == 'diamonds':
        return '♦'
    else:
        return '♣'
    
'''
*******
*7    *
*  ♠  *
*     *
*******
'''
def card_matrix(name, suite):
    s = card_suite_to_symbol_str(suite)
    row1 = ['*'] * 7
    row2 = ['*', ' ', ' ', ' ', ' ', ' ', '*']
    row3 = ['*', ' ', ' ', s, ' ', ' ', '*']
    row4 = ['*', ' ', ' ', ' ', ' ', ' ', '*']
    row5 = ['*'] * 7

    if name == 'ace':
        row2[1] = 'A'
    elif name == 'jack':
        row2[1] = 'J'
    elif name == 'queen':
        row2[1] = 'Q'
    elif name == 'king':
        row2[1] = 'K'
    else:
        value = int(name)
        if value == 10:
            row2[1] = '1'
            row2[2] = '0'
        else:
            row2[1] = name
    return [row1, row2, row3, row4, row5]


def pretty_hand_str(hand_str):
    res = ''
    card_matrices = [card_matrix(card_str.split(' of ')[0], card_str.split(' of ')[1]) for card_str in hand_str]
    for i in range(5):
        res += ' '.join([''.join(c[i]) for c in card_matrices]) + '\n'
    return res

