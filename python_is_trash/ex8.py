# В списке заданном пользователем подсчитать сумму четных чисел
user_list = list(map(int,input("Введите числа через пробел: ").split()))
print(f"Сумма четных чисел из списка {user_list} равна: {sum(i for i in user_list if i % 2 ==0)}")