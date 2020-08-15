# -*- coding: utf-8 -*-
# author: fyt
# time: 2020-2-28

#匿名函数：没有名字的函数
# def sum2(x,y):
#     return x+y
# a=sum2(1,2)
# print(a)

# print((lambda x,y:x+y)(1,2))
# max min sorted map filter  reduce

#匿名函数于其他函数结合使用
salaries={
    'egon':30000,
    'alex':1000000,
    'wupeiqi':10000,
    'yuanhao':2000
}

#求薪资最高的那个人名，即比较的是value，但取得结果是key
#通过max函数的key参数来改变max函数的比较依据，key的值就是比较依据
#可以通过max函数的key参数来改变max函数的比较依据，运行原理
#max函数会‘for循环出一个值，然后将改值传给key指定的函数
#调用key指定函数，将拿到的放回值当做比较
# def func(name):
#     return salaries[name]
#求最大值
# print(max(salaries,key=lambda name:salaries[name]))

# nums=[11,33,22,9,31]
# res=sorted(nums,reverse=True)
# print(res)
#排序
# print(sorted(salaries,key=lambda name:salaries[name],reverse=True))
# names=['alex','lxx_sb','wxx']
#映射
# res=map(lambda name:name+'_dsb',names)
# print(list(res))


#过滤（从一个列表中过滤出符合规则的值)
# a=filter(lambda name:name.endswith('sb'),names)
# for i in a:
#     print(i)

#reduce:把多个值合并成一个结果
from  functools import reduce
# l=['a','b','c']
# a=reduce(lambda x,y:x+y,l,'A')
# print(a)

a=reduce(lambda x,y:x+y,range(101),1)
print(a)
