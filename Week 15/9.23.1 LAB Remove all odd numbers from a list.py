# Write the remove_odds() function, which receives a list of integers as a parameter and returns a new list of
# integers containing only the even numbers from the original list. The main program outputs values of the
# returned list.
#
# Hint: If the original list has odd numbers, then the new list will be smaller in length than the original list
# and should have no blank elements.
#
# Ex: If the list passed to the remove_odds() function is [1, 2, 3, 4, 5, 6, 7, 8, 9], then the function returns
# and the program output is:
#
# [2, 4, 6, 8]



# Ex: If the list passed to the remove_odds() function is [2, 8, 6], then the function returns and the program
# output is:
#
# [2, 8, 6]
#


def remove_odds(nums):
    new_nums = []
    for i in nums:
        if i % 2 == 0:
            new_nums.append(i)
    return new_nums


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    result = remove_odds(nums)

    print(result)

