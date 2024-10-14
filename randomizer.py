from random import randint

# happy_man = randint(1, 7)


# # 1 sanya
# # 2 dan 
# # 3 Lusha 
# # 4 Slavix
# # 5 Sharik 
# # 6 Maxic
# # 7 Velarion

# if happy_man == 1:
#     print(f"Следующим мотиватором будет {happy_man} Саня Бибос!")
# elif happy_man == 2:
#     print(f"Следующим мотиватором будет {happy_man} Дэн!")
# elif happy_man == 3:
#     print(f"Следующим мотиватором будет {happy_man} Люша!")
# elif happy_man == 4:
#     print(f"Следующим мотиватором будет {happy_man} Славис!")
# elif happy_man == 5:
#     print(f"Следующим мотиватором будет {happy_man} Шарик!")
# elif happy_man == 6:
#     print(f"Следующим мотиватором будет {happy_man} Максик!")
# elif happy_man == 7:
#     print(f"Следующим мотиватором будет {happy_man} Веларион!")


from random import randint
names = ["Biblos", "Dan", "Lusha", "Sharik", "Slavix", "Velarion"]
list_length = len(names)
randomizer = randint(0, list_length - 1)

for name in names:
    print(f"Следующий мотиватор - {names[randomizer]}")
    break
