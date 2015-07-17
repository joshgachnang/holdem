import utils

MULTIPLIER = {
    'straight_flush': 25,
    'foak': 30,
    'full_house': 15,
    'flush': 10,
    'straight': 8,
    'toak': 6,
    'two_pair': 4,
    'pair': 3
}


class TableStrategy(object):
    def __init__(self, scale=1):
        self.multiplier = {k: v * scale for k, v in MULTIPLIER.items()}

    def get_table_multiplier(self, hole, table, hand):
        highest_hand = utils.highest_hand(hole, table, hand)
        return MULTIPLIER[highest_hand]
