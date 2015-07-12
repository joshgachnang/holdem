import json
import logging

FACE_VALUE = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8,
              '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}

FACE_REPR = {1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
             9: '9', 10: 'T', 11: 'J', 12: 'Q', 13: 'K', 14: 'A'}

logger = logging.getLogger()


class StaticHoleStrategy(object):
    def __init__(self):
        self.data = {}
        with open('/Users/josh/src/holdem/static_hole/hole_data.json',
                  'r') as f:
            self.data = json.load(f)
        print("Hole len {}".format(len(self.data.keys())))

    def get_win_percentage(self, hand):
        suited = "s" if hand[2] == hand[5] else ""
        if FACE_VALUE[hand[1]] <= FACE_VALUE[hand[4]]:
            hole = "{}{}{}".format(hand[1], hand[4], suited)
        else:
            hole = "{}{}{}".format(hand[4], hand[1], suited)
        return self.data[hole]["win"]
