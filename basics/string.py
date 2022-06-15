"==================строки================="
#  строки - неизменяемый тип данных который предназначен для хранения текста (последовательности символов), заключенно в оденарные или двойные кавычки
# синтаксис ; 


string1 = 'строка с одинарными кавычками'
string2 = "строкаа с двойными кавычкамии"
# error = 'not right" 
string3 = "don't"  #потому что внутри двойных кавычек все одинарные это просто символы
string4 = '"Makers bootcamp"' #потому что внутри одинарных кавычек все одинарные это просто символы  
string5 = '''
много строчный текст в
одинарных кавычках
тут можно ставить "любые" 'кавычки'
'''
string6 = """
много строчный текст в
двойных кавычках
тут можно ставить "любые" 'кавычки'
"""

string7 = 'hello' + ' ' + 'world' # world
string8 = 'A' * 5 # 'AAAAA'

"=====================экранизация строк======================"
# экроназация спец-символы
'\n' # перенос на новою строку 
'\t' # табуляция
'\\' # отображение \ (потому что он является иструкцией, которая влияет на наш код)
'\'' # отображение '
"\"" # отображение "
'\r' # возврожение каретки в начало строки
'\v' # 
# \\ чтобы экранировать нужен символ \\
'My website is Latracal \rSolution'
# Solutionte is Latracal
'hello\world'
# hello 
#   world
"=======================форматирование строк=========================="
title = 'плов'
price = '1500'
format = f'Название: {title}, Цена: {price}'
# Название: Плов, Цена: 1300

fotmat2 = 'Название: %5, Цена: %5'
print(fotmat2 % ("гуляш", "250"))
print(fotmat2 % ("cамсы", "70"))
# Название: гуляш, Цена: 1300


format3 = 'Название: {}, Цена: {}'
print(format3 % ("shakarab", "70"))
# Название: shakarab, Цена: 1300

"+======================методы строк=========================="
# методы типов данных - фуекцииб к которым мы оброщамся через точку
dir(str) # позволяет посмотреть все методы класса (типы данных)

'HELLO'.lower() #'hello
'hello'.upper() # 'HELLO'
'Hello'.swapcase() # 'hELLO'
'hello'.title() # 'Hello'
'hello world'.capitalize() #'Hello world'
'hello'.center(11) # '   hello   '
'hello'.center(11,'-') # '---hello---'
'hello'.count('l') # 2
'hello'.count('ll') #1 
'hello hello'.count('hello') #2
'hello world'.startswith('hell') # true
'hello world'.endswith('ld') #true
'hello world'.startswith('H') # false

'hello world'.find(' ') # 5
'hello world'.find("o") # 4
'hello world'.find('wo') # 6
'hello world'.find('hello') # 0

'hello world'.split() # ['hello' 'world']
'hello world'.split('o') # ['hell', ' w', 'rld']

'$'.join(['hello', 'world']) # 'hello$world'
' '.join(['hello', 'world']) # 'hello world'
''.join(['hello', 'world']) # 'helloworld
' '.join('hello world'.split()) # 'hello world'
"===============================конкатинация================================"
# конкатинация - склеивание строк
'hello' +' world' # "helloworld"
'hello'

"=============================индексы================================="
# индекс - это порядковый номер символа в строке
'h e l l o  w o r l d'
# 0 1 2 3 4 5 6 7 8 9 10
string = 'hello world' 
string[0] # h
string[10] # 
string[5] # ' '

# cрез - подстрока строки
string = [0:5] #'hello'
string = [0:6] # 'hello'
string = [2:4] # 'll'

string[:5] #'hello'
string[6:] # 'world'
string[:] #'hello world'
string[0:11:2] # 'hlowrd'
string[::3] # 'hll'
string[::-1] # 'dlrow olleh'
string == string[0::1]

string -'hello'
string.upper()
print(string)

"=======Доп инфа======="
 a = 5
 b = 5
 print(id(a))
 print(id(b))
 print(hash(a))
 print(hash(b))
string = 'abracadabra'
print(string.('a', 'K'))

count = 0
number = input()
if number.isdigit():
    count = number
print(count)
