# a = 1
# if a==0:
#     print("a=0")
# else:
#     print("a!0")


# """
# x>1 (3x-5) 
# -1<=x<=1 (x+2)
# x < -1 (5x+3)
# """
# x = int(input("输入您的数字："))

# if x > 1:
#     print(3*x-5)

# else:
#     if x >= -1:
#         print(x + 2)
#     else:
#         print(5*x+3)


# 猜数字游戏
# import random

# computet_num = random.randint(1,100)

# while True:
#     people_num = int(input("请输入您的数字："))

#     if people_num < computet_num:
#         print("大一点")
#     elif people_num > computet_num:
#         print("小一点")
#     else:
#         print("猜对了")
#         break





# def fun1(a,b,c):
#     print("这是参数a:",a)
#     print("这是参数b:",b)
#     print("这是参数c:",c)

# fun1(1,23,4)


# def fun1(a):
#     # return "ac"
#     print("a")

# fun1("c")

# def fun1(a,b,c,d):
#     print(a,b,c,d)

# fun1(10,13,d=13,c=90)

# fun1 = lambda x: x+10
# print(fun1(5))

# def fun1(x):
#     return x+10

# print(fun1(5))

# fun1 = lambda x,y: x+y
# print(fun1(10,12))


# list = ["ha"]
# b = {"hah"}
# c = "a"
# d = ("a","v")
# print(type(list))
# print(type(b))
# print(type(c))
# print(type(d))

# lista = ["a","e","d","b","c"]
# lista.append("b")
# lista.insert(5,"e")
# lista.remove("b")
# num = lista.pop(1)
# print(num)

# lista.sort()
# print(lista)


# l2 = [1,2,4,52,21,2,12]
# l2.sort(reverse=False)

# l2.reverse()
# a = l2.index(52)
# l2.extend("a")
# l2.clear()
# a = l2.count(4)
# a = l2.copy()

# print(a)



# list_a = []
# for i in range(1,4):
#     list_a.append(i**2)

# print(list_a)


# lista = []
# for i in range(5):
#     lista.append(i**2)
# print(lista)


# list_a = [i**2 for i in range(5)]
# print(list_a)

# listb = []
# for i in range(5):
#     if i%2 == 0:
#         listb.append(i**2)
# print(listb)

# list_b = [i**2 for i in range(5) if i%2==0]
# print(list_b)

# listc = []
# for i in range(1,3):
#     for j in range(1,3):
#         listc.append(i*j)
# print(listc)

# list_c = [i*j for i in range(1,3) for i in range(1,3)]
# print(list_c)


# list_d = [1,2,3,4,5,6]
# del list_d[1:3]

# print(list_d)

# 元祖
# tuple1 = (1,2,3)
# tuple2 = 1,2,3

# print(tuple1)
# print(type(tuple1))
# print(tuple2)
# print(type(tuple2))


# 元祖的不可变特性
# tuple3 = (1,2,3)
# tuple3[0] = 4
# print(tuple3)

# list1 = [1,2,3]
# list1[0] = 4
# tuple1 = (1,2,3,list1)
# tuple1[3][1] = 9
# print(tuple1)

# set_a = {1}
# set_b = set()
# print(type(set_a))
# print(type(set_b))

# print(len(set_a))
# print(len(set_b))


# a = {1,2,3}
# b = {3,4,5}
# print(a.union(b))
# print(a.intersection(b))
# print(a.difference(b))
# a.add(5)
# print(a)


# a = [i for i in "abbfebfwe"]
# print(a)