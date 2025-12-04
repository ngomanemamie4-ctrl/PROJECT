try:
    a = float(input("First number: "))
    b = float(input("Second number: "))
except ValueError:
    print("Error: please enter numeric values.")
    raise SystemExit(1)

op = input("Operator (+ - * /): ").strip()
if op not in "+-*/":
    print("Unknown operator.")
    raise SystemExit(1)

try:
    if op == "+":
        r = a + b
    elif op == "-":
        r = a - b
    elif op == "*":
        r = a * b
    else:
        r = a / b
except ZeroDivisionError:
    print("Error: division by zero.")
    raise SystemExit(1)

print("Result:", r)