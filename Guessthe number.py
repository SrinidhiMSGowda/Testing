import random

number = random.randint(1, 100)
print(f"(cheat: The number is {number})")
attepts = 0

print("Welcome to the Guess the Number Game!")


while True:
    guess = int(input("Enter your guess: "))
    attepts += 1
    
    if guess < number:
        print("Too low! Try again.")
    elif guess > number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You've guessed the number {number} in {attepts} attempts.")
        break