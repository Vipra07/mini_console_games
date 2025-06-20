import art
import random
print(art.logo)
print("Welcome to the Number Guessing Game!")
numbers = []
for i in range(1,101):
    numbers.append(i)

num = random.choice(numbers)
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "hard":
    attempts = 5
else:
    attempts = 10
game_over = False
while not game_over:
    guess = int(input("Make a Guess: "))
    attempts -= 1
    if attempts > 0:
        if guess > num:
            print("Too high")
            print("Guess Again")
            print(f"You have {attempts} attempts left")
        elif guess < num:
            print("Too low")
            print("Guess Again")
            print(f"You have {attempts} attempts left")
        else:
            print(f"You Got It! The answer was {num}")
            game_over = True
    elif attempts == 0:
        if guess == num:
            print(f"You Got It! The answer was {num}")
        else:
            print("You've run out of attempts. Play again!")
        game_over = True
