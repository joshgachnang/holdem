import unittest

import utils


class TestUtils(unittest.TestCase):
    def setUp(self):
        self.test_hole = [('2', 's'), ('3', 's')]
        self.test_flop = [('2', 'h'), ('A', 'h'), ('K', 'h')]
        self.test_turn = self.test_flop + [('3', 'd')]
        self.test_river = self.test_turn + [('2', 'd')]
        self.straight_flop = [('4', 'h'), ('5', 'h'), ('6', 'h')]
        self.straight_river = self.straight_flop + [('7', 'h'), ('9', 's')]
        self.flush_flop = [('5', 's'), ('6', 's'), ('7', 's')]

    def test_current(self):
        nums = utils.get_nums(self.test_hole, self.test_flop)
        self.assertEqual([2, 2, 3, 13, 14], nums)

    def test_pair_flop(self):
        hand = utils.highest_hand(self.test_hole, self.test_flop)
        self.assertEqual('pair', hand)

    def test_two_pair_turn(self):
        hand = utils.highest_hand(self.test_hole, self.test_turn)
        self.assertEqual('two_pair', hand)

    def test_full_house_vier(self):
        hand = utils.highest_hand(self.test_hole, self.test_river)
        self.assertEqual('full_house', hand)

    def test_5_straight(self):
        hand = utils.highest_hand(self.test_hole, self.straight_flop)
        self.assertEqual('straight', hand)

    def test_6_straight(self):
        hand = utils.highest_hand(self.test_hole, self.straight_river)
        self.assertEqual('straight', hand)

    def test_4_not_straight(self):
        self.straight_flop[2] = ('7', 'h')
        hand = utils.highest_hand(self.test_hole, self.straight_flop)
        self.assertEqual('high card', hand)

    def test_ace_low_straight(self):
        hand = utils.highest_hand(self.test_hole,
                                  [('4', 'h'), ('5', 'h'), ('A', 'h')])
        self.assertEqual('straight', hand)

    # def test_straight_flush(self):
    #     hole = [('2', 'h'), ('3', 'h')]
    #     hand = utils.highest_hand(hole, self.straight_flop)
    #     self.assertEqual('straight_flush', hand)

    def test_5_flush(self):
        hand = utils.highest_hand(self.test_hole, self.flush_flop)
        self.assertEqual('flush', hand)

    def test_6_flush(self):
        hand = utils.highest_hand(self.test_hole,
                                  self.flush_flop + [('8', 's')])
        self.assertEqual('flush', hand)

    def test_4_not_flush(self):
        hand = utils.highest_hand([('8', 'h'), ('9', 's')], self.test_flop)
        self.assertEqual('high card', hand)



if __name__ == "__main__":
    unittest.main()
