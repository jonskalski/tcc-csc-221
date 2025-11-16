# Define a function named coin_flip that returns "Heads" or "Tails" according to a random value 1 or 0.
# Assume the value 1 represents "Heads" and 0 represents "Tails". Then, write a main program that reads the
# desired number of coin flips as an input, calls function coin_flip() repeatedly according to the number of coin
# flips, and outputs the results. Assume the input is a value greater than 0.
#
# Ex: If the random seed value is 5 and the input is:
#
# 3
# the output is:
#
# Heads
# Heads
# Tails
# Note: For testing purposes, a pseudo-random number generator with a fixed seed value is used in the program. The program uses a seed value of 5 during development, but when submitted, a different seed value may be used for each test case.
#
# The program must define and call the following function:
# def coin_flip()

import random

def coin_flip():
    flip = random.randint(0,1)
    if flip == 0:
        result = "Tails"
    else:
        result = "Heads"
    return result

if __name__ == "__main__":
    random.seed(5)  # Unique seed
    number_of_flips = int(input())

    for i in range(number_of_flips):
        print(coin_flip())



