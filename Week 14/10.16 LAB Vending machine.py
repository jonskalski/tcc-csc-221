# Given three integers as user inputs that represent the number of bottles of drinks to purchase, to restock,
# and to purchase afterward, create a VendingMachine object that performs the following operations:
#
# Purchase the first input number of bottles of drinks
# Restock the second input number of bottles of drinks
# Purchase the last input number of bottles of drinks
# Report inventory
# A VendingMachine's initial inventory is 20 bottles of drinks.

class VendingMachine:

    def __init__(self):
        self.bottles = 20

    def purchase(self, amount):
        self.bottles = self.bottles - amount

    def restock(self, amount):
        self.bottles = self.bottles + amount

    def get_inventory(self):
        return self.bottles

    def report(self):
        print(f"Inventory: {self.bottles} bottles")


if __name__ == "__main__":
    vending = VendingMachine()
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    vending.purchase(num1)
    vending.restock(num2)
    vending.purchase(num3)
    vending.report()
    # TODO: Purchase first input number of bottles of drinks
    # TODO: Restock second input number of bottles of drinks
    # TODO: Purchase last input number of bottles of drinks
    # TODO: Report inventory