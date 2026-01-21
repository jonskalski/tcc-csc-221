# Complete the calc_average() function that has a float list parameter and returns the average value of the elements in the list as an integer.
# If the input list is:
#
# 1.1 2.1 3.1 4.1 5.1
# then the returned average will be:
#
# 3

def calc_average(nums):
    length = len(nums)
    average = int(sum(nums) / length)
    return average


if __name__ == "__main__":
    nums = [1.1, 2.1, 3.1, 4.1, 5.1]
    print(calc_average(nums))  # calc_average() should return 3