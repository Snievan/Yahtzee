from typing import List

import numpy as np
from dices import Dices

from rules.rule_abc import LowerRule


class ThreeOFaKind(LowerRule):
    description = "At least three of the same"
    scores = "Sum of all dice"
    examples = [2, 3, 4, 4, 4]

    def get_score(self, dices: Dices):
        _valid = self.is_valid(dices)
        return _valid * dices._sum

    def is_valid(self, dices: Dices):
        return dices._max_dup >= 3


class FourOfaKind(LowerRule):
    description = "At least Four of the same"
    scores = "Sum of all dice"
    examples = [4, 5, 5, 5, 5]

    def get_score(self, dices: Dices):
        _valid = self.is_valid(dices)
        return _valid * dices._sum

    def is_valid(self, dices: Dices):
        return dices._max_dup >= 4 


class FullHouse(LowerRule):
    description = "Three of one number and two of another"
    scores = "25"
    examples = [2, 2, 5, 5, 5]

    def get_score(self, dices: Dices):
        _valid = self.is_valid(dices)
        _score = 25
        return _valid * _score

    def is_valid(self, dices: Dices):
        dist = dices._dist_sorted
        return dist[0] == 3 and dist[1] == 2


class SmallStraight(LowerRule):
    description = "Four sequential dice"
    scores = "30"
    examples = [1, 3, 4, 5, 6]

    def get_score(self, dices: Dices):
        _valid = self.is_valid(dices)
        _score = 30
        return _valid * _score

    def is_valid(self, dices: Dices):
        return dices._max_straight_len >= 4


class LargeStraight(LowerRule):
    description = "Five sequential dice"
    scores = "40"
    examples = [1, 2, 3, 4, 5]

    def get_score(self, dices: Dices):
        _valid = self.is_valid(dices)
        _score = 40
        return _valid * _score

    def is_valid(self, dices: Dices):
        return dices._max_straight_len >= 5


class Yahtzee(LowerRule):
    description = "All five dice the same"
    scores = "50"
    examples = [3, 3, 3, 3, 3]

    def get_score(self, dices: Dices):
        _valid = self.is_valid(dices)
        _score = 50
        return _valid * _score

    def is_valid(self, dices: Dices):
        has_fives = dices._max_dup >= 5 
        return has_fives


class Chance(LowerRule):
    description = "Any combination"
    scores = "Sum of all dice"
    examples = [1,1,3,4,5]

    def get_score(self, dices: Dices):
        _valid = self.is_valid(dices)
        _score = int(dices._sum)
        return _valid * _score

    def is_valid(self, dices: Dices):
        return True




if __name__ == "__main__":

    rules = [ThreeOFaKind, FourOfaKind, FullHouse,
                 SmallStraight, LargeStraight, Yahtzee, Chance]
    for rule in rules:
        instance = rule()
        instance._check_rule(faces = [1,2,3,4,5])
