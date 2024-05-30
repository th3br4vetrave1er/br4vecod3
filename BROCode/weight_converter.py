weight = float(input("Enter your weight: "))
unit = input("Is it in Kg or Lbs? (K or L): ")
if unit == "K":
    weight *= 2.205
    unit = "LBS"
    print(f"Your weight is {round(weight, 1)} {unit}")
elif unit == "L":
    weight /= 2.205
    unit = "Kg"
    print(f"Your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid!")

