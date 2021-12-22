import random

MIN_NUMBER = 1
MAX_NUMBER = 100

number_to_guess = random.randint(MIN_NUMBER, MAX_NUMBER)

should_continue = True
while should_continue:

    player_guess = int(input("What is the number? "))

    if player_guess == number_to_guess:
        print("Awesome, you got it!")
        should_continue = False
    else:
        if player_guess < number_to_guess:
            print("You guessed too low.  Try a higher number.")
        else:
            print("You guessed too high.  Try a lower number.")
