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

for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status