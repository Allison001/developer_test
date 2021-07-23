# from json import loads


# def read_line():
#     with open("/Users/yeahmobi/Desktop/work/python/developer/test_api2/api/wenjian.yaml",'r') as f:
#         n = f.readlines()
#         count =0
#         flag = True
#         for i in n:
#             i = i.strip() #去除行前后的空格

            # if i.startswith("#"):
            #     continue
            # elif i == "":
            #     continue
            # elif i[0:3] == '"""':
            #     continue
            # elif i.startswith("'''"):
            #     continue
            # elif i.startswith('"""') and i.endswith('"""'):
            #     continue
            # else:
            #     count += 1
#
#             if i == "'''" or i == '"""':
#                 if flag == True:
#                     flag = False
#                     continue
#                 else:
#                     flag = True
#                     continue
#             elif (i.startswith("'''") and i.endswith("'''")) or (i.startswith('"""') and i.endswith('"""')):
#                 continue
#             elif i.startswith("'''") or i.startswith('"""') or i.endswith("'''") or i.endswith('"""'):
#                 if flag == True:
#                     flag = False
#                     continue
#                 else:
#                     flag = True
#                     continue
#             else:
#                  count += 1
#         print(count)
#
#
# read_line()


# def count_line_core(file_name):  ##传入单个文件，统计行数，之后返回该文件的实际代码行数；区分utf-8、gbk有待优化
#     # print('core_file_name:',file_name)
#     lines_count=0
#     flag=True
#     # try:
#     #     with open(file_name,'r',encoding='gbk') as fp:
#     #         # print('gbk file_name:',file_name)
#     #         for i in fp:
#     #             i=i.strip()
#     #             if i=="'''" or i=='"""':
#     #                 if flag==True:
#     #                     flag=False
#     #                     continue
#     #                 else:
#     #                     flag=True
#     #                     continue
#     #             elif (i.startswith("'''") and i.endswith("'''")) or (i.startswith('"""') and i.endswith('"""')):
#     #                 continue
#     #             elif i.startswith("'''") or i.startswith('"""') or i.endswith("'''") or i.endswith('"""'):
#     #                 if flag==True:
#     #                     flag=False
#     #                     continue
#     #                 else:
#     #                     flag=True
#     #                     continue
#     #             if flag==True and i!='' and not i.startswith('#'):
#     #                 lines_count+=1
#     #                 #print(i)
#     #             if i.startswith('#-*-') or i.startswith('#coding') or i.startswith('#encoding'):
#     #                 lines_count+=1
#     #                 #print(i)
#     # except:
#     with open(file_name,'r',encoding='utf-8') as fp:
#         # print('utf-8 file_name:',file_name)
#         for i in fp:
#             i=i.strip()
#             if i=="'''" or i=='"""':
#                 if flag==True:
#                     flag=False
#                     continue
#                 else:
#                     flag=True
#                     continue
#             elif (i.startswith("'''") and i.endswith("'''")) or (i.startswith('"""') and i.endswith('"""')):
#                 continue
#             elif i.startswith("'''") or i.startswith('"""') or i.endswith("'''") or i.endswith('"""'):
#                 if flag==True:
#                     flag=False
#                     continue
#                 else:
#                     flag=True
#                     continue
#             if flag==True and i!='' and not i.startswith('#'):
#                 lines_count+=1
#                 #print(i)
#             if i.startswith('#-*-') or i.startswith('#coding') or i.startswith('#encoding'):
#                 lines_count+=1
#                 #print(i)
#     return lines_count


# def count_line_core(file_name):  ##传入单个文件，统计行数，之后返回该文件的实际代码行数；区分utf-8、gbk有待优化
#     # print('core_file_name:',file_name)
#     lines_count=0
#     flag=True
#     with open(file_name,'r',encoding='utf-8') as fp:
#         # print('utf-8 file_name:',file_name)
#         for i in fp:
#             i=i.strip()
#             if i=="'''" or i=='"""':
#                 if flag==True:
#                     flag=False
#                     continue
#                 else:
#                     flag=True
#                     continue
#                 continue
#             elif (i.startswith("'''") and i.endswith("'''")) or (i.startswith('"""') and i.endswith('"""')):
#                 continue
#             # elif i.startswith("'''") or i.startswith('"""') or i.endswith("'''") or i.endswith('"""'):
#             #     if flag==True:
#             #         flag=False
#             #         continue
#             #     else:
#             #         flag=True
#             #         continue
#
#             if flag==True and i!='' and not i.startswith('#'):
#                 lines_count+=1
#                 print(i)
#             # if i.startswith('#-*-') or i.startswith('#coding') or i.startswith('#encoding'):
#             #     lines_count+=1
#             #     print(i)
#     return lines_count
#
# print(count_line_core('/Users/yeahmobi/Desktop/work/python/developer/test_api2/api/wenjian.yaml'))
"""
这是一个统计代码行数的函数
"""
# def count_line(filename): #函数名
#     with open(filename) as f:
#         flag = True
#         count = 0
#         for i in f.readlines():
#             i = i.strip()
#             if i == '"""' or i == "'''":
#                 if flag == True:
#                     flag = False
#                     continue
#                 else:
#                     flag = True
#                     continue
#
#             elif (i.startswith("'''") and i.endswith("'''")) or (i.startswith('"""') and i.endswith('"""')):
#                 continue
#             elif i !='' and flag == True and i[0:1] != "#":
#                 count+=1
#                 print(i)
#         return count
#
# print(count_line('/Users/yeahmobi/Desktop/work/python/developer/test_api2/api/test_wen.py'))


# class Solution:
#     def reverse(self, x: int) -> int:
#         s = int(str(abs(x))[::-1])
#         if s.bit_length() > 31:
#             return 0
#         else:
#             if x >=0:
#                 return s
#             else:
#                 return -s
# a = Solution().reverse(120)
# print(a)


# class Solution:
#     def reverse(self, x: int) -> int:
#         if x >=0:
#             a = int(str(x)[::-1])
#         else:
#             a =0- int(str(x)[:0:-1])
#
#
#         if (-2**31) <a < (2**31)-1:
#             return a
#         else:
#             return 0




# class Solution:
#     def solve(self , str ):
#         # write code her
#         str = list(str)
#         print(str)
#         l,r = 0,len(str)-1
#         while l <=r:
#             str[l],str[r] = str[r],str[l]
#             l +=1
#             r -=1
#         return ''.join(str)
#
# a=Solution().solve('ancd')
# print(a)


# class Solution:
#     def maxLength(self, arr):
#         # write code here
#         l, r = 0, 0
#         stark = []
#         n = 0
#         while r < len(arr):
#
#             if arr[r] in stark:
#                 l += 1
#                 r = l
#                 stark.clear()
#
#             else:
#                 stark.append(arr[l])
#                 r += 1
#                 n = max(n, len(stark))
#
#         return n

# class Solution:
#     def maxLength(self , arr ):
#         # write code here
#         res=[]
#         length=0
#         for i in arr:
#             if i not in res:
#                 res+=[i]
#             else:
#                 res = res[res.index(i)+1:] + [i]
#             if length<len(res): length= len(res)
#         return length

# class Solution:
#     def maxLength(self , arr ):
#         # write code here
#         l,stark =0,[] #定义一个l存储每次遇到重复的最大值，stark存储不重复的值
#         for i in arr:
#             if i in stark:  #如果在stark中，就开始遍历
#                 l = max(l,len(stark))
#                 st = stark.index(i) #获取当前i(重复元素)在stark中的下标
#                 stark = stark[st+1:]  #取当前stark中重复元素后的数
#             stark.append(i)
#         return max(l,len(stark))
#
# arr = [2,2,3,4,3]
# a = Solution().maxLength(arr)
# print(a)

# stark = [1,2,3,4]
# # st = stark.index(4)
# stark = stark[1:]
# print(stark)


# "1AB2345CD","12345EF"


class Solution:
    def LCS(self , str1 , str2 ):
        # l = 0
        n = []
        for i in range(len(str2)):
            s = str2[:i+1]
            if s in str1:
                # l = max(l,len(s))
                if not n:
                    n.append(s)
                if len(s) > len(n[0]):
                    n.append(s)

            else:
                str2 = str2[i:]
        return n[-1]
a = Solution().LCS("1AB2345CD","12345EF")
print(a)


# a = ['ancd']
# print(len(a[0]))