# Write a function driving_cost() with parameters miles_per_gallon, dollars_per_gallon, and miles_driven,
# that returns the dollar cost to drive those miles. All items are of type float. The function called with
# arguments (20.0, 3.1599, 50.0) returns 7.89975.
#
# The main program's inputs are the car's miles per gallon and the price of gas in dollars per gallon (both float).
# Output the gas cost for 10 miles, 50 miles, and 400 miles, by calling your driving_cost() function three times.
#
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print(f"{your_value:.2f}")

# Your program must define and call a function:
# def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven)


def driving_cost(miles_per_gallon, dollars_per_gallon, miles_driven):
    gallons = miles_driven / miles_per_gallon
    price = gallons * dollars_per_gallon
    return price

if __name__ == "__main__":
    mpg = float(input())
    dpg = float(input())

    ten = driving_cost(mpg,dpg,10)
    fifty = driving_cost(mpg,dpg,50)
    fourhun = driving_cost(mpg,dpg,400)

    print(f"{ten:.2f}")
    print(f"{fifty:.2f}")
    print(f"{fourhun:.2f}")
