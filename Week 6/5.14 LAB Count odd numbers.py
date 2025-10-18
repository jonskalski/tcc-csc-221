#Write a program that takes in four positive integers and outputs the number of odd numbers.
#(Hint: use the modulo operator to determine if a number is odd)

num_1 = int(input())
num_2 = int(input())
num_3 = int(input())
num_4 = int(input())

count = 0

count = count + 1 if (num_1 % 2 != 0) else count
count = count + 1 if (num_2 % 2 != 0) else count
count = count + 1 if (num_3 % 2 != 0) else count
count = count + 1 if (num_4 % 2 != 0) else count

print(count)
