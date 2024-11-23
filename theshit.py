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

# 1
name = input("Ваше имя: ")
age = input("Ваш возраст: ")
print("Привет, меня зовут "+ name + ", " + "и мне " + age + " лет!" )