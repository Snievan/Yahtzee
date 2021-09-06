from typing import List, Union


class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def set_color(s: Union[str, int, float, List], c: str):

    def colorfy(x): return c + str(x) + Color.END
    if type(s) == list:
        return [colorfy(i) for i in s]
    return colorfy(s)
