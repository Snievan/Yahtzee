from typing import List

from tabulate import tabulate

import configure as c
from dices import Dices
from rules.rule_abc import Rule


class UserScore:
    "Player's personal score. Records his/her category selections and scores"

    categories: List[Rule] = c.CATEGORIES
    tot_count: int = c.NUMS_OF_TOT_CAT
    upper_count: int = c.NUMS_OF_UPPER_CAT

    user_name: str = "Ace"
    inds: List[int] = []
    names: List[str] = []
    choosable: List[bool] = []
    scores: List[int] = []

    upper_score: int = 0 
    bonus_score: int = 0
    total_score: int = 0

    def __init__(self, user_name: str = "Ace") -> None:
        self.user_name = user_name
        self.inds = range(self.tot_count)
        self.names = [cat.name for cat in self.categories]
        self.choosable = [True] * self.tot_count
        self.scores = [0] * self.tot_count

    def choose_category(self, ind: int, dices: Dices) -> bool:
        "Player choose a category to regist, return True if success"
        if not self.choosable[ind]:
            return False
        catgory = self.categories[ind]
        score = catgory.get_score(dices)
        self.choosable[ind] = False
        self.scores[ind] = score
        self.update_bonus_score()
        self.update_total_score()
        return True

    def update_bonus_score(self) -> None:
        "Caculate bonus score.If sum of upper section score up to 63, player gain extra 35 poing"
        BONUS_SCORE = 35
        THRESHOLD_SUM = 63
        self.upper_score = sum(self.scores[:self.upper_count])
        is_valid = self.upper_score >= THRESHOLD_SUM
        self.bonus_score = is_valid * BONUS_SCORE

    def update_total_score(self) -> None:
        "Caculate total score"
        plain_score = sum(self.scores)
        bonus_score = self.bonus_score
        self.total_score = plain_score + bonus_score

    def __repr__(self) -> tabulate:
        return f"user(user_name={self.user_name},score={self.total_score})"
