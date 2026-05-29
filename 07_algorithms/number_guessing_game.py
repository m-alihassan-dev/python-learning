import random

number = random.randint(1, 100)
attempts = 0

print("🎯 Welcome to the Number Guessing Game!")
print("Guess a Number between 1 and 100")

while True:
    guess = input("Enter Your Guess: ")

    if not guess.isdigit():
        print("Please Enter a Valid Number.")
        continue

    guess = int(guess)
    attempts += 1

    if guess < 1 or guess > 100:
        print("Number Out of Range! Try Between 1 and 100.")
    elif guess == number:
        print(f"Congratulations! You Guessed it in {attempts} Attempts.")
        break
    elif guess > number:
        print("Too high! Go a Little Lower.")
    else:
        print("Too low! Go a Little Higher.")