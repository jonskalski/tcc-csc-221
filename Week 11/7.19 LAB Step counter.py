# A pedometer treats walking 1 step as walking 2.5 feet. Define a function named feet_to_steps that takes a float
# as a parameter, representing the number of feet walked, and returns the number of steps walked as an integer by
# using int(). Then, write a main program that reads the number of feet walked as an input, calls function
# feet_to_steps() with the input as an argument, and outputs the number of steps returned from feet_to_steps().
#
# Use floating-point arithmetic to perform the conversion.
#
# Note: Converting a float to an integer may affect the result's accuracy.

def feet_to_steps(steps):
    distance = int(steps / 2.5)
    return distance


if __name__ == "__main__":
    steps = float(input())
    print(feet_to_steps(steps))

