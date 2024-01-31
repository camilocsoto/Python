![](https://tinypic.host/images/2024/01/31/icon_better.png){height='180px'}
------------
### Features

- Implements a simple text-based game of rock, paper, scissors.
- Imports the `random` module for generating random choices for the computer player.
- Defines functions:
  - `computer_choice()`: Generates a random choice for the computer player from predefined options.
  - `user_choice()`: Takes and validates user input for the player's choice (rock, paper, or scissors).
  - `run_game()`: Manages the game flow, including rounds, user and computer choices, and determines the winner.
- Uses a global tuple `options` containing the game choices ("rock", "paper", "scissors").
- Executes the game logic when the script is run (`if __name__ == "__main__":`).
- Handles user input using the `input()` function, converting it to lowercase for case-insensitivity.
- Raises an exception if the user's input is not a valid option.
- Utilizes conditional statements to compare user and computer choices and determine the winner of each round.
- Prints messages indicating the result of each round and the final outcome of the game.
- Terminates the game when the specified number of rounds is completed, declaring the winner.
- Includes comments to explain the purpose of functions and provide context for certain code blocks.

------------
## How run the game:

Follow the next steps:
```sh
cd game
python3 rps.py

```
------------
# View of player:
![](https://tinypic.host/images/2024/01/31/view.png)
