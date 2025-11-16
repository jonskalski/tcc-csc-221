# Function returns the multiplication and division of two numbers
def number_equation(num1,num2):
    division = num1 / num2   # Divides the two input values
    multiply = num1 * num2    # Multiplies the two input values
    return division, multiply    # Returns the division of two input values
        # Returns the multiplication of the two input values
num1 = int(input())    # Gets input value
num2 = int(input())    # Gets input value
answer = (number_equation(num1, num2)) # Assigns answer with return function values
print(answer, end=" ") # Outputs the two return functions on the same line