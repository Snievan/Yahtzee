from typing import List

from dices import Dices
from user_interface.score_borad import ScoreBoard
from user_interface.user_input import UserInput
from user_interface.user_output import UserOutput
from user_score import UserScore


class Yahzeet:

    max_player = 4
    rounds = 13
    roll_dice_count = 3

    users: List[UserScore]

    def __init__(self) -> None:
        self.user_input = UserInput(self.max_player)
        self.user_output = UserOutput()
        self.dice = Dices()

    def user_regist(self) -> List[str]:
        """Reigist user up to 4 members"""
        user_names = self.user_input.regist_users()
        return user_names

    def gen_scorecard(self, user_names: List[str]) -> List[UserScore]:
        """Instances users with user names"""
        users = []
        for name in user_names:
            users.append(UserScore(name))
        self.scoreboard = ScoreBoard(users)
        self.users = users

    def phase_rool_dice(self, us: UserScore) -> None:
        """Phase that user has up to 3 times to roll dices"""
        self.user_output.show_scoreboard(self.scoreboard)
        count = self.roll_dice_count
        self.user_input.start_turn(us)
        dice_selection = []
        self.dice(dice_selection)
        self.user_output.introduce_dices(self.dice)
        for i in range(count-1):
            is_select, dice_selection = self.user_input.choose_dices()
            if not is_select:
                break
            self.dice(dice_selection)
            self.user_output.introduce_dices(self.dice)

    def phase_choose_category(self, us: UserScore) -> None:
        """Phase that for user to select category. If choose is empty, will auto select possilble one."""
        self.user_output.show_scoreboard_on_choice(
            self.scoreboard, us, self.dice)

        choose: bool = False
        while not choose:
            cat_choice = self.user_input.choose_category()
            if cat_choice == -1:
                for i, is_choosable in enumerate(us.choosable):
                    if is_choosable:
                        choose = us.choose_category(i, dices=self.dice)
                        break
            else:
                choose = us.choose_category(cat_choice, dices=self.dice)
                if not choose:
                    self.user_output.cat_already_taken()

    def progress_turn(self, us: UserScore):
        """Progress players turn"""
        self.phase_rool_dice(us)
        self.phase_choose_category(us)

    def progress_round(self):
        """Progress game's round"""
        for us in self.users:
            self.progress_turn(us)

    def progress_game(self):
        """Progress 13 turns round"""
        for _ in range(self.rounds):
            self.progress_round()

    def end_game(self):
        self.user_output.show_scoreboard(self.scoreboard)
        self.user_output.end_regards()

    def run(self):
        user_names = self.user_regist()
        self.gen_scorecard(user_names)
        self.progress_game()
        self.end_game()


if __name__ == "__main__":
    game = Yahzeet()
    game.run()
