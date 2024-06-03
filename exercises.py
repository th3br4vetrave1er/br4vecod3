# name = input("Enter name of product!: ")
# quantity = int(input("How many products? "))
# price = float(input("Enter price! "))
# print(f"{name} is good product! But did you know, that we have {quantity} more products at our warehouse? \nWith the price of {price}. Thats only {price * quantity}$ !!")

# grade = int(input("Enter your grade!: "))
# if grade >= 5:
#     print("PASSED")
# else:
#     print("FAILED")

# workers = list(map(str, input("Enter names of workers with spaces: ").split()))
# salaries = list(map(int, input("Enter salary of workers with spaces: ").split()))
# for worker, salary in zip(workers, salaries):
#     print(f"{worker} recieved {salary} $")
# print(workers)
# print(salaries)
#
# total_salary = 0
# while True:
#     name = input("Введите имя сотрудника (или 'stop' для завершения): ")
#     if name.lower() == "stop":
#         break
#     salary = float(input(f"Введите зарплату для {name}: "))
#     total_salary += salary
#     print(f"{name}: {salary}")
# print(f"Общая сумма всех зарплат: {total_salary}")


# sales = list(map(int, input("Введите продажи за неделю через пробел: ").split()))
# print("Все продажи:", sales)
# max_sale = max(sales)
# min_sale = min(sales)
# average_sale = sum(sales) / len(sales)
# print(f"Максимальная продажа: {max_sale}")
# print(f"Минимальная продажа: {min_sale}")
# print(f"Средняя продажа за неделю: {average_sale}")
