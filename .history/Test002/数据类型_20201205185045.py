# fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
# print(fruits.count("apple"))

# a = fruits.index("banana",4)
# print(a)


# fruits.reverse()
# print(fruits)

# fruits.append("daka")
# print(fruits)

# print(fruits.sort)

# a = fruits.pop(0)
# print(a)
# print(fruits)


# number = [1,2,45,3,7,24,3]

# print(number.sort(reverse=True))




# from collections import deque


# queue = deque(["Eric", "John", "Michael"])
# queue.append("Terry")  
# queue.append("Graham")
# a= queue.popleft()
# print(a)
# b = queue.popleft()
# print(b)
# print(queue)

# number = [1,2,3,4]
# number.append(5)
# number.append(6)
# print(number)

# number.pop()
# number.pop()
# print(number)


# lista = []
# for i in range(1,10):
#     lista.append(i**2)

# print(lista)

# number = list(map(lambda x: x**2, range(1,10)))
# print(number)

# number = [i**2 for i in range(1,10)]
# print(number)

# number1= [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
# print(number1)


# lis2 = []

# for x in [1,2,3]:
#     for y in [3,1,4]:
#         if x != y:
#             lis2.append(x,y)

# print(number1)


# ver = [1,2,3]
# lista = [i**2 for i in ver]
# print(lista)


# ver1 = [-1,-2,3,4,-5]
# list2 = [i**2 for i in ver1 if i>0]
# print(list2)

# list3 = [abs(i) for i in ver1]
# print(list3)


# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# ab = [i.strip() for i in freshfruit]
# print(ab)

# list4 =[(x,x**2) for x in range(10)]
# print(list4)

# ver =[[1,2,3],[4,5,6],[7,8,9]]

# list5 = [y for i in ver for y in i]
# print(list5)

# from math import pi

# pia = 1.1323123

# for i in range(6):
#     print(round(pia,i))

# list6 = [round(pia,i) for i in range(6)]

# print(list6)


#交换行和列

row_col = [
    [1,4,7],
    [2,5,8],
    [3,6,9]
]

# list10 =[reo[2] for reo in row_col]
# print(list10)

# list9 = []
# for i in range(3):
#     list9.append([reo[i] for reo in row_col])

# print(list9)


# a = []
# for i in row_col:
#     a.append(i[0])
# print(a)

# lista =[i[0] for i in row_col]
# print(lista)

# liasb = []
# for i in range(3):
#     liasb.append([y[i] for y in row_col])

# print(liasb)

listc = [[y[i] for y in row_col] ]