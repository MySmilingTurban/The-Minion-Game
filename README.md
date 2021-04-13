# The-Minion-Game
>Creative replacement of Toss
- Kevin and Stuart are sample players who want to play the **'The Minion Game'**.
- Player Names can be changed interactively.

##### Game Rules

- Number of players - 1 or 2
- In case of 1 player, 2nd player is Bot by default.
- Both players are given the same string,
- Both players have to make substrings using the letters of the string .
- Stuart has to make words starting with consonants.
- Kevin has to make words starting with vowels.
- The game ends when both players have made all possible substrings.

##### Scoring
A player gets +1 point for each occurrence of the substring in the string .

**For Example**:

String  = BANANA

Kevin's vowel beginning word = ANA

Here, ANA occurs twice in BANANA. 

Hence, Kevin will get 2 Points.

- For better understanding, see the image below:

![image](https://user-images.githubusercontent.com/51584037/114600652-34dde080-9cb2-11eb-92fd-099ff86883ce.png)

***Your task is to determine the winner of the game and their score.***

##### Function Description

- minion_game has the following parameters:
- string: the string to analyze

###### Prints

The Winner's name and score, separated by a space on one line, 

*OR* Draw if there is no winner

###### Input Format

- First line of input contains the string.
- Second line of input contains name of Player 1. {By default - Stuart}
- Third line of input contains name of Player 2. {By default - Kevin}

*Note*: The string will contain only uppercase letters .

##### Sample Input

BANANA
##### Sample Output

Stuart 12
