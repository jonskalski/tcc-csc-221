# Number Guessing Game
# Jonathan Skalski
# 10/31/2025




import random

# This sets the program to run in a loop.
play_again = "Y"


# This is the main portion of the program. This only runs when play_again is Y. If the code changes the Y to anything
# else, this while loop will stop.
while play_again == "Y":
    secret_number = random.randint(1, 50) #sets secret number
    guess_count = 0 #resets the guess count
    user_guess = 99 #sets the user guess to a number out of range of the secret number.


    # This loop inputs the user's guess. It gives the user an instant way to quit the program "0"
    while user_guess != secret_number and user_guess != 0:
        user_guess = int(input("Enter a guess 1-50, or 0 to quit: "))


        # This ensures that the user's guess is between 0 and 50. 0 gives it the ability to quit and 50 is the high.
        if user_guess < 0 or user_guess > 50:
            print("Guess must be between 1 and 50!")
        elif user_guess == 0: #quit condition
            print("Come back soon!")
            play_again = "N" #sets play again to N which ends the initial loop
        else:
            guess_count += 1 #increases guess count for each guess
            if user_guess > secret_number:
                print("Too high!")
            elif user_guess < secret_number:
                print("Too low!")
            else:
                print(f"That's it! You took {guess_count} guesses to get the number.")

    if user_guess != 0: #initiates the replay question
        play_again = "" #sets play again to null
        while play_again != "Y" and play_again != "N": #use must put in a Y or N in order to continue
            play_again = input("Would you like to play again? (Y/N): ")
    else: #sets play_again to N in the case where user input 0
        play_again = "N"

print("Thanks for playing!")