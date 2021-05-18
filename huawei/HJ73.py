while True:
    try:
        y,m,d = map(int,input().split())
        month =[31,28,31,30,31,30,31,31,30,31,30,31]
        days = sum(month[:(m-1)])+d
        if m >=2 and (y%4==0 and y%100 !=0 or y%400 ==0):
            days+=1
        print(days)
    except:
        break

# m = map(int,input())
# month =[31,28,31,30,31,30,31,31,30,31,30,31]
# a = month[0:3:1]
# print(a)

# days = sum(month)
# print(days)
