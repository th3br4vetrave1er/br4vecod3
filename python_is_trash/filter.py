# С помощью функции `filter` изменить список так, чтобы остались только нечётные элементы

prompt = input("Enter your digits with spaces: ")

filtered_prompt = list(map(int, prompt.split()))
filtered_prompt = list(filter(lambda x: x % 2 != 0, filtered_prompt))
print(filtered_prompt)

