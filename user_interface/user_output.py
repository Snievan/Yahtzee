from dices import Dices
from user_score import UserScore

from user_interface.score_borad import ScoreBoard


class UserOutput:

    @staticmethod
    def introduce_dices(dice: Dices):
        for i, face in enumerate(dice.faces):
            print(f"Number {i+1} dice's face is {face}")
    @staticmethod
    def cat_already_taken():
        print("You should choose a categrory yet not taken!")

    @staticmethod
    def show_scoreboard(sb: ScoreBoard) -> None:
        sb.show_board()

    @staticmethod
    def show_scoreboard_on_choice(sb: ScoreBoard, us: UserScore, dice: Dices) -> None:
        sb.show_board_on_choice(us, dice)

    @staticmethod
    def end_regards():
        print("Congratulations! You have finished the game!")
