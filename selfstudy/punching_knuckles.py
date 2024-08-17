sales_w1 = [7,3,42,19,15,35,9]
sales_w2 = [12,4,26,10,7,28]
sales = []
day = int(input("Enter another day to week 2: "))
sales_w2.append(day)
sales = sales_w1 + sales_w2
worst_day = min(sales) * 1.5
best_day = max(sales) * 1.5
print(f"On the best day you have earned {best_day}")
print(f"On the worst day you have earned {worst_day}")
print(f"On the first week you earned {sales_w1}, and on the second week you earned {sales_w2}, in total its {worst_day + best_day} adenas.")