#Write a program that takes in three integers and outputs the largest value.
#If the input integers are the same, output the integers' value.

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())

max_val = 0


if ((num_1 > num_2) and (num_1 > num_3)):
    max_val = num_1
if ((num_2 > num_3) and (num_2 > num_1)):
    max_val = num_2
if ((num_3 > num_1) and (num_3 > num_2)):
    max_val = num_3
if (num_1 == num_2 == num_3):
    max_val = num_1

print(f"Max of [{num_1}, {num_2}, {num_3}] is {max_val}")