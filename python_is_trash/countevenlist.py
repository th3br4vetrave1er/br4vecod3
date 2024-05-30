#  В списке, заданном пользователем, подсчитать сумму чётных чисел

prompt = input("Enter your numbers with spaces: ")
prompt = list(map(int, prompt.split()))
even_prompt = sum(x for x in prompt if x % 2 == 0)
print(prompt)
print(even_prompt)
