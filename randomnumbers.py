import random

# Generate a random number between 1 and 100
number_to_guess = random.randint(1, 100)

print("🎲 I'm thinking of a number between 1 and 100.")
print("Try to guess it!")

# Start guessing loop
while True:
    guess = int(input("Enter your guess: "))

    if guess == number_to_guess:
        print("🎉 Correct! You guessed the number!")
        break
    elif guess > number_to_guess:
        if guess - number_to_guess <= 5:
            print("You're very close! But it's still a bit too high.")
        else:
            print("Too high!")
    else:  # guess < number_to_guess
        if number_to_guess - guess <= 5:
            print("You're very close! But it's still a bit too low.")
        else:
            print("Too low!")
