# Numerous engineering and scientific applications require finding solutions to a set of equations. Ex: 8x + 7y = 38
# and 3x - 5y = -1 have a solution x = 3, y = 2. Given integer coefficients (a, b, c, d, e, and f) of two linear
# equations with variables x and y listed below, use brute force to find an integer solution for x and y in the range
# -10 to 10.

""" Read in first equation, ax + by = c """
a = int(input())
b = int(input())
c = int(input())

""" Read in second equation, dx + ey = f """
d = int(input())
e = int(input())
f = int(input())

z = 0


for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if (((a * x) + (b * y)) == c) and (((d * x) + (e * y)) == f):
            print(f"x = {x} , y = {y}")
            z = 1

if z == 0:
    print("There is no solution")