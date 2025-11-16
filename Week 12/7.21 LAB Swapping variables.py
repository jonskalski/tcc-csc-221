# Define a function named swap_values that takes four integers as parameters and swaps the first with the second,
# and the third with the fourth values. Then write a main program that reads four integers from input, calls function
# swap_values() to swap the values, and prints the swapped values on a single line separated with spaces.

# The program must define and call the following function.
# def swap_values(user_val1, user_val2, user_val3, user_val4)

def swap_values(user_val1, user_val2, user_val3, user_val4):
    temp1 = user_val1
    user_val1 = user_val2
    user_val2 = temp1

    temp2 = user_val3
    user_val3 = user_val4
    user_val4 = temp2

    return user_val1, user_val2, user_val3, user_val4

if __name__ == "__main__":
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())

    swap1, swap2, swap3, swap4 = swap_values(val1, val2, val3, val4)

    print(swap1, swap2, swap3, swap4)