"""
  По теме: Строки
"""
"""
1) Напишите программу, которая будет запрашивать пользовательские данные: имя, фамилию, возраст. Далее программа должна проделать следующие операции: в имени убрать все буквы ‘a’(если они есть), в фамилии - разделить все буквы разделителем *. В конце программа выдает вам объединенную строку, состоящую из полученных имени и фамилии, при этом данная строка должна повторяться столько раз, сколько составляет возраст пользователя.

Например:
Ввод: Введите имя, фамилию и возраст через пробел: John Snow 4
Вывод: JоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*wJоhnS*n*o*w

"""

# data = (input('Введите имя, фамилию и возраст через пробел:').split())
# name =data[0]
# last_time = data[1]
# age = data[-1]

# name = name.lower().replace('a', '')
# last_time = '*'.join(list(last_time))
# print((name + last_time) * int(age))

"""



2) Напишите программу, которая высчитывает количество гласных букв в введенной пользователем строке. И программа выдает вам следующее предложение: В вашей строке насчитано n гласных букв.

Например:
Ввод: Введите строку: I love Makers Bootcamp!
Вывод: В вашей строке насчитано 8 гласных букв

Примечание: не использовать конкатенацию

"""
# from itertools import count


# from re import S
# from tkinter import W


# string = (input('Введите строку'))
# a = string.count('a') 
# o = string.count('o')
# i = string.count('i')
# u = string.count('u')
# y = string.count('y')
# e = string.count('e')
# print(f'В вашей строке насчитано {a+o+i+u+y+e} гласных букв')  

# string = (input('Введите строку:'))
# w = string.count('w')
# q = string.count('q')
# r = string.count('r')
# t = string.count('t')
# p = string.count('p')
# s = string.count('s')
# d = string.count('d')
# f = string.count('f')
# g = string.count('g')
# h = string.count('h')
# j = string.count('j') 
# k = string.count('k')
# l = string.count('l')
# z = string.count('z')
# x = string.count('x')
# c = string.count('c')
# v = string.count('v')
# b = string.count('b')
# n = string.count('n')
# m = string.count('m')
# print(f'В вашей строке насчитано'{'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'z'})

"""
3) Напишите программу, которая просит пользователя ввести свой юзернейм (одним словом) и генерирует пароль из юзернейма, добавив в конец строки символ $, в середину символ &, и заменив строчные буквы на заглавные и наоборот.


Например:
Ввод: Введите юзернейм: JohnSnow
Вывод: Вам сгенерирован пароль: jOHN&sNOW$
"""

# username = (input('Введите юзернейм'))
# center = int(len(username)/2)
# new_username = username [:center] + '&' + username[center:] + '$'
# password = new_username.swapcase()
# print(f'Вам сгенерирован пароль', password)

# name = input('Введите ваше имя')
# last_name = input('Введите вашу фамилию')
# age = input('Введите ваш возраст')
# city = input('Введите ваш город')
# print(f'Вас зовут, {name}, ваша фамилия, {last_name}, ваш возраст, {age}, ваш город, {city}.')
