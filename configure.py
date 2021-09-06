from typing import List
from rules.rules_lower import (Chance, FourOfaKind, FullHouse, LargeStraight,
                               SmallStraight, ThreeOFaKind, Yahtzee)
from rules.rules_upper import Aces, Fives, Fours, Sixes, Threes, Twos
from rules.rule_abc import Rule

CATEGORIES: List[Rule] = [Aces(), Twos(), Threes(), Fours(), Fives(), Sixes(),
                          ThreeOFaKind(), FourOfaKind(), FullHouse(), SmallStraight(), LargeStraight(), Yahtzee(), Chance()]
CATEGORY_NAMES = [cat.name for cat in CATEGORIES]
NUMS_OF_TOT_CAT = 13
NUMS_OF_UPPER_CAT = 6

if __name__ == '__main__':
    from tabulate import tabulate
    import pandas as pd 
    content = []
    for cat in CATEGORIES:
        content.append([cat.name,cat.scores,'-'.join([str(i) for i in cat.examples]),cat.examples_scores])
    df = pd.DataFrame(content,columns=['Catorory','Score method','Example','Example score'])
    print(df.to_markdown())

