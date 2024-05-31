'''''''''
calculations_to_units = 24
name_of_units = "hours"


def days_to_units(num_of_days, custom_message):
    print(f"{num_of_days} days are {num_of_days * calculations_to_units} {name_of_units}")
    print(custom_message)


def scope_check(num_of_days):
    my_var = "variable inside function"
    print(name_of_units)
    print(num_of_days)
    print(my_var)


scope_check(20)

# days_to_units(20, "Okie - Dokie!")

welcome_msg = int(input("Enter your message, PLS!: "))




def is_isogram(string):
    string = string.lower()
    counter = 0
    for i in string:
        diffs = string.count(i)
        counter += diffs
    return counter == len(string)
    
    



print('a', 'b', 'c', sep='*')
print('d', 'e', 'f', sep='**', end='')
print('g', 'h', 'i', sep='+', end='%')
print('j', 'k', 'l', sep='-', end='\n')
print('m', 'n', 'o', sep='/', end='!')
print('p', 'q', 'r', sep='1', end='%')
print('s', 't', 'u', sep='&', end='\n')
print('v', 'w', 'x', sep='%')
print('y', 'z', sep='/', end='!')




digit = int(input())
first = digit // 100
middle = (digit % 100) // 10
last = digit % 10
print("Сумма цифр =", first + middle + last)
print("Произведение цифр =", first * middle * last)



digit = int(input())
first = digit // 100
second = (digit % 100) // 10
third = digit % 10
print(first, second, third, sep="")
print(first, third, second, sep="")
print(second, first, third, sep="")
print(second, third, first, sep="")
print(third, first, second, sep="")
print(third, second, first, sep="")




digit = int(input())
first = digit // 1000
second = (digit % 1000) // 100
third = (digit % 100) // 10
forth = digit % 10
print("Цифра в позиции тысяч равна", first)
print("Цифра в позиции сотен равна", second)
print("Цифра в позиции десятков равна", third)
print("Цифра в позиции единиц равна", forth)




passwrd = input()
check = passwrd
if check == passwrd:
    print("Пароль принят")
else:
    print("Пароль не принят")




# Использование lambda-функции с map()
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x ** 2, numbers))
print(squared)  # Выведет: [1, 4, 9, 16, 25]

# Использование lambda-функции с filter()
numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)  # Выведет: [2, 4]

# Сортировка списка по длине строк с использованием lambda-функции
words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=lambda x: len(x), reverse=True)
print(sorted_words)  # Выведет: ['date', 'apple', 'banana', 'cherry']







# У цій програмі ми обчислюємо суму чисел доти,
# доки користувач не введе 0

total = 0

number = int(input('Enter a number: ')) 

# Додаємо числа, доки number не дорівнюватиме 0
while number != 0:
    total += number  # total = total + number

    # Запитуємо користувацький ввід
    number = int(input('Enter a number: '))

print('total =', total)


'''''''''