# # 我有 1~N 一共 N 个连续的数，每个数出现一次
# # ，比如 1，2，3，4，5，6，7，8，9.....N，
# # 现在我把它打乱，打乱的过程中丢失了一个数，
# # 请用时间/空间复杂度尽可能小的方式找出这个数
#
# # def find(a):
# #     a = sorted(a)
# #     n = []
# #     for i in range(len(a)+1):
# #         n.append(i+1)
# #
# #     for j in n:
# #         if j in a:
# #             continue
# #         else:
# #             return j
# #
# # a = find()
#
#
# # 2020-06-18购买“帮宝适”品牌的人，在当前时间各大区的分布人数，并且找出分布人数大于10w的大区
# # //购买表
# # A表：pin 人 time 时间 brand品牌
# # // 画像表
# # B表：pin 人 time 时间 regional 地区
# #
# # select regional,count(*) from A
# # inner join B on A.pin = B.pin
# # where B.time = '2020-07-15'
# # group by regional
#
# # a = '1.2.1'
# # a = a.split('.')
# # print(a)
# # a = '1.2.1'
# # a= a.replace('.','')
# # print(a)
# # a = '  fwe  '
# # a = a.strip()
# # print(a)
#
# # a = {}
# # b = 'eowjfwe'
# # for i in b:
# #     a[i] = a.get(i,0) +1
# # c = {'e': 2, 'o': 1, 'w': 2, 'j': 1, 'f': 1}
# # if a ==c :
# #     print(True)
# # else:
# #     print(False)
#
#
# # class Solution:
# #     def search(self, nums, target):
# #         left, right = 0, len(nums) - 1
# #         while left <= right:
# #             pivot = left + (right - left) // 2
# #             if nums[pivot] == target:
# #                 return pivot
# #             elif nums[pivot] > target:
# #                 right = pivot - 1
# #             elif nums[pivot] < target:
# #                 left = pivot + 1
# #
# # #         return -1
# #
# # class Solution(object):
# #     def getKthFromEnd(self, head, k):
# #         stark = []
# #         while head:
# #             stark.append(head)
# #             head = head.next
# #         return stark[-k]
#
# # class Solution(object):
# #     def getKthFromEnd(self, head, k):
# #         h1 = head
# #         h2 = head
# #         # 让快指针先走k步
# #         for i in range(k):
# #             h2 = h2.next
# #         # h2快指针有值，两个指针同事往后走
# #         while h2:
# #             h1 = h1.next
# #             h2 = h2.next
# #         return h1
#
# # a = '021'
# # print(int(a))
#
#
#
# #
# # class Solution:
# #     def spiralOrder(self , matrix):
# #         res = []
# #         while matrix:
# #             res += matrix[0]
# #             matrix = list(zip(*matrix[1:]))[::-1]
# #         return res
# #
# # a = Solution().spiralOrder([[1,2,3],[4,5,6],[7,8,9]])
# # print(a)
#
# # res = []
# # a = [[4,7],[5,8]]
# # #
# # lista = zip(*a)
# # lista_id = id(zip(*a))
# # listb = list(zip(*a))
# # res +=listb[0]
# # print(lista)
# # print(lista_id)
# # print(listb)
# # print(res)
#
# # str = "abad"
# # a = list(str)
# # print(a)
#
# a = '   1.2.1   '
# # a = a.split('.')
# # b = ''.join(a)
# # print(int(b))
#
# # a = a.strip()
# # print(a)
#
# # class Solution:
# #     def longestCommonPrefix(self, strs):
# #         test = ''
# #         g = ''
# #         for i in strs[0]:
# #             test += i
# #             for j in strs[1:]:
# #                 if not j.startswith(test):
# #                     return g
# #             g += i
# #         return g
# #
# # a = Solution().longestCommonPrefix(["flower","flow","flight"])
# # print(a)
#
# import copy
# # class data():
# #     name = ''
# # a = data()
# # a.name="dog"
# #
# # b = data()
# # b.name = "cat"
# #
# # arry = [a.name,b.name]
# # arryc = copy.copy(arry)
# # arryd = copy.deepcopy(arry)
# #
# # print("修改前：",arry)
# # print("修改前浅拷贝：",arryc)
# # print("修改前深拷贝：",arryd)
# #
# # arry[0]='pig'
# #
# #
# # print("修改后：",arry)
# # print("修改后浅拷贝：",arryc)
# # print("修改后深拷贝：",arryd)
#
# # arry = ["a","b","c"]
# #
# # copyq = copy.copy(arry)
# # copyd = copy.deepcopy(arry)
# #
# # arry[0] = 'r'
# #
# # print(copyq)
# # print(copyd)
#
# import copy
#
# l1 = [[1, 2], (3, 4)]
# l2 = l1
# l3 = copy.copy(l1)
# l4 =copy.deepcopy(l1)
# print(id(l1))
# print(id(l2))
# print(id(l3))
# print('*'*30)
# print('Item in l1')
# for i in l1:
#     print(id(i))
# print('Item in l2')
# for i in l2:
#     print(id(i))
# print('Item in l3')
# for i in l3:
#     print(id(i))
#
#
# class Solution:
#     def mergeTrees(self, root1: TreeNode, root2: TreeNode) -> TreeNode:
#         if not root1:
#             return root2
#         if not root2:
#             return root1
#
#         mertree = TreeNode(root1.val + root2.val)
#         mertree.left = self.mergeTrees(root1.left, root2.left)
#         mertree.right = self.mergeTrees(root1.right, root2.right)
#
#         return mertree







# rt78[89)fkt4]+

# 87tr[98)4tkf]+


# def splita(stra):
#     res = []
#
#
#     a = stra.split("[")
#     res.append(a[0])
#
#     b = a[1].split(')')
#     res.append(b[0])
#
#     c = b[1].split("]")
#     res.append(c[0])
#     res.append(c[1])
#
#     stark =[]
#     for i in res:
#         i = list(i)
#         l,r = 0,len(i)-1
#         while l <= r:
#             i[r],i[l] =i[l],i[r]
#             l +=1
#             r -=1
#         stark.append(i)
#
#     r = str(''.join(stark[0])) + "[" + str(''.join(stark[1])) + ")" + str(''.join(stark[2])) + "]" +str(''.join(stark[3]))
#
#     return  r
#
# a = splita("rt78[89)fkt4]+")
# print(a)


class Solution(object):
	def levelOrder(self, root):
		if not root:
			return []
		res = []
		queue = [root]
		while queue:
			# 获取当前队列的长度，这个长度相当于 当前这一层的节点个数
			size = len(queue)
			tmp = []
			# 将队列中的元素都拿出来(也就是获取这一层的节点)，放到临时list中
			# 如果节点的左/右子树不为空，也放入队列中
			for _ in range(size):
				r = queue.pop(0)
				tmp.append(r.val)
				if r.left:
					queue.append(r.left)
				if r.right:
					queue.append(r.right)
			# 将临时list加入最终返回结果中
			res.append(tmp)
		return res


















