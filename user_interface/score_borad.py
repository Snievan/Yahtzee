from typing import Dict, List

import configure as c
import pandas as pd
from dices import Dices
from rules.rule_abc import Rule
from tabulate import tabulate
from user_score import UserScore

from user_interface.misc import Color, set_color


class ScoreBoard:
    """Player's score card"""
    categories: List[Rule] = c.CATEGORIES
    tot_count: int = c.NUMS_OF_TOT_CAT
    upper_count: int = c.NUMS_OF_UPPER_CAT

    MAX_USER_NUM = 4
    THRESHOLD_SUM = 63

    def __init__(self, user_scores: List[UserScore]):
        """Rule to regist"""

        self.user_scores = user_scores
        self.user_names = [us.user_name for us in user_scores]

    def color_score_one(self, us: UserScore) -> List[str]:
        color_scores = []

        for i, (choosable, score) in enumerate(zip(us.choosable, us.scores)):
            if i == self.upper_count:
                bouus_progression = f"({us.upper_score:.0f}/63)"
                bonus_score = us.bonus_score
                color_scores += [bouus_progression, bonus_score]
            if choosable:
                color_scores.append("")
            else:
                color_scores.append(set_color(score, Color.BOLD))
        color_scores.append(us.total_score)
        return color_scores

    def coloer_score_one_on_choose(self, us: UserScore, dice: Dices) -> List[str]:

        color_scores = []

        for i, (choosable, score) in enumerate(zip(us.choosable, us.scores)):
            if i == self.upper_count:
                bouus_progression = f"({us.upper_score:.0f}/63)"
                bonus_score = us.bonus_score
                color_scores += [bouus_progression, bonus_score]
            if choosable:
                possible_point = self.categories[i].get_score(dice)
                color_scores.append(set_color(possible_point, Color.GREEN))
            else:
                color_scores.append(set_color(score, Color.BOLD))
        color_scores.append(us.total_score)
        return color_scores

    def color_score_board(self) -> pd.DataFrame:
        row_ins = c.CATEGORY_NAMES[:c.NUMS_OF_UPPER_CAT] + set_color(
            ['Bonus Progress', 'Bonus Score'], Color.CYAN) + c.CATEGORY_NAMES[c.NUMS_OF_UPPER_CAT:] + set_color(['Total Score'], Color.CYAN)
        cat_nums = [1, 2, 3, 4, 5, 6] + ['', ''] + \
            [7, 8, 9, 10, 11, 12, 13] + ['']
        content = {"Catogory No.": cat_nums, "Catogory": row_ins}
        for us in self.user_scores:
            content.update({us.user_name: self.color_score_one(us)})
        return pd.DataFrame(content)

    def color_score_board_on_choice(self, us: UserScore, dice: Dices) -> pd.DataFrame:
        df = self.color_score_board().copy()
        df[us.user_name] = self.coloer_score_one_on_choose(us,dice)
        df.rename({us.user_name: set_color(us.user_name,Color.GREEN)},inplace= True )
        return df

    def show_board(self):
        df = self.color_score_board()
        print(tabulate(df, tablefmt='github', headers='keys', showindex=False))

    def show_board_on_choice(self,us:UserScore,dice:Dices):
        df = self.color_score_board_on_choice(us,dice)
        print(tabulate(df, tablefmt='github', headers='keys', showindex=False))



    def __repr__(self):
        return tabulate(self.color_score_board(), tablefmt='github', headers='keys', showindex=False)
