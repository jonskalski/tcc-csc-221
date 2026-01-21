# Given class Triangle, complete the program to read and set the base and height of triangle1 and triangle2,
# determine which triangle's area is smaller, and output the smaller triangle's info, making use of Triangle's
# relevant methods.

class Triangle:

    def __init__(self):
        self.base = 0
        self.height = 0

    def set_base(self, user_base):
        self.base = user_base

    def set_height(self, user_height):
        self.height = user_height

    def get_area(self):
        area = 0.5 * self.base * self.height
        return area

    def print_info(self):
        print(f"Base: {self.base:.2f}")
        print(f"Height: {self.height:.2f}")
        print(f"Area: {self.get_area():.2f}")


if __name__ == "__main__":
    triangle1 = Triangle()
    triangle2 = Triangle()

    triangle1.base = float(input())
    triangle1.height = float(input())
    triangle2.base = float(input())
    triangle2.height = float(input())

    # TODO: Read and set base and height for triangle2 (use set_base() and set_height())

    print("Triangle with smaller area:")

    if triangle1.get_area() < triangle2.get_area():
        triangle1.print_info()
    else:
        triangle2.print_info()
