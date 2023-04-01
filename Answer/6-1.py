class Calculator:
    def __init__(self, n):
        self.n = n

    def add(self, m):
        return self.n + m

    def mul(self, m):
        return self.n * m

calculator = Calculator(3)
print(calculator.add(10))    # 13
print(calculator.add(-3))    # 0
print(calculator.mul(5))     # 15
print(calculator.mul(1 / 3)) # 1.0
