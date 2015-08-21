import utils

MULTIPLIER = {
    'straight_flush': 300,
    'foak': 200,
    'full_house': 60,
    'flush': 50,
    'straight': 40,
    'toak': 30,
    'two_pair': 25,
    'pair': 15
}


class TableStrategy(object):
    def __init__(self, scale=1):
        self.multiplier = {k: v * scale for k, v in MULTIPLIER.items()}

    def get_table_multiplier(self, hole, table, hand):
        highest_hand = utils.highest_hand(hole, table, hand)
        return MULTIPLIER[highest_hand]
