#  В строке, заданной пользователем, с помощью слайсинга убрать лишние возможные пробелы с
# начала и в конце.
prompt = input("Enter your string: ")
edited = prompt.split()
print(" ".join(edited))