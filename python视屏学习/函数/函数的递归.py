# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28
# def age(n):
#     if n == 1:
#         return 18
#     return age(n-1) +2
#
# print(age(5))

# l=[1,[2,[3,[4,[5,]]]]]
# for i in l:
#     print(i)
#递归
# def search(l):
#     for item in l:
#         if type(item) is not  list:
#             print(item)
#         else:
#             search(item)
#
# search(l)
#二分法
nums=[13,15,17,23,31,53,74,81,93,102,103,201,303,403,503,777]
def serache(n):
    print(n)
    num1=503
    num=(len(n)-1)//2
    num2=n[num]
    if num2 > num1:
        n=n[-num:]
        serache(n)
    elif num2 < num1:
        n=n[num:]
        serache(n)
    else:
        print("find it le %s == %s"%(num1,num2))
serache(nums)


l=[1,2,10,30,33,99,101,200,301,311,402,403,500,900,1000] #从小到大排列的数字列表

def search(n,l):
    print(l)
    if len(l) == 0:
        print('not exists')
        return
    mid_index=len(l) // 2
    if n > l[mid_index]:
        #in the right
        l=l[mid_index+1:]
        search(n,l)
    elif n < l[mid_index]:
        #in the left
        l=l[:mid_index]
        search(n,l)
    else:
        print('find it')


search(3,l)

#三元表达式：
 # res=条件成立情况下放回值 if 条件 else 条件不成立的情况先返回值
def max2(x,y):
    if x>y:
        return x
    else:
        return y
name=input("your name>>>:").strip()
res="sb" if  name=='qlz' else 'nb'
print(res)

x=19;y=20;z=30
res1= x if x>y else z
print(res1)