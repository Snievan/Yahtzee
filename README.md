
# Yahzeet Game
Run this game in vscode terminal with command "python .\yahzeet.py"
## Player Operation
### Player Register Phase
Input each player's name one by on following ths instruction. 
Press an empty enter to finish this phase.

### Roll Dice Phase
Enter the Dice number you want to reroll.
Inpur seperated by space. For example "1 3 5"
Press an empty enter to keep all the dice and step to next phase.

### Choose Category phase
Enter the Category number you want to choose.
Press an empty enter, will make system automaticly select one for you.


## Rules
Each turn player roll dice(up to 3 times), then choose an category.
Game will continue 13 rounds for all categories to be selected.
Bonus Rule:  If the sum of the score 1-6 reach 63, player will get an extra 35 points.

|      | Catorory      | Score method    | Example   | Example score |
| ---: | :------------ | :-------------- | :-------- | ------------: |
|    0 | Aces          | Sum of dice 1   | 1-1-1-3-4 |             3 |
|    1 | Twos          | Sum of dice 2   | 2-2-2-5-6 |             6 |
|    2 | Threes        | Sum of dice 3   | 3-3-3-3-4 |            12 |
|    3 | Fours         | Sum of dice 4   | 4-4-5-5-5 |             8 |
|    4 | Fives         | Sum of dice 5   | 1-1-2-2-5 |             5 |
|    5 | Sixes         | Sum of dice 6   | 3-3-6-6-6 |            18 |
|    6 | ThreeOFaKind  | Sum of all dice | 2-3-4-4-4 |            17 |
|    7 | FourOfaKind   | Sum of all dice | 4-5-5-5-5 |            24 |
|    8 | FullHouse     | 25              | 2-2-5-5-5 |            25 |
|    9 | SmallStraight | 30              | 1-3-4-5-6 |            30 |
|   10 | LargeStraight | 40              | 1-2-3-4-5 |            40 |
|   11 | Yahtzee       | 50              | 3-3-3-3-3 |            50 |
|   12 | Chance        | Sum of all dice | 1-1-3-4-5 |            14 |

For more detailed info, visit site below
https://en.wikipedia.org/wiki/Yahtzee


## Dependency 
python libs:
- tabulate
- pandas
- numpy