import random

def play_guessing_game ():
    for attempts in range (1, 4):
        number = random.randint(1, 5)
        answer = int(input(f"Guess the number between 1 and 5? :) Attempts: {attempts}/3 --> "))
        if answer == number:
            print("Correct! 🎉 That’s right! You win!")
            return
        else:
            print("Sorry :( Try again!")
    print(f"Game over! The Number was {number}")

if __name__ == "__main__":
    play_guessing_game()