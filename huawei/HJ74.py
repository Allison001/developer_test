# s = input().split()
# print(s)
# print(s[0])
# print(type(s))

# str = "00000003210Runoob01230000000"
# print(str.strip( '0' ))

# str2 = "   Runoob      "
# print(str2.strip())

while True:
    try:
        s = input().split() # d:// "file name" ddd
        print(s)
        n = 0
        res = []
        s1 = ''
        for c in s:
            n += c.count('"')
            if n%2==0:
                s1 += c.strip('"')
                res.append(s1)
                s1 =''
            else:
                s1 += c.strip('"')+' '
        print(len(res))
        for i in res:
            print(i)
    except:
        break