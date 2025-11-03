# Number Guessing Game
# Jonathan Skalski
# 10/31/2025

# This program generates a random number between 1 and 50 and asks the user to guess it.
# After a guess, the program tells the user if they are too high or low.
# If at any time, the user wants to quit, they just guess 0 to stop the program.
# Once the user guesses the right number, the program displays the number of guesses.
# After the round is done, the user is asked if they want to play again.
# The user MUST input a whole number between 0 and 50 in order to provide a valid guess.
# Other inputs will prompt the user to try again.
# If the user wants to replay, they must choose Y or N (caps).



import random

# This sets the program to run in a loop
play_again = "Y"

# This is the main portion of the program. This only runs when play_again is Y. If the code changes the Y
# to anything else, this while loop will stop.
while play_again == "Y":
    print() # inserts a line break between games, I didn't like how it looked when you play again
    print("New game starting...") #
    secret_number = random.randint(1,50) # sets the secret Number
    guess_count = 0 # resets the guess count
    user_guess = 99 # sets the user guess to a number outside the range of the secret number

    # this loop inputs the user's guess. It also gives the user an instant way to quit the program
    # with "0"
    while user_guess != secret_number and user_guess != 0:
        user_string = input("Enter a guess 1-50, or 0 to quit: ") # string because we need to validate

        valid = "valid" # defining valid in order to make sure that the input is a valid number

        for i in user_string: # looks at each character in the input to check for validity (number)
            if i < "0" or i > "9": # any character outside of the set of numbers
                valid = "not" # allows the reinput of proper numbers

        if valid == "not":
            print("Please enter a valid number.")
            continue # if the user has input an invalid input, sends them back to do it right

        user_guess = int(user_string)

        # this ensures that the user's guess is between 0 and 50. 0 is the quit statement and 50 is the high
        if user_guess < 0 or user_guess > 50:
            print("Guess must be between 1 and 50!")
        elif user_guess == 0: # allows the user to complete the quit condition
            print("Come back soon!")
            play_again = "N" # sets play_again to N which ends the initial loop
        else:
            guess_count += 1 # increases the guess count for each guess
            if user_guess > secret_number:
                print("Too high!")
            elif user_guess < secret_number:
                print("Too low!")
            else:
                print(f"That's it! You took {guess_count} guesses to get the number.")

    if user_guess != 0: # initiates the replay question
        play_again = "" # sets play again to null
        while play_again != "Y" and play_again != "N": # user must put in Y or N to continue
            play_again = input("Would you like to play again? (Y/N): ")
    else: # sets play_again to N in the case where user input is 0
        play_again = "N"

print("Thanks for playing!")
