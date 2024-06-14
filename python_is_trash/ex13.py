# 2. С помощью функции filter изменить list так, что-бы остались только
# нечетные элементы

user_list = list(map(int, input("Введите цифры для списка: ").split()))
print(f"В списке {user_list} нечетными элементами являются: {list(filter(lambda x: x % 2 != 0, user_list))}")