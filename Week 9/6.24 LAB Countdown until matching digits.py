# Write a program that takes in an integer in the range 11-99 (inclusive) as input. The output of the program is a
# countdown starting from the input integer until an integer where both digits are identical.

num = int(input())


if num < 11 or num > 99:
    print("Input must be 11-99")
else:
    while num >= 11:
        print(num)
        ten = num // 10
        one = num % 10
        if ten == one:
            break
        num -= 1
