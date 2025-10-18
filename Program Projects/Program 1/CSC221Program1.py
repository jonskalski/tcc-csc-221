#Jonathan Skalski
#September 27, 2025
#This program takes user input of the number of CSC221 books purchased and calculates the tax
#and then displays that information.

import math

unit_books = int(input("How many CSC221 books were purchased? "))
unit_price = float(input("How much was each book? "))

total_price = unit_price * unit_books
tax_rate = 0.053
total_tax = (total_price * tax_rate)

total_cost = total_price + total_tax

print("You bought",unit_books,"books at $" +
      str(f"{unit_price:.2f}"),"each. The tax is $" +
      str(f"{total_tax:.2f}") + ". Your total cost is $" +
      str(f"{total_cost:.2f}") + ".")

ceiling = math.ceil(total_cost)
floor = math.floor(total_cost)
print("Ceiling is",ceiling)
print("Floor is",floor)

print(id(unit_books),id(unit_price),id(total_price),id(total_tax),id(total_cost),id(ceiling),id(floor))
