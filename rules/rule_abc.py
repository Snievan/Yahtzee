from abc import ABC, abstractmethod
from typing import List, Tuple

from dices import Dices


class Rule(ABC):
    description: str = None
    scores: str = None
    examples: List = None

    @abstractmethod
    def get_score(self, dices: Dices) -> int:
        pass

    @property
    def name(self):
        return self.__class__.__name__

    @property
    def examples_scores(self):
        """Return exmple's coressponding scores"""
        dices = Dices()
        dices.set_faces(self.examples)
        _scores = self.get_score(dices)
        return _scores


    def _check_rule(self, faces: List = None):
        print("===========================")
        print('Check rule for: ', self.name)
        dices = Dices()
        if faces == None:
            dices.set_faces(self.examples)
        else:
            dices.set_faces(faces)
        print(f"Dices is : {dices}")
        print(f'Score is : {self.get_score(dices)}')


class UpperRule(Rule):
    description = "Any combination"
    dice_num: int = 0
    # scores = f'Sum of dice {dice_num}'

    @property
    def scores(self):
        return f'Sum of dice {self.dice_num}'

    def get_score(self, dices: Dices):
        score = sum(dices.faces == self.dice_num) * self.dice_num
        return score


class LowerRule(Rule):

    def get_score(self, dices: Dices):
        score = sum(dices.faces == self.dice_num) * self.dice_num
        return score

    @abstractmethod
    def is_valid(self, dices: Dices):
        pass
