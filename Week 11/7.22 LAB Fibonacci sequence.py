# The Fibonacci sequence begins with 0 and then 1 follows. All subsequent values are the sum of the previous two,
# ex: 0, 1, 1, 2, 3, 5, 8, 13. Complete the fibonacci() function, which has an index, n (starting at 0), as a
# parameter and returns the nth value in the sequence. Any negative index values should return -1.

# Note: Use a for loop and DO NOT use recursion.

def fibonacci(n):
    if n > 0:
        num1 = 0
        num2 = 1
        for i in range(n-1):
            total = num1 + num2
            num1 = num2
            num2 = total
        return total
    elif n == 0:
        return 0
    else:
        return -1


if __name__ == "__main__":
    start_num = int(input())
    print(f"fibonacci({start_num}) is {fibonacci(start_num)}")