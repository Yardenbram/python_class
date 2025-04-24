import sys

def add(*args):
    return sum(args)

def subtract(*args):
    result = args[0]
    for num in args[1:]:
        result -= num
    return result

def multiply(*args):
    result = 1
    for num in args:
        result *= num
    return result

def divide(*args):
    result = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        result /= num
    return result

def calculator():
    if len(sys.argv) < 4:
        print("Usage: python calculator.py <num1> <num2> ... <operation>")
        return

    *nums_str, operation = sys.argv[1:]

    try:
        numbers = [float(n) for n in nums_str]
    except ValueError:
        print("Error: All inputs must be valid numbers.")
        return

    try:
        if operation == "add":
            result = add(*numbers)
        elif operation == "subtract":
            result = subtract(*numbers)
        elif operation == "multiply":
            result = multiply(*numbers)
        elif operation == "divide":
            result = divide(*numbers)
        else:
            print("Error: Unsupported operation. Use add, subtract, multiply, or divide.")
            return

        print("Result:", result)
    except Exception as e:
        print("Error:", e)

if __name__ == "__main__":
    calculator()