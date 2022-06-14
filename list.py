'=========================list==========================='
#  списки - изменяемый, индексируемый, упорядоченный, итерируемый тип двнных 6 предназначенный для хранения двнных в опредиленном порядке

list_ = [1, 2, 4,'hello', [0.1, 2], {"a":3}]
list_[1] #2
list_[4] #[0.1, 2]
list_[4][0] # 0.1
list_[3][0] # 'h'
list_[-1]["a"] # 3

'==================создание списков===================='

list1 = [1, 2, 3]
list2 = list('hello') # ['h','e','l','l','o']
list3 = list(range(1, 11)) #[1,2,3,4,5,6,7,8,9,10,11]
list4 = [1] * 5 # [1,1,1,1,1]



"=========================методы списков============================"
list =[]
list_.append(1)
print(list_) #[1] 
list_.append('hello')
print(list_) # [1, 'hello]
list_.append([1,2,3,4])
print(list_) # [1, 'hello', [1,2,3,4]]
list_.append(1,2,3) # Type Error


# clear очищает список

list_.clear()
print(list_) # []

# clear считает количество принетого элемента в списке
list_ = [1,2,1,1,3,2,]
list_.count(1) # 4
list_.count(2)# 2
list_.counbt(3) # 3

list_ = ['hello', 'hello', 'hello']
list_.count('h') # 0
list_.count('hello') # 3
len(list_) # 3

# len счистает колтчество обЪектов в списке
list_ = [1,2,[3,4,5],6,7,[8,9,10]]
len(list_) # 6

# extend добавляет элементы второго списка в первый, изменяя первый
list1 = [1,2,3]
list2 = [4,5,6]
list_.extend(list2)
print(list1) # 
print(list2) #

# index  возрощает индекс перого вхождения принятого элемента
list1 = [1,2,3,4,1,2,3,5,4,1]
list1.index(3) # 2
list1.index(1) # 

# insert lj,fdkztn 'ktvtyn gj byltrcs
list_ = [1,2,3]
list_.insert(0, 'hello')
print(list_) # ['hello', 1,2,3]
list_.insert(2,10)
print(list_)


# pop удфляет элемент из списка по индексу и результатом отработонного метода удет удаленный элемент 
list_ = [1,2,3,4,5,6,7]
popped = list_.pop()
print(list_, popped) # [1,2,3,4,5,6] 7
popped = list_.pop(1)
print(list_, popped) # [1,2,3,4,5,6] 2


print([1,2,[3,4,[5,6]]].pop(2).pop(2).pop(1))


# remove  удаляет первый приянятый  элемент в списке
list_ = [1,2,3,1,2,3,1,2,4,1,2,6]
list_.remove(2)
print(list_)


# reverse изменяет список, раставляя егго элементы в обратном порядке 
list_ = [1,2,3,4,5]
print(list_.reverse())
print(list_)

# sort сортирует список состоящий из элементов одного типа данных в в
list_ = [1,2,3,4,5,6,7,8]
list_.sort()
print(list_) 
list_.sort()