from rules.rule_abc import UpperRule


class Aces(UpperRule):
    dice_num = 1
    examples = [1, 1, 1, 3, 4]


class Twos(UpperRule):
    dice_num = 2
    examples = [2, 2, 2, 5, 6]


class Threes(UpperRule):
    dice_num = 3
    examples = [3, 3, 3, 3, 4]


class Fours(UpperRule):
    dice_num = 4
    examples = [4, 4, 5, 5, 5]


class Fives(UpperRule):
    dice_num = 5
    examples = [1, 1, 2, 2, 5]


class Sixes(UpperRule):
    dice_num = 6
    examples = [3, 3, 6, 6, 6]


if __name__ == "__main__":

    rules = [Aces, Twos, Threes,
             Fours, Fives, Sixes]
    for rule in rules:
        instance = rule()
        instance._check_rule()

