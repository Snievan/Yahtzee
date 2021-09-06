from typing import List, Optional, Tuple

import configure as c
from user_score import UserScore


class UserInput:

    def __init__(self, max_player: int = 4) -> None:
        self.max_player = max_player

    @staticmethod
    def game_start():
        print("Welcome to YAHZEET! ")

    def regist_users(self) -> List[str]:

        seq = ['first', 'second', 'third', 'fourth']
        user_names = []
        for i in range(self.max_player):
            instruction = f"Plase enter the {seq[i]} player name(enter empty to complete):"
            user_name = input(instruction)
            if not user_name:
                break
            user_names.append(user_name)
        print("You have done player registeration")
        print("Players are: " + str(user_names))
        return user_names

    @staticmethod
    def start_turn(us: UserScore) -> None:

        instrunction = f"Plase press [ENTER] to start {us.user_name}'s turn and make a first roll:"
        _ = input(instrunction)

    @staticmethod
    def choose_dices() -> Tuple[bool, List[int]]:
        """Player enter empty to want to skip roll section, enter numbers sep by space to choose dics want to keep"""
        instruction = "[DICE SELECTION] Plaeas input Dice number you want to reroll(seperate by spcae): "
        is_select: bool = True
        choice_list: List[int] = []
        while True:
            choice = input(instruction)

            if not choice:
                print("Skip roll dices")
                is_select = False
                break
            try:
                choice = choice.split(' ')
                for i in choice:
                    assert i.isnumeric(), "Not a number"
                    choice_list.append(int(i)-1)
                break
            except:
                # print(traceback.format_exc())
                print("Not a valid selection, please try again")
        return is_select, choice_list

    @staticmethod
    def choose_category() -> int:
        instruction = "[CATEGORY SELECTION] Plaeas input category number you want to choose: "
        while True:
            choice = input(instruction)
            if not choice:
                return -1
            try:
                assert choice.isnumeric(), "Not a number"
                assert 0 <= int(choice) <= c.NUMS_OF_TOT_CAT, "Out of range"
                break
            except:
                # print(traceback.format_exc())
                print("Not a valid selection, please try again")
        return int(choice) - 1

    def game_end():
        print("Hope you have greate fun!")
