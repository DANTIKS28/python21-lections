"============================exceptions============================"
#исключения (ошибки) - объекты которые прерывают работу кода, если были вызваны 

SyntaxError #  исключения которые выходи когда в коде допущена синтаксиче ская ошибка 
# ( - SyntaxError: unexpected EOF while parsing (когда мы не закрыли кавычку или скобку)

# a = SyntaxError: invalid syntax
# (когда мы что -то сделали не синтаксису питона)

NameError # исключения котороя выходит когда мы обращаемся к несуществующей переменной 

# vggjvhvnv
# NameError: name 'v' is not defined

IndexError# исключения которое выходит, когда мы обращаемся пот несуществующему индексу 

# list_ = [1,2,3,4]
# list_ = [1000]
# list_.pop(1000) - IndexError: pop index out of range

KeyError # исключения которое выходит, когда мы обращаемся пот несуществующему ключу

dict_= {'a': 1}
# dict_['b'] - KeyError: 'b'
# dict_.pop('b') - KeyError: 'b'

# print(dict_.get('b')) # не ошибка, выйдет None если ключа нету


ValueError # выхоит когда мы пытаемся распаковать какую-то последовательность, где количество переменных и элементов в последоватьности не совпадает или когда мы в функции передаем некорректный для нее тип данных

# a,b,c = 'ab' # ValueError: not enough values to unpack (expected 3, got 2)
# a,b = 'ab' # 2  символа могут распаковаваться на 2 переменные 
# int('kbhbbhhbjj')  - ValueError: not enough values to unpack (expected 3, got 2)

TypeError # когда мы пытаемся использоать методы не свойственные какому типу данных или когда мы пытаемся передать функцию больше или меньше агрументов, чем принимает функция 

# for i in 123456789: - TypeError: 

# 5 + '5' # - TypeError: unsupported operand type(s) for +: 'int' and 'str'


IndentationError # когда мы не правельно используем отступы 
#  a = 4 -IndentationError: unexpected indent

# for i in range(1):
# print(i)    - IndentationError: expected an indented block

"=====================obrabotka исключения======================="
try:
    print('hello')
except:
    print('hello')
else:
    print('else')