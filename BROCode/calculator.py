operator = input("Enter your Operator! (+, -, *, /): ")
a = float(input("Enter you first number: "))
b = float(input("Enter you second number: "))

if operator == "+":
    result = a + b
    print(round(result, 3))
elif operator == "-":
    result = a - b
    print(round(result, 3))
elif operator == "*":
    result = a * b
    print(round(result, 3))
elif operator == "/":
    result = a / b
    print(round(result, 3))
else:
    print(f"{operator} is not valid operator!")