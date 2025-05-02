# Guess the Number

A simple, console-based Python game where the computer picks a secret number and you try to guess it in three attempts.

## Description

This script implements a “Guess the Number” game:

1. On each of three attempts, it uses `random.randint(1, 5)` to generate a new secret number between 1 and 5.  
2. It prompts you with`Guess the number between 1 and 5? :) Attempts: X/3 -->`where `X` is the current attempt (1–3).  
3. You enter a guess (integer).  
4. If your guess matches the secret, it prints `Correct! 🎉 That’s right! You win!` and the game ends immediately.  
5. Otherwise it prints `Sorry :( Try again!` and moves on to the next attempt.  
6. If all three attempts fail, it reveals the last generated number:  
