"===============логические операторы=============="
"логические операторы - выраженияб которые возврощают True, если правда и false, если не правда"
5 == 5 # True
4 == 5# False

5 != 5 # false 
5 != 2 # true 
5 > 10 # false
10 > 5 # true
5 > 5 # false
10 < 5 #false

5 <= 10 #true
10 <= 5 #False
5<=5 # true
5 >= 10 # false
10 >= 5# true
5 >= 5 #true
'5'== 5 # false
# 5 = 3 # присваивание

"=============And or not================="
# and - и
# or - или
a = 5
b = 6

a == 5 and b == 6 # True (правая сторона True, левая тоже True)
a == 5 and b == 5 # False (правая сторона True, но левая False)
a == 4 and b == 5 # False (обе стороны False)

a == 5 or b == 6 # True (правая сторона True, левая тоже True)
a == 5 or b == 5 # True (правая сторона True, но левая False)
a == 4 or b == 5 # False (обе стороны False)

# если обе части выдают True - будет True
# если обе части выдают False - будет False
# если одна часть True, вторая False:
# 1. если стоит and - выйдет False
# 2. если стоит or - выйдет True

not True # False
not False # True
not a == 5 # False (потому что a == 5)
not a == 4 # True (потому что a == 5)


2 in [1,2,3,4,5] # true
"a" in {'b':3, "c":'a'} # False 

'====================Bool type====================='
# булевые типы данных - имеют всего два значения True и false
# bool(1) # True
# bool(0) #False
# bool(-324)# true

# bool('hello') # true
# bool('') # false
# bool(' ') # true

# bool(False) # False
# bool(True) # true
'=====================None Type======================='
# # none - это тип данных с одним значением none, который используется для обозначения пустых значений или отсутствием значения

# bool(None) # false
# bool('None') #true

# a = None
# print(bool(a)) # false
# print(a is None) # True

# # is это проверка на полное соответствие


'==================условные операторы======================='
# ## eckjdyst jgthfnjhs ye;ys lkz njuj xnj,ss ghb hfpys[ d[kjlysp lfyys[ rjl]]]

# if условие1:
#     тело1
#     # будет работать только если условие1 верно

# if условие1:
#     тело1
#     # будет работать только если условие1 верно
# else:
#     тело2
#     # будет работать если условие1 не верно

# if условие1:
#     тело1
#     # будет работать только если условие1 верно
# elif условие2:
#     тело2
#     # будет работать если условие1 не верно и условие2 верно

# if условие1:
#     тело1
#     # будет работать только если условие1 верно
# elif условие2:
#     тело2
#     # будет работать если условие1 не верно и условие2 верно
# else:
#     тело3
    # будет работать если условие1 не верно и условие2 не верно

# в одной конструкции мы модем использовать неограниченное кол-во elif 
# в одной конструкции мы модем использовать только один if
# else  мы можем использовать так-же только один раз или вообще не укказывать 

# a = int(input('введите число: '))
# if a > 0:
#     print(f'число {a} - положительное')
# elif a < 0:
#     print(f'число {a} - отрицательное')
# else:
#     print(f'число {a} - это 0')

'============FizzBuzz========='
# выве
# если число кратно 3 - вывести Fizz
# если число кратно 5 - вывкести Buzz
# если число кратно и 5 и 3 - вывести FizzBuzz
# если число кратно ни 5 ни 3 - вывести число

# for i in range(1, 17):
#     if i % 5 == 0 and i % 3 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# for i in range(1, 101):
#     if (i % 3):
#         print('Fizz')
#     if (i % 5):
#         print('BUzz')
#     if ((i % 3) or (i % 5)):
#         print('FizzBazz')
#     else:
#         print(i)

# for i in range(1, 17):
#     if i % 3 == 0:
#         if i % 5 == 0:
#             print('FizzBuzz')
#         else:
#             print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#     else:
#         print(i)


# x = int(input())
# y = int(input()) 

# print(f"x{' не' if x % y != 0 else ''} делится на y")
# print(f"Частное: {x // y}'") 
# print(f"Oстаток: {x % y}' if x % y != 0 else ''")

"================yernarnie operatori=================="
# uslovi v odnu strochku
# telo1 if uslovie else telo2
res = 'Hello' if a == 5 else 'Bye' 
print(res) 
# Hello, если a == 5
# Bye, если a != 5