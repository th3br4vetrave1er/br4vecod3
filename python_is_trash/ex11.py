# 5. В строке заданной пользователем с помощью слайсинга убрать лишние
# возможные пробелы с начала и в конце

user_string = input("Введите строку с пробелами: ")
edited_string = user_string.split()
edited_string = " ".join(edited_string)
print(edited_string)