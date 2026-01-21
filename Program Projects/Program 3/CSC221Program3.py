# Program 3 - Even/Odd Calculation
# Jonathan Skalski
# 12/6/25

import random


def get_user_inputs():  # Function to set up the paramaters of the calculation
    count_nums = int(input("Enter number of values to generate: "))
    while count_nums <= 0:  # Input must be positive
        print("Please enter a positive integer.")
        count_nums = int(input("Enter number of values to generate: "))
    low_num = int(input("Enter low end of the value range: "))
    high_num = int(input("Enter high end of the value range: "))

    while low_num > high_num:  # Validates that the High number is Higher than the Low
        print("Low number must be lower than high number.")
        low_num = int(input("Enter low end of the value range: "))
        high_num = int(input("Enter high end of the value range: "))

    return count_nums, low_num, high_num


def generate_list(count_nums, low_num, high_num):  # Generates the list of random integers
    num_list = []
    for i in range(count_nums):
        rand_num = random.randint(low_num, high_num)
        num_list.append(rand_num)
    return num_list


def num_count(num_list):  # Generates the count of even and odd numbers in the list
    odd_nums = 0
    even_nums = 0

    for num in num_list:
        if num % 2 == 0:
            even_nums += 1
        else:
            odd_nums += 1

    return odd_nums, even_nums


def main():  # Main program
    total_lists = 0
    total_numbers = 0
    total_odd = 0
    total_even = 0

    again = "Y"  # Sets the main loop

    while again == "Y":
        count_nums, low_num, high_num = get_user_inputs()
        final_list = generate_list(count_nums, low_num, high_num)
        odd_nums, even_nums = num_count(final_list)
        odd_pct = odd_nums / count_nums * 100
        even_pct = even_nums / count_nums * 100

        print(f"Odd values: {odd_pct:.1f}%")
        print(f"Even values: {even_pct:.1f}%")

        total_lists += 1
        total_numbers += count_nums
        total_odd += odd_nums
        total_even += even_nums

        # Loop to prompt user for another round of numbers
        again = input("Do you want to generate a new set of values? (Y/N) ").upper()

        while again not in ("Y", "N"):
            again = input("Do you want to generate a new set of values? (Y/N) ").upper()

    print("\n--- Session Summary ---")
    print(f"Total sets generated: {total_lists}")
    print(f"Total numbers analyzed: {total_numbers}")

    if total_numbers > 0:
        total_odd_pct = total_odd / total_numbers * 100
        total_even_pct = total_even / total_numbers * 100
        print(f"Overall odd percentage: {total_odd_pct:.1f}%")
        print(f"Overall even percentage: {total_even_pct:.1f}%")
    else:  # Count of numbers must be positive
        print("No numbers were analyzed.")


if __name__ == "__main__":
    main()

