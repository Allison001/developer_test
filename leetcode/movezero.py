
# class Solution():
#     def moveZeroes(self,nums):
#         """
#         :type nums:List[int]
#         :rtype:None No not return anything
#         """
#         if not nums:
#             return 0
#
#         #两个指针i，j
#         j = 0
#         for i in range(len(nums)):
#             if nums[i]:
#                 nums[j],nums[i] = nums[i],nums[j]
#                 j += 1
#
# nums = [3,4,5,0,1,0,23]
# a = Solution().moveZeroes(nums)
# print(nums)


class Solution():
    def moveZeroes(self, nums):
        if not nums:
            return 0
        a = []
        b = []
        for i in range(len(nums)):
            if nums[i]:
                a.append(nums[i])
            else:
                b.append(nums[i])
        return a+b


# num = [0,1,0,3,12]
# a = Solution().moveZeroes(num)
# print(a)


nums = [0,1,0,3,12]
print(Solution().moveZeroes(nums))


