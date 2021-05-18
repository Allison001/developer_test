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




from collections import deque


queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")  
queue.append("Graham")
queue.popleft()