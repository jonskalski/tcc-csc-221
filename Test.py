class Factorial:
    def __init__(self, num1 = 5):
        self.num1= num1
    def calculate_fact(self):
        fact = 1
        for i in range(1, self.num1 + 1):
            fact *= i
        print(fact)
fact1 = Factorial(2)
fact1.calculate_fact()