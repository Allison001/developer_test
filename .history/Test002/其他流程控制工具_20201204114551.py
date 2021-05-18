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


# def fib2(n):
#     a,b = 0,1
#     result = []
#     while a<n:
#         result.append(a)
#         a,b = b, a+b
#     return result

# f = fib2(10)

# print(f)


# def ask_ok(prompt, retries=4, reminder='Please try again!'):
#     while True:
#         ok = input(prompt)
#         if ok in ('y', 'ye', 'yes'):
#             return True
#         if ok in ('n', 'no', 'nop', 'nope'):
#             return False
#         retries = retries - 1
#         if retries < 0:
#             raise ValueError('invalid user response')
#         print(reminder)



# ask_ok('Do you really want to quit?')


# def f(a,l=[]):
#     l.append(a)
#     return l

# print(f(10))
# print(f(11))


# def l(a,L=[]):
#     L.append(a)
#     print(L)

# l(1)
# l(2)
# l(3)


# def l(a,L=None):
#     if L is None:
#         L =[]
#     L.append(a)
#     return L

# print(l(0))
# print(l(1))
# print(l(2))

# def f(a, L=None):
#     if L is None:
#         L = []
#     L.append(a)
#     return L

# print(f(1))
# print(f(2))
# print(f(3))



# def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
#     print("-- This parrot wouldn't", action, end=' ')
#     print("if you put", voltage, "volts through it.")
#     print("-- Lovely plumage, the", type)
#     print("-- It's", state, "!")


# parrot(1000)


# def cheeseshop(kind, *arguments, **keywords):
#     print("-- Do you have any", kind, "?")
#     print("-- I'm sorry, we're all out of", kind)
#     for arg in arguments:
#         print(arg)
#     print("-" * 40)
#     for kw in keywords:
#         print(kw, ":", keywords[kw])

# cheeseshop("Limburger", "It's very runny, sir.",
#            "It's really very, VERY runny, sir.",
#            shopkeeper="Michael Palin",
#            client="John Cleese",
#            sketch="Cheese Shop Sketch")


# def cheeseshop(kind,*arg,**key):
#     print(kind)
#     for a in arg:
#         print(a)
#     for b in key:
#         print(b)


# cheeseshop("a","b","c",cal="e",avv="f",faf="fawef",hh="f")


# def abcd(kind,*arr):
#     print(kind)
#     for i in arr:
#         print(i)

# abcd("a","b","n")


# def a(**ab):
#     for i in ab:
#         print(i,ab[i])

# a(a="a1",b="b1")

def pos_only_arg(arg, “):
    print(arg)