# Given two integers that represent the miles to drive forward and the miles to drive in reverse as user inputs,
# create a SimpleCar object that performs the following operations:
#
# Drives input number of miles forward
# Honks the horn
# Reports car status
# Drives input number of miles in reverse
# Honks the horn
# Reports car status


class SimpleCar:
    def __init__(self):
        self.miles = 0

    def drive(self, dist):
        self.miles = self.miles + dist

    def reverse(self, dist):
        self.miles = self.miles - dist

    def get_odometer(self):
        return self.miles

    def honk_horn(self):
        print("beep beep")

    def report(self):
        print(f"Car has driven: {self.miles} miles")


if __name__ == "__main__":
    car = SimpleCar()
    car.drive(int(input()))
    car.honk_horn()
    car.report()
    car.reverse(int(input()))
    car.honk_horn()
    car.report()
