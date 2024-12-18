# from random import randint
# win_num = randint(0, 100)
# print("GUESSING GAME!!!")
# print(win_num)
# guess = int(input("ENTER THE NUM IN DIGITS: "))

# while guess != win_num:
#     if guess < win_num:
#         print("A little higher, mate!")
#     elif guess > win_num:
#         print("Too much, mate!")
#     guess = int(input("GUESS AGAIN: "))

# if guess == win_num:
#     print(f"YOU GUESSED IT! {guess} IS THE WIN NUM!!!")


# names = ["Jack Bronson", "Will Smith", "Tom Kukuruz"]

# names_dict = {}

# for name in names:
#     name_list = name.split()
#     names_dict[name_list[0]] = name_list[1]
#     print(name_list)
#     print(names_dict)

# print(names_dict)
# names_dict["John"] = "Connor"
# print(names_dict)
# del names_dict["John"]
# print(names_dict)

# try:
#   10 / 0
# except Exception as e:
#   print(e)

# # prints "division by zero"


# for i in range(1, 123):
#   if i % 3 == 0 and i % 5 == 0:
#     print("FIZZBUZZ")
#   elif i % 3 == 0:
#     print("FIZZ")
#   elif i % 5 == 0:
#       print("BUZZ")
#   else:
#       print(i)

# from pandas import DataFrame

# dictionary = {
#     "name": ["John", "Vishvajit", "Harsh", "Harshita"],
#     "age": [20, 25, 31, 25],
#     "gender": ["Male", "Male", "Male", "Female"]
# }

# df = DataFrame(data=dictionary, columns=["name", "age"])
# print(df)

# text = "Test text here, nothing special"

# print(text.replace("nothing", "very"))


# name = input("What is your name? ")
# color = input("What is you favorite color? ")

# print(f"{name} likes {color}")

# import requests
# resp = requests.get("http://olympus.realpython.org")
# html = resp.text
# print(html[86:132])


# string1 = "Becomes"
# string2 = "becomes"
# string3 = "BEAR"
# string4 = " bEautiful"


# string1 = string1.lower()
# print(string1.startswith("be"))
# print(string2.startswith("be"))
# string3 = string3.lower()
# print(string3.startswith("be"))
# string4 = string4.lstrip().lower()
# print(string4.startswith("be"))

# takes = input("gimme input: ")
# takes_lower = takes.lower()
# takes_len = len(takes)
# print(takes_lower, takes_len)

# answer = input("tell me ur psswrrd: ")
# first_letter = answer[0].upper()
# print(first_letter)

# a = input("enter a ")
# b = input("enter b ")

# result = float(int(a) * int(b))

# print(result)

# # 1
# name = input("Ваше имя: ")
# age = input("Ваш возраст: ")
# print("Привет, меня зовут "+ name + ", " + "и мне " + age + " лет!" )


# #2

# num = 5

# print(num / 2)
# print(num // 2)

# #3

# name = input("Ваше имя: ")
# print(name * 3)

# text = "python is fun"

# print(text.upper())
# print(text.lower())
# print(text.title())


# #4

# user_input = input("enter your input: ")

# print("Длина строки: ", len(user_input))

# #1
# num = int(input("Enter your num: "))
# if num % 2 == 0:
#   print("Your num is odd")
# else:
#   print("Num is equal")


# import random

# random_integer = random.randint(1, 10)

# print(random_integer)


# import my_module
# print(my_module.my_favorite_colour)

# import random

# random_num = random.random() * 10
# print(random_num)

# random_float = random.uniform(1, 10)

# print(random_float)


# heads = 1
# tails = 2
# the_roll = random.randint(heads, tails)

# if the_roll == 1:
#   print("heads")
# else:
#   print("tails")


# import random

# friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

# print(f"{friends[random.randint(0, len(friends)
# - 1)]} is payin the bill") # or random.choice(friends)

# day_1 = 1.434

# day_2 = 2.12

# day_3 = 1.632

# day_4 = 5.59

# day_5 = 2.542

# day_6 = 1.1

# day_7 = 1.324

# week_dist = 1000 * (day_1 + day_2 + day_3 + day_4 + day_5 + day_6 + day_7)

# week_dist /= 1000

# print(week_dist)


# from decimal import Decimal

# i = Decimal("3.3") + Decimal("4.1")

# print(i)


# response = 424562


# sec_in_days = 60 * 60 * 24

# sec_in_hours = 60 * 60

# sec_in_minutes = 60

# days = response // sec_in_days

# response = response % sec_in_days

# hours = response // sec_in_hours

# response = response % sec_in_hours

# minutes = response // sec_in_minutes

# seconds = response % sec_in_minutes

# print(days, hours, minutes, seconds)


# weight = 75  # Вес
# height = 175 # Рост
# dist = 9.75  # Расстояние в км
# hours = 2 # Время движения в часах

# # spent_calories = weight * 0.035 +
# (dist ** 2 / height + weight * 0.029) * hours
# spent_calories = (0.035 * weight +
# (0.029 * weight) * (((dist/hours) ** 2) / height)) * hours * 60
# print(spent_calories)


# def speak_up(sentence):
#     sentence.pop()
#     sentence.append('!')
#     return sentence


# words = ['Программировать', 'круто', '.']

# more_words = {'Пиши', 'код', '.'}
# print(speak_up(words))
# print(speak_up(more_words))


# name: str = "Natasha"
# var_for_bool: bool = True

# print(__annotations__)

def is_rhomb(size_a: float, size_b: float) -> bool:
    return size_a == size_b


print(is_rhomb(14.2, 14.2))
