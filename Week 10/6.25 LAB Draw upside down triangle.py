# Write a program that outputs a right triangle of asterisks given the height as input. Each line ends with a blank space.

triangle = int(input())

for i in range(triangle, 0, -1):
    for j in range(i):
        print(f"*",end=" ")
        triangle -= 1
    print()