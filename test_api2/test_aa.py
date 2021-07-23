

# def dui(num):
#     res = []
#     while num >=1:
#         a = num % 2
#         num = num //2
#         res.append(a)
#
#     r,l = 0,len(res)-1
#     while r <= l:
#         if res[r] != res[l]:
#             return False
#         r +=1
#         l -=1
#     return True
#
# b = dui(8)
# print(b)


def find(nums):
    less = []
    pivotlist = []
    more = []

    for i in range(len(nums)):
        pivot = nums[0]
        if nums[i] == pivot:
            pivotlist.append(nums[i])
        elif nums[i] > pivot:
            more.append(nums[i])
        else:
            less.append(nums[i])
        less = find(less)
        more = find(more)
    nums = less + pivotlist + more
    return nums

a = find([1,2,4,2,6,3,8])
print(a)


