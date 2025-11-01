import random
print("Welcome to the Number Guessing Gaame!")
number=random.randint(1,100)
guess=0
attempts=0

while guess != number:
    guess=int(input("Enter a number(1-100):"))
    attempts=attempts+1

    if guess < number:
        print("Too low! Please try again.")
    elif guess > number:
        print("Too high! Please try again.")
    else:
        print(f"Congratulations! You guessed it in {attempts} attempts.")
