# 3. Пользователь задает диапазон чисел a,b, так же пользователь задает
# список чисел. Подсчитать среднее арифм.чисел находящихся в этом диапазоне
# в списке

start = int(input("Введите начало диапазона: "))
finish = int(input("Введите конец диапазона: "))
num_list = []
while start <= finish:
    num_list.append(start)
    start += 1
print(f"Cреднее арифметическое цифр в данном диапазоне {num_list} равно {sum(i for i in num_list) / len(num_list) }")
    