# Write a program that repeatedly reads in integers until a negative integer is read. The program also keeps track of
# the largest integer that has been read so far and outputs the largest integer at the end.

num1 = int(input())
num_max = 0

while num1 >= 0:
    if num1 > num_max:
        num_max = num1
    num1 = int(input())

print(f"Largest integer: {num_max}")
