FACE_VALUE = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

FACE_REPR = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
             9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

HAND_ORDER = ['straight_flush', 'foak', 'full_house', 'flush', 'straight',
              'toak', 'two_pair', 'pair']


def get_nums(hole, table):
    return sorted([FACE_VALUE[num[0]] for num in hole + table])


def get_suits(hole, table):
    return sorted([num[1] for num in hole + table])


def get_hand(hole, table):
    pairs = {}
    hands = {
        'straight_flush': None,
        'flush': None,
        'straight': [],
        'full_house': None,
        'foak': None,
        'toak': None,
        'pair': None,
        'two_pair': None
    }

    nums = get_nums(hole, table)

    # Check flush
    flushes = cards_required_for_flush(hole, table)
    if sorted(flushes.values())[0] <= 0:
        hands['flush'] = True

    # Check straight
    if 14 in nums:
        # Ace can be low card
        streak = [1]
        prev = 1
    else:
        streak = []
        prev = None
    for num in nums:
        if prev is not None and num - prev == 1:
            streak.append(num)
            if len(streak) >= 5:
                hands['straight'] = streak
        elif num == prev:
            pairs_num = pairs.get(num, 1)
            pairs[num] = pairs_num + 1
            streak = [num]
        else:
            streak = [num]
        prev = num

    # TODO(pcsforeducation) handle straight flush
    #if hands['flush'] and hands['straight']:
    #    hands['straight_flush'] = hands['straight']

    for k, v in pairs.items():
        if v == 4:
            hands['foak'] = k
        if v == 3:
            if k > hands['toak']:
                hands['toak'] = k
        elif v == 2:
            if k > hands['pair']:
                # Possibly gives wrong 3 pair
                if hands['pair']:
                    hands['two_pair'] = [k, hands['pair']]
                hands['pair'] = k

    if hands['toak'] and hands['pair']:
        if hands['two_pair']:
            hands['full_house'] = (hands['toak'], hands['two_pair'][0])
        else:
            hands['full_house'] = (hands['toak'], hands['pair'])
    return hands


def highest_hand(hole, table, hands=None):
    if not hands:
        hands = get_hand(hole, table)
    for hand in HAND_ORDER:
        if hands[hand]:
            return hand
    return 'high card'


def cards_required_for_flush(hole, table):
    """Returns the cards required per suit for a flush"""
    suits = get_suits(hole, table)
    return {key: 5 - suits.count(key) for key in ['h', 's', 'd', 'c']}
