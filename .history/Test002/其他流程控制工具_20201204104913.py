#if 语句

# x = int(input("请输入数字："))

# if x < 0:
#     x = 0
#     print("Negative changed to zero")

# elif x == 0:
#     print("Zero")

# elif x ==1:
#     print("Single")

# else:
#     print("More")



# for语句

# words = ['cat', 'window', 'defenestrate']

# for i in words:
#     print(i,len(i))

# for i in range(5):
#     print(i)

# for i in range(5,10):
#     print(i)

# for i in range(0,10,2):
#     print(i)

# for i in range(-10,-100,-10):
#     print(i)


# a = ['Mary', 'had', 'a', 'little', 'lamb']
# for i in range(len(a)):
#     print(i,a[i])

# print(range(10))

# for i in range(10):
#     print(i)

# a = sum(range(0,11))
# print(a)

# b = list(range(0,11))
# print(b)

# for i in range(0,11):
#     print(i)



# for n in range(2,10):
#     for x in range(2,n):
#         if n % x ==0:
#             print(n, 'equals', x, '*', n//x)
#             break
#     else:
#         print(n," is a prime number")


# for i in range(2,10):
#     if i % 2 ==0:
#         print("even number",i)
#         continue
#     print("old number",i)



# pass语句


# 定义函数
# def sum(n):
#     a,b = 0,1
#     while a < n:
#         print(a,end=" ")
#         a,b = b, a+b
#     print()

# # sum(100)

# f = sum
# f(100)


def fib2(n):
    a,b = 0,1
    result = []
    while a<n:
        result.append(a)
        a,b = b, a+b
    return result

