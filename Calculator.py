class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def power(self, a, b):
        return a ** b

    def remainder(self, a, b):
        return a % b


def main():
    calc = Calculator()
    a = int(input("Enter a number: "))
    op = input("Enter an operator: ")
    b = int(input("Enter another number: "))
    if op == "+":
        print(a, " + ", b, " = ", calc.add(a, b))
    elif op == "-":
        print(a, " - ", b, " = ", calc.subtract(a, b))
    elif op == "*":
        print(a, " * ", b, " = ", calc.multiply(a, b))
    elif op == "/":
        print(a, " / ", b, " = ", calc.divide(a, b))
    elif op == "**":
        print(a, " ** ", b, " = ", calc.power(a, b))
    elif op == "%":
        print(a, " % ", b, " = ", calc.remainder(a, b))
    else:
        print("Invalid operator")


if __name__ == "__main__":
    main()
