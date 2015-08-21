import json
import logging
import os

logger = logging.getLogger()


class StaticHoleStrategy(object):
    def __init__(self):
        self.data = {}
        data_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                 'hole_data.json')
        with open(data_path, 'r') as f:
            self.data = json.load(f)
        logger.debug("Hole len {}".format(len(self.data.keys())))

    def get_win_percentage(self, hand):
        suited = "s" if hand[0][1] == hand[1][1] else ""
        hole = "{}{}{}".format(hand[0][0], hand[1][0], suited)
        return self.data[hole]["win"]

    def get_multiplier(self, hole):
        win = float(self.get_win_percentage(hole))

        if win < 40:
            return 2
        elif 40 <= win < 50:
            return 3
        elif 50 <= win < 60:
            return 5
        elif 60 <= win < 65:
            return 10
        elif 65 <= win < 80:
            return 25
        else:
            return 100
