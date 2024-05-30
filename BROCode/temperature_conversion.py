unit = input("Is this temperature Celsius or Fahrenheit (C/F): ")
temp = float(input("Enter the temperature: "))

if unit == "C":
    temp = round((9 * temp) / 5 + 32, 1)
    print(f"Your temperature is {temp} Fahrenheit!")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    print(f"Your temperature is {temp} Celsius!")
else:
    print("Enter valid values!")