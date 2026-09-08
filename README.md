# 🎯 Number Guessing Game

A simple, interactive number guessing game built in Python while learning the language fundamentals. This is one of my first real projects — a small step from "learning syntax" to "building something that runs."

## About the Project

The game greets you, asks a couple of personal questions, and then lets you pick a difficulty level before challenging you to guess a randomly generated secret number within a limited number of attempts.

Each wrong guess costs points, and your final score is multiplied based on the difficulty you chose — so higher difficulty means higher risk, but a bigger reward.

## Features

- Personalized greeting (asks your name and how you'd like to be greeted)
- Asks about your college and branch for a friendlier experience
- Three selectable difficulty levels
- Randomly generated secret number using Python's `random` module
- Limited number of attempts per game
- Score deducted for every wrong guess
- Final score calculated with a difficulty-based multiplier
- Simple performance feedback at the end (Excellent / Good / Keep practicing)

## Difficulty Levels

| Difficulty | Number Range | Attempts | Starting Score | Multiplier |
| ---------- | ------------ | -------- | --------------- | ---------- |
| Easy       | 1–200        | 15       | 150             | 1x         |
| Medium     | 1–100        | 10       | 250             | 2x         |
| Hard       | 1–50         | 5        | 400             | 3x         |

**Note:** 25 points are deducted for every wrong guess.

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/ajlan-codes/number-guessing-game.git
```

### 2. Move into the project folder

```bash
cd number-guessing-game
```

### 3. Run the game

```bash
python guessing_game.py
```

> Make sure Python 3 is installed on your system.

## Example Gameplay

```text
Hi everyone who got time to look at my first little game
We are in a number guessing game

What is your name? Ajlan
How should I greet you? Hello
Hello Ajlan!

Which college do you study at? College of Engineering Kallooppara
Which branch are you studying? CSE

I see you are from College of Engineering Kallooppara
And you're studying CSE

Are you ready to play? yes/no: yes
Awesome! Let's begin

Choose difficulty: hard, easy, or medium: hard
nice challenge!

Guess the number? 25
This is low, try again you lost 25 points

Guess the number? 38
You have won!
You used 2 attempts.
Your score is 375
Your final score is 1125
Amazing!
Great performer!
```

*Actual output will vary since the secret number is generated randomly each time.*

## Technologies Used

- Python 3
- `random` module
- `input()` for user interaction
- `if / elif / else` conditional logic
- `for` loops with `break`
- Variables and basic scoring logic

## What I Learned

Building this project helped me practice:

- Taking and using input from the user
- Storing and updating data with variables
- Writing conditional logic to branch game flow
- Generating random numbers with the `random` module
- Using loops to manage repeated attempts
- Tracking state (attempts used, score) across a loop
- Using `break` to exit a loop early on a win
- Structuring a small project from scratch, end to end

## Known Limitations

Since this is an early learning project, a few rough edges are still there on purpose — I plan to fix these as I improve:

- Entering a difficulty other than `easy`, `medium`, or `hard` isn't handled gracefully yet and will cause an error.
- Non-numeric guesses (e.g. typing letters) aren't validated and will crash the game.
- There's no input validation loop — invalid input isn't re-prompted.

## Future Improvements

- [ ] Add input validation for difficulty and guesses
- [ ] Handle invalid input without crashing
- [ ] Add a "play again" option instead of restarting the script
- [ ] Move hardcoded values (attempts, scores, multipliers) into a config/dictionary
- [ ] Add unit tests for the scoring logic

## About Me

I'm a first-year Computer Science student learning Python and exploring programming through small, hands-on projects like this one. This is one of my first steps into coding, and I'm excited to keep learning and building.

## Repository

[View the project on GitHub](https://github.com/ajlan-codes/number-guessing-game)

## License

This project is licensed under the MIT License — you're free to use, copy, modify, and distribute it, including for commercial purposes, as long as the original copyright notice is included.

Copyright (c) 2026 ajlan-codes