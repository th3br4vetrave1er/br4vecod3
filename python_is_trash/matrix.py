# С помощью вложенного списка эмитировать матрицу чисел 3x3. Значения заполняются
# случайным образом. Подсчитать сумму элементов главной диагонали матрицы

# matrix = [[row + col for col in range(3)] for row in range(3)]
# for row in matrix:
#     print(row)
# diagonal_sum = 0
# for i in range(len(matrix)):
#     diagonal_sum += matrix[i][i]
# print("Сумма главной диагонали:",diagonal_sum)

# range(len(matrix)) создаёт последовательность индексов от 0 до длины матрицы (не включая).
# matrix[i][i] обращается к элементу на позиции [i][i], что соответствует элементу главной диагонали.
# Каждый элемент главной диагонали добавляется к diagonal_sum.


import random
from pandas import DataFrame as df

n = int(input('Введите порядок матрицы: \n'))
rng = list(map(int, input('Введите диапазон чисел, которыми нужно заполнить матрицу: \n').split()))
print()
matrix = [[random.randrange(rng[0], rng[1]+1) for j in range(n)] for i in range(n)] #Создаем матрицу

# Выводим матрицу
for row in matrix:
    for elem in row:
        print(elem, end = ' ')
    print()
print()
print(df(matrix)) # Выводим матрицу пиздато: ровненькуя с индексами

# Считаем диагонали
general_line = 0
for i in range(n):
    general_line += matrix[i][i]
print(f'Сумма элементов главной диагонали равна: {general_line}')

side_line = 0
for i in range(n):
    side_line += matrix[i][n-i-1]
print(f'Сумма элементов побочной диагонали равна: {side_line}')
