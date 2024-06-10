# Написать простой калькулятор

print("Добро пожаловать в калькулятор!")
first_digit = int(input("Введите первое число!:\n"))
operator = input("Выберите действие!(+, -, *, /):\n")
second_digit = int(input("Введите второе число!:\n"))
if operator == "+":
    print(f"Получается: {first_digit + second_digit}")
elif operator == "-":
    print(f"Получается: {first_digit - second_digit}")
elif operator == "*":
    print(f"Получается: {first_digit * second_digit}")
elif operator == "/":
    print(f"Получается: {first_digit / second_digit}")
else:
    print("Что-то не так!")