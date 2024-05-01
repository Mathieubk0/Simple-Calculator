class Calculator:
    def calculate(self, x, y, operation):
        try:
            x = float(x)
            y = float(y)
        except ValueError:
            return "Invalid input. Please enter valid numbers."

        if operation == "+":
            return f"{x} plus {y} equals {x + y}."
        elif operation == "-":
            return f"{x} minus {y} equals {x - y}."
        elif operation == "*":
            return f"{x} times {y} equals {x * y}."
        elif operation == "/":
            if y != 0:
                return f"{x} divided by {y} equals {x / y}."
            else:
                return "You can't divide by zero."
        elif operation == "%":
            return f"{x} modulo {y} leaves {x % y}."
        else:
            return "This isn't a valid operation. Please try again."

    def run_calculator(self):
        while True:
            x = input("Enter the first number (or 'exit' to quit): ")
            if x.lower() == 'exit':
                print("Exiting the calculator.")
                break

            y = input("Enter the second number: ")
            if y.lower() == 'exit':
                print("Exiting the calculator.")
                break

            operation = input("Choose the operation (+, -, *, /, %): ")
            if operation.lower() == 'exit':
                print("Exiting the calculator.")
                break

            result = self.calculate(x, y, operation)
            print(result)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.run_calculator()