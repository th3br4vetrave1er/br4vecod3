# 1. Есть список чисел заданный пользотелем, использовать функцию sorted()
# для того, что-бы отсортировать список по четности его элементов sorted(,
# key = lambda)

user_list = list(map(int, input("Введите числа для списка: ").split()))

print(f"Cписок {user_list} в отсортированном по чётности виде будет выглядеть так: {sorted(user_list, key = lambda x: x % 2 == 0, reverse=True)}")