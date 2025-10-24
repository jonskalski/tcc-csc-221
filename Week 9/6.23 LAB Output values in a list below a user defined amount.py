# Write a program that first gets a list of integers from input. The input begins with an integer indicating the number
# of integers that follow. Then, get the last value from the input, which indicates a threshold. Output all integers
# less than or equal to that last threshold value.

count = int(input())
list = []

for num in range(count):
    num = int(input())
    list.append(int(num))

biggest = int(input())

number = ""

for i in list:
    if i <= biggest:
        print(f"{i},",end="")

