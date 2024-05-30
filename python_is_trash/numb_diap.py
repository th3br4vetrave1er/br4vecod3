# Пользователь задает диапазон чисел `a,b`, а также список чисел. Подсчитать среднее
# арифметическое чисел, находящихся в этом диапазоне в списке.

a_diap = int(input("Enter A: "))
b_diap = int(input("Enter B: "))

digit_list = input("Enter List of Digits: ")

digit_list = list(map(int, digit_list.split()))

filtered_digits = [x for x in digit_list if a_diap <= x <= b_diap]
if filtered_digits:
    average = sum(filtered_digits) / len(filtered_digits)
    print(average)
else:
    print("No such digits in diapason")
