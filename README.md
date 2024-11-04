# Lesson 15: Command Line Arguments

## Learn Python fast with some content ideas

Learning Python is a great choice, especially given your interest in web development, mobile app development, and software engineering. Here are some excellent resources to get you started:

**1. LearnPython.org:** This interactive Python tutorial offers free lessons for beginners. It covers topics like variables, loops, functions, and more. You can even get certified after completing the [`tutorials[1]`](https://www.learnpython.org/).

**2. Python Official Documentation:** The official Python documentation provides comprehensive information about the language. Start with the Python Tutorial for beginners and explore further as you gain [`confidence[2]`](https://stackoverflow.com/questions/70577/best-online-resource-to-learn-python).

**3. freeCodeCamp’s Python Courses:**
**- [`Full Course for Beginners`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/):** This YouTube course covers programming basics, including lists, conditionals, strings, and small projects like a calculator and a guessing game.
**- [`The Ultimate Python Beginner’s Handbook`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/)** Dive deeper into Python concepts and explore its growing popularity [`3`](https://www.freecodecamp.org/news/learn-python-free-python-courses-for-beginners/) and [`4`](https://www.freecodecamp.org/news/the-python-guide-for-beginners/).

**REMEMBER:** practice coding regularly, work on small projects, and explore real-world examples.

## What is Command Line Arguments in Python?

Command line arguments in Python are parameters that you can pass to your Python script when you run it from the command line. These arguments allow you to influence the behavior of the script without changing the code.

Here's a step-by-step explanation:

1. **Writing the Script**: You write a Python script that can accept command line arguments.
2. **Using `argparse` Module**: Python provides a built-in module called `argparse` to handle command line arguments.
3. **Defining Arguments**: You define what arguments your script can accept using `argparse.ArgumentParser`.
4. **Parsing Arguments**: The `parse_args()` method of `ArgumentParser` parses the arguments passed to the script.
5. **Using Arguments**: You can then use these parsed arguments in your script.

### Example

Here's a simple example to illustrate:

```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple example script.")

# Add arguments
parser.add_argument("name", type=str, help="The name of the person to greet.")
parser.add_argument("-a", "--age", type=int, help="The age of the person.")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
```

### Running the Script

You can run this script from the command line and pass arguments to it:

```sh
python script.py John -a 30
```

### Output

```
Hello, John!
You are 30 years old.
```

In this example:

- `name` is a positional argument, which means it is required.
- `-a` or `--age` is an optional argument, which means it is not required but can be provided.

Command line arguments are useful for making your scripts more flexible and reusable.

## How can I handle command line arguments in Python scripts?

To handle command line arguments in Python scripts, you can use the [`argparse`] module, which provides a way to define and parse command line arguments. Here’s a step-by-step guide using the provided [`main.py`] example:

### Step-by-Step Guide

1. **Import the [`argparse`] Module**: This module helps in creating a parser object to handle command line arguments.
2. **Create a Parser Object**: Use [`argparse.ArgumentParser`] to create a parser object.
3. **Define Arguments**: Use the [`add_argument`] method to specify what command line arguments your script accepts.
4. **Parse the Arguments**: Use the [`parse_args`] method to parse the arguments passed to the script.
5. **Use the Parsed Arguments**: Access the parsed arguments using the attributes of the object returned by [`parse_args`].

### Example

Here’s the provided [`main.py`] script with explanations:

```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple example script.")

# Add arguments
parser.add_argument("name", type=str, help="The name of the person to greet.")
parser.add_argument("-a", "--age", type=int, help="The age of the person.")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Hello, {args.name}!")
if args.age:
    print(f"You are {args.age} years old.")
```

### Explanation

1. **Import `argparse`**:

   ```python
   import argparse
   ```

2. **Create the Parser**:

   ```python
   parser = argparse.ArgumentParser(description="A simple example script.")
   ```

   This creates a parser object with a description of the script.

3. **Add Arguments**:

   ```python
   parser.add_argument("name", type=str, help="The name of the person to greet.")
   parser.add_argument("-a", "--age", type=int, help="The age of the person.")
   ```

   - `name`: A positional argument (required).
   - `-a` or `--age`: An optional argument.

4. **Parse the Arguments**:

   ```python
   args = parser.parse_args()
   ```

   This parses the command line arguments and stores them in the `args` object.

5. **Use the Parsed Arguments**:
   ```python
   print(f"Hello, {args.name}!")
   if args.age:
       print(f"You are {args.age} years old.")
   ```
   This prints a greeting using the parsed arguments.

### Running the Script

To run the script with the name "John" and age "30", use:

```sh
python main.py John -a 30
```

### Output

```
Hello, John!
You are 30 years old.
```

This is how you handle command line arguments in Python scripts using the [`argparse`] module.

## How can I handle optional command line arguments in Python scripts?

To handle optional command line arguments in Python scripts, you can use the `argparse` module. Optional arguments are specified with a `-` or `--` prefix and can have default values or be omitted entirely.

### Step-by-Step Guide

1. **Import the `argparse` Module**: This module helps in creating a parser object to handle command line arguments.
2. **Create a Parser Object**: Use `argparse.ArgumentParser` to create a parser object.
3. **Define Optional Arguments**: Use the `add_argument` method to specify optional command line arguments.
4. **Parse the Arguments**: Use the `parse_args` method to parse the arguments passed to the script.
5. **Use the Parsed Arguments**: Access the parsed arguments using the attributes of the object returned by `parse_args`.

### Example

Here’s an example script demonstrating how to handle optional command line arguments:

```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A script to demonstrate optional arguments.")

# Add optional arguments
parser.add_argument("-n", "--name", type=str, help="The name of the person to greet.")
parser.add_argument("-a", "--age", type=int, help="The age of the person.", default=0)

# Parse the arguments
args = parser.parse_args()

# Use the arguments
if args.name:
    print(f"Hello, {args.name}!")
else:
    print("Hello, World!")

if args.age:
    print(f"You are {args.age} years old.")
else:
    print("Age not provided.")
```

### Explanation

1. **Import `argparse`**:

   ```python
   import argparse
   ```

2. **Create the Parser**:

   ```python
   parser = argparse.ArgumentParser(description="A script to demonstrate optional arguments.")
   ```

   This creates a parser object with a description of the script.

3. **Add Optional Arguments**:

   ```python
   parser.add_argument("-n", "--name", type=str, help="The name of the person to greet.")
   parser.add_argument("-a", "--age", type=int, help="The age of the person.", default=0)
   ```

   - `-n` or `--name`: An optional argument for the name.
   - `-a` or `--age`: An optional argument for the age with a default value of 0.

4. **Parse the Arguments**:

   ```python
   args = parser.parse_args()
   ```

   This parses the command line arguments and stores them in the `args` object.

5. **Use the Parsed Arguments**:

   ```python
   if args.name:
       print(f"Hello, {args.name}!")
   else:
       print("Hello, World!")

   if args.age:
       print(f"You are {args.age} years old.")
   else:
       print("Age not provided.")
   ```

   This prints a greeting using the parsed arguments. If the name is not provided, it defaults to "World". If the age is not provided, it defaults to 0.

### Running the Script

To run the script with the name "John" and age "30", use:

```sh
python script.py -n John -a 30
```

To run the script with only the name "John", use:

```sh
python script.py -n John
```

To run the script without any optional arguments, use:

```sh
python script.py
```

### Output

For `python script.py -n John -a 30`:

```
Hello, John!
You are 30 years old.
```

For `python script.py -n John`:

```
Hello, John!
Age not provided.
```

For `python script.py`:

```
Hello, World!
Age not provided.
```

This is how you handle optional command line arguments in Python scripts using the `argparse` module.

To reflect the guidance provided in the script you shared, you can make a few adjustments to ensure it aligns with the example provided. Specifically, you need to handle the optional [`age`] argument correctly and ensure the script runs as expected.

Here is the updated version of your script:

```python
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 10:58:04 2024

@author: chien
"""

import argparse

# Create the parser
parser = argparse.ArgumentParser(description="A simple example script.")

# Add arguments
parser.add_argument("name", type=str, help="The name of the person to greet.")
parser.add_argument("-a", "--age", type=int, help="The age of the person.", default=None)

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Hello, {args.name}!")
if args.age is not None:
    print(f"You are {args.age} years old.")
else:
    print("Age not provided.")
```

### Explanation of Changes

1. **Removed Unnecessary Comments**: Removed the commented-out code to clean up the script.
2. **Default Value for Age**: Added `default=None` to the `age` argument to explicitly handle the case where the age is not provided.
3. **Simplified Conditional Check**: Changed the condition to check if `args.age` is not `None` to handle the optional argument correctly.

### Running the Script

To run the script with the name "Sisovin" and age "52", use:

```sh
python main.py Sisovin -a 52
```

### Expected Output

```
Hello, Sisovin!
You are 52 years old.
```

To run the script with only the name "Sisovin", use:

```sh
python main.py Sisovin
```

### Expected Output

```
Hello, Sisovin!
Age not provided.
```

This ensures that the script handles the optional `age` argument correctly and provides the expected output based on the provided command line arguments.

## What are some common use cases for using command line arguments in Python scripts?

Command line arguments in Python scripts are commonly used for a variety of purposes. Here are some typical use cases:

1. **Configuration and Settings**:

   - Allow users to specify configuration options or settings without modifying the script.
   - Example: [`python script.py --config config.yaml`]

2. **Input and Output File Paths**:

   - Specify input and output file paths for processing data.
   - Example: [`python script.py input.txt output.txt`]

3. **Enabling or Disabling Features**:

   - Toggle features on or off using flags.
   - Example: [`python script.py --verbose`]

4. **Specifying Parameters for Algorithms**:

   - Pass parameters to algorithms or functions, such as learning rates or thresholds.
   - Example: [`python script.py --learning-rate 0.01 --epochs 50`]

5. **Automation and Scripting**:

   - Automate tasks by passing arguments to scripts in batch processing or cron jobs.
   - Example: `python backup.py --destination /backup`

6. **Debugging and Development**:

   - Enable debugging modes or specify development environments.
   - Example: [`python script.py --debug`] or [`python script.py --env development`]

7. **User Authentication and Authorization**:

   - Pass user credentials or tokens for authentication.
   - Example: [`python script.py --username user --password pass`]

8. **Data Filtering and Selection**:

   - Filter or select specific data to process.
   - Example: [`python script.py --filter "date > '2023-01-01'"`]

9. **Version and Help Information**:
   - Provide version information or help messages.
   - Example: [`python script.py --version`] or [`python script.py --help`]

### Example Script with Various Use Cases

```python
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Example script with various use cases for command line arguments.")

# Add arguments
parser.add_argument("input_file", type=str, help="Path to the input file.")
parser.add_argument("output_file", type=str, help="Path to the output file.")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
parser.add_argument("--learning-rate", type=float, default=0.01, help="Learning rate for the algorithm.")
parser.add_argument("--epochs", type=int, default=10, help="Number of epochs for training.")
parser.add_argument("--username", type=str, help="Username for authentication.")
parser.add_argument("--password", type=str, help="Password for authentication.")
parser.add_argument("--filter", type=str, help="Filter criteria for data processing.")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Input File: {args.input_file}")
print(f"Output File: {args.output_file}")
if args.verbose:
    print("Verbose mode enabled.")
print(f"Learning Rate: {args.learning_rate}")
print(f"Epochs: {args.epochs}")
if args.username and args.password:
    print(f"Authenticated as {args.username}")
if args.filter:
    print(f"Filter: {args.filter}")
```

### Running the Script

```sh
python script.py input.txt output.txt --verbose --learning-rate 0.01 --epochs 50 --username user --password pass --filter "date > '2023-01-01'"
```

### Output

```
Input File: input.txt
Output File: output.txt
Verbose mode enabled.
Learning Rate: 0.01
Epochs: 50
Authenticated as user
Filter: date > '2023-01-01'
```

This example demonstrates how command line arguments can be used for various purposes, making scripts more flexible and user-friendly.

Great! Let's generate some unit tests for the `decide_winner` function within your `rps` game.

### Plan

1. Create a test file named `test_game_rps.py`.
2. Import the necessary modules and the `decide_winner` function.
3. Write test cases for each possible outcome:
   - Player wins.
   - Computer wins.
   - Tie game.

### Code

```python
# test_game_rps.py
import unittest
from game_rps import rps

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.game = rps('TestPlayer')
        self.decide_winner = self.game.__closure__[0].cell_contents.__closure__[1].cell_contents

    def test_player_wins_with_rock(self):
        result = self.decide_winner(1, 3)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_paper(self):
        result = self.decide_winner(2, 1)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_scissors(self):
        result = self.decide_winner(3, 2)
        self.assertEqual(result, "🎉 You win!")

    def test_computer_wins_with_rock(self):
        result = self.decide_winner(3, 1)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_paper(self):
        result = self.decide_winner(1, 2)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_scissors(self):
        result = self.decide_winner(2, 3)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_tie_game_with_rock(self):
        result = self.decide_winner(1, 1)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_paper(self):
        result = self.decide_winner(2, 2)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_scissors(self):
        result = self.decide_winner(3, 3)
        self.assertEqual(result, "😲 Tie game!")

if __name__ == "__main__":
    unittest.main()
```

### Explanation

- **Imports**: Import `unittest` and the `rps` function from `game_rps`.
- **Setup**: Initialize the game and extract the `decide_winner` function.
- **Test Cases**: Cover all possible outcomes for the game.

You can run these tests using the following command in your terminal:

```sh
python -m unittest test_game_rps.py
```

The error indicates that the [`self.game`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Ftest_game_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A5%2C%22character%22%3A14%7D%5D 'test_game_rps.py') object is not structured as expected, leading to an `AttributeError` when trying to access `__closure__`. This suggests that the [`rps`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Fgame_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A12%2C%22character%22%3A4%7D%5D 'game_rps.py') function does not return a closure or the expected structure.

To fix this, let's assume that [`decide_winner`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Ftest_game_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A7%2C%22character%22%3A13%7D%5D 'test_game_rps.py') is a method within the [`rps`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Fgame_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A12%2C%22character%22%3A4%7D%5D 'game_rps.py') class or function. We need to adjust the test setup to correctly access [`decide_winner`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Ftest_game_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A7%2C%22character%22%3A13%7D%5D 'test_game_rps.py').

### Plan

1. Ensure [`decide_winner`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Ftest_game_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A7%2C%22character%22%3A13%7D%5D 'test_game_rps.py') is accessible directly from the [`rps`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Fgame_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A12%2C%22character%22%3A4%7D%5D 'game_rps.py') instance.
2. Update the test setup to correctly reference [`decide_winner`](command:_github.copilot.openSymbolFromReferences?%5B%7B%22%24mid%22%3A1%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Ftest_game_rps.py%22%2C%22scheme%22%3A%22file%22%7D%2C%7B%22line%22%3A7%2C%22character%22%3A13%7D%5D 'test_game_rps.py').

### Updated Code

```python
# test_game_rps.py
import unittest
from game_rps import rps

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.game = rps('TestPlayer')
        self.decide_winner = self.game.decide_winner  # Adjust this line based on actual implementation

    def test_player_wins_with_rock(self):
        result = self.decide_winner(1, 3)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_paper(self):
        result = self.decide_winner(2, 1)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_scissors(self):
        result = self.decide_winner(3, 2)
        self.assertEqual(result, "🎉 You win!")

    def test_computer_wins_with_rock(self):
        result = self.decide_winner(3, 1)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_paper(self):
        result = self.decide_winner(1, 2)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_scissors(self):
        result = self.decide_winner(2, 3)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_tie_game_with_rock(self):
        result = self.decide_winner(1, 1)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_paper(self):
        result = self.decide_winner(2, 2)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_scissors(self):
        result = self.decide_winner(3, 3)
        self.assertEqual(result, "😲 Tie game!")

if __name__ == "__main__":
    unittest.main()
```

### Explanation

- **setUp Method**: Adjusted to directly access `decide_winner` from the `rps` instance.
- **Test Cases**: Remain the same, assuming `decide_winner` is a method of the `rps` instance.

Ensure that the `rps` function or class in `game_rps.py` has a `decide_winner` method accessible in this manner. If `decide_winner` is not directly accessible, you may need to adjust the implementation of `rps` accordingly.

To integrate the unit tests with your existing code, you need to ensure that the `decide_winner` function is accessible for testing. Since `decide_winner` is defined inside the `play_rps` function, you can modify the `rps` function to return `decide_winner` for testing purposes.

Here's how you can adjust your code:

1. Modify the `rps` function to return `decide_winner` when called with a specific argument (e.g., `test=True`).
2. Update your test file to use this modified `rps` function.

### Updated [`game_rps.py`](command:_github.copilot.openRelativePath?%5B%7B%22scheme%22%3A%22file%22%2C%22authority%22%3A%22%22%2C%22path%22%3A%22%2Fd%3A%2FlearnPython%2FLesson15%2Fgame_rps.py%22%2C%22query%22%3A%22%22%2C%22fragment%22%3A%22%22%7D%5D 'd:\\learnPython\Lesson15\game_rps.py')

```python
import sys
import random
from enum import Enum
from turtle import title

print("")

def rps(name='PlayerOne', test=False):
    game_count = 0
    player_wins = 0
    computer_wins = 0

    def decide_winner(player, computer):
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins
        if player == 1 and computer == 3:
            player_wins += 1
            return "🎉 You win!"
        elif player == 2 and computer == 1:
            player_wins += 1
            return "🎉 You win!"
        elif player == 3 and computer == 2:
            player_wins += 1
            return "🎉 You win!"
        elif player == computer:
            return "😲 Tie game!"
        else:
            computer_wins += 1
            return f"🐍 Computer wins!\nSorry, {name}..😢"

    if test:
        return decide_winner

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal computer_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        title = " Game: Rock, Paper, Scissors (RPS) ".upper()
        print(title.center(50, "" + ("=") + ""))
        print('')
        print("Welcome to the game of Rock, Paper, Scissors (RPS)!")

        print("")
        # Top Section of the Menu
        line01 = "*************************************************************"
        line02 = "*                                                           *"
        line03 = "* Enter...                                                  *"
        line04 = "* 1 for Rock,                                               *"
        line05 = "* 2 for Paper, or                                           *"
        line06 = "* 3 for scissors                                            *"
        line07 = "*                                                           *"
        # Bottom Section of the Menu
        line08 = "* Would you like to play again?                             *"
        line09 = "* Y for Yes, if you want to stop, type: Q                   *"
        line10 = "* Q to Quit                                                 *"
        print("")

        print(f"Hello, {name}! Let's play Rock, Paper, Scissors (RPS)!")
        print("")

        playerchoice = input(f" " + line01 + "\n " + line02 + "\n " + line03 + "\n " + line04 + "\n " + line05 + "\n " + line06 + "\n " + line07 + "\n " + line01 + "\n\n Enter your choice: ")

        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, You must enter 1, 2, or 3.")
            return play_rps()
        print("")

        player = int(playerchoice)
        if player < 1 or player > 3:
            print("Invalid input. Please try again.")
            sys.exit("You must enter a number:\n\n 1, 2, or 3.")

        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print("")
        print(f"\n{name}, You chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(
            f"Computer chose {str(RPS(computer)).replace('RPS.', '').title()}.\n"
        )
        print("")

        game_result = decide_winner(player, computer)

        print("")
        print(game_result)
        print("")

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: {str(game_count)}")
        print(f"\nPlayer Wins: {str(player_wins)}")
        print(f"\nComputer Wins: {str(computer_wins)}")
        print(f"\nPlayer and Computer Tie: {str(game_count - player_wins - computer_wins)}")

        print(f"\nPlay again, {name}?")

        while True:
            playagain = input(" " + line01 + "\n " + line08 + "\n " + line09 + "\n " + line10 + "\n " + line01 + "\n\n Enter your choice: ")
            if playagain.lower() not in ["y", "q"]:
                print("Invalid input. Please try again.")
                continue
            else:
                break

        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n 🎉🎉🎉🎉 \n")

            title = " End Game: Rock, Paper, Scissors (RPS) ".upper()
            print(title.center(50, "" + ("=") + ""))
            print ("Thank you for playing the game of Rock, Paper, Scissors (RPS)!")
            print ("")
            sys.exit(f"Bye! Bye! Bye! {name}! 👋👋👋 \n\n")
    return play_rps

if __name__ == "__main__":
    import argparse

    # Create the parser
    parser = argparse.ArgumentParser(
      description="Provides a personalized game experience."
    )

    # Add arguments
    parser.add_argument(
      "-n", "--name", metavar="name",
      required=True, help="The name of the person is playing the game."
    )

    args = parser.parse_args()

    # Use the arguments
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
```

### Updated `test_game_rps.py`

```python
import unittest
from game_rps import rps

class TestRPSGame(unittest.TestCase):
    def setUp(self):
        self.decide_winner = rps('TestPlayer', test=True)

    def test_player_wins_with_rock(self):
        result = self.decide_winner(1, 3)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_paper(self):
        result = self.decide_winner(2, 1)
        self.assertEqual(result, "🎉 You win!")

    def test_player_wins_with_scissors(self):
        result = self.decide_winner(3, 2)
        self.assertEqual(result, "🎉 You win!")

    def test_computer_wins_with_rock(self):
        result = self.decide_winner(3, 1)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_paper(self):
        result = self.decide_winner(1, 2)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_computer_wins_with_scissors(self):
        result = self.decide_winner(2, 3)
        self.assertEqual(result, "🐍 Computer wins!\nSorry, TestPlayer..😢")

    def test_tie_game_with_rock(self):
        result = self.decide_winner(1, 1)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_paper(self):
        result = self.decide_winner(2, 2)
        self.assertEqual(result, "😲 Tie game!")

    def test_tie_game_with_scissors(self):
        result = self.decide_winner(3, 3)
        self.assertEqual(result, "😲 Tie game!")

if __name__ == "__main__":
    unittest.main()
```

### Explanation

- **`rps` Function**: Modified to return `decide_winner` when called with `test=True`.
- **Unit Tests**: Updated to use the modified `rps` function to get the `decide_winner` function for testing.
