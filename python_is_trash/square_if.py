# Написать программу, которая возводит число в квадрат, если оно чётное.

digit = int(input("Enter your digit:\n"))
if digit % 2 == 0:
    print(f"Your square digit is {digit ** 2}")
else:
    print("Enter even number!")