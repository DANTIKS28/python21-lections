"""
1) Напишите программу, которая запрашивает с ввода семь чисел через запятую, добавляет их в список. На экран выводит первое и последнее число списка. Затем удаляет последнее число и вместо него вставляет слово “Makers”.
Например: 
Ввод: Введите цифры через запятую: 5, 7, 8, 1, 3, 0, 8
Вывод: 5 8
[5, 7, 8, 1, 3, 0, 'Makers']
"""
numbers_str = input('введите семь чисел через ,').split(',')
numbers_int = []
for number in numbers_str:
  numbers_int.append(int(number))
print(numbers_int[0], numbers_int[-1])

"""
2) Напишите программу, которая генерирует 10 случайных чисел, добавляет их в список и возвращает вам список этих чисел в отсортированном виде в порядке возрастания.
"""
from random import sample

number = sample(range(0, 10), k=10)
print(numbers)
print(sorted(numbers))
print(numbers)

"""
3) Напишите программу, которая заполняет список словами, введенными с клавиатуры, измеряет длину каждого слова и добавляет полученное значение в другой список. Например, список слов – ['yes', 'no', 'maybe', 'ok', 'what'], список длин – [3, 2, 5, 2, 4]. Оба списка должны выводиться на экран.
"""
list_lenght = int(input('Enter list lenght'))
word = []
words_lenght = []
for i in range(list_lenght):
    word = input('Enter word: ')
    words.append(word)
for i in words:
    words_lenght.append(len(i))
print(words_lenght)