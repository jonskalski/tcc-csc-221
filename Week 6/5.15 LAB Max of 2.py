#Write a program that takes in two integers and outputs the larger value.
#If the two integers are the same, output the integers' value.

num_1 = int(input())
num_2 = int(input())

if num_1 > num_2:
    print("Max of",num_1,"and",num_2,"is",num_1)
elif num_2 > num_1:
    print("Max of",num_1,"and",num_2,"is",num_2)
else:
    print("Max of",num_1,"and",num_2,"is",num_1)