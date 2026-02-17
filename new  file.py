

# ----------Number Guessing Game-----------
print("🎲Welcome to the Number Guessing Game!")
import random
secret_number = random.randint(1,10)
number_tries = 0
while True :
    try1 = int(input("Guess a number between 1 and 10:"))
    number_tries += 1
    if try1 == secret_number :
        print(f"🎉Correct! You guessed the number in {number_tries} tries.")
        break
    elif try1 > secret_number:
        print("🔼Too high! Try again.")
    else :
        print("🔼Too low! Try again.")






















