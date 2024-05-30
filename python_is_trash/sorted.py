# Есть список чисел, заданный пользователем, использовать функцию `sorted()` для сортировки
# списка по чётности его элементов `sorted(, key = lambda)`.

listed = input("Enter list with spaces: ")
listed = list(map(int, listed.split()))
sorted_list = sorted(listed, key=lambda x: x % 2)
print(sorted_list)