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

number1= [(x,y) for x in [1,2,3] for y in [3,1,4] if x != y]
print(number1)


lis2 = []

for x in [1,2,3]:
    for y in [3,1,4]:
        if x != y:
            lis2.append(x,y)