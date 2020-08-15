#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Author:fyt

#1.定义函数的三种形式
#1.1 无参函数
# def foo():
#   print('x')
#
# #1.2 有参函数
# def func(x,y):
#     print(x,y)
#
# #1.3 空函数
# def func():
#     pass

#调用函数的三种模式
#语句形式
# def foo():
#     print('from foo')
# foo()
#表达式形式
# def foo(x,y):
#     res=x+y
#     return res
# res=foo(1,3)
# print(res*100)

#可以当作参数传给另一个函数
# def max2(x,y):
#     if x>y:
#         return x
#     else:
#         return y
#
# res=max2(max(2,3),1)
# print(res)


#函数的返回值
#返回值没有类型限制

#返回一个值：调用函数拿到的结果就是一个值
#返回多个值：调用函数拿到的结果就是一个元组
#返回0搁置或者没有返回值，函数返回的结构都是None


#return关键字
#函数遇到return就会立即退出，也就是说return是函数结束的标志

# def foo():
#     return [1,3],1,1.3,{'name':'fyt'}
# res=foo()
# print(res)

#函数的参数分为两大类
  #1.1 形参： 在定义阶段括号类指定的变量名，称为形参
  #1.2 实参：指函数在调用阶段括号内传入的值，即实参本质就是“值"

# def foo(x,y): #x y 是形参
#     print(x,y)
# foo(1,2) #1,2是实参


#位置参数和默认参数
#1.1 位置参数：
     # 位置形参：在定义函数阶段按照从左到右的顺序依次定义的形参，称之为位置形参
     # 位置实参：在调用函数阶段按照从左到右的顺序依次定义的形参，称之为位置实参
#但凡按照位置定义的形参，必须被传值，多一个不行，少一个也不行
# def foo(x,y): #位置形参
#     print(x,y)
# foo(1,2) #位置实参


#关键字实参：在调用阶段，按照key=value的形式指名道姓的为形参传值
#注意，关键字参数可以顺序，但任然要指名道姓为指定的形参传值
#可以混合使用位置实参与关键字实参，但是位置实参必须放到关键字实参的前面
# def foo(name,age):
#     print(name,age)
# # foo(age=18,name='fyt') #关键字参数
#
# foo('fyt',age=19)



#默认参数
#默认参数：指的是在定义函数阶段就已经为某个形参赋值了，改形参称之为有默认值的形参，简称默认参数
#默认参数在定义阶段就已经被赋值了，意味着在调用阶段可以不用为其赋值
# def foo(x,y=2): #默认新参
#     print(x,y)
# foo(1,2) #默认实参

# def register(name,age,sex='f'):
#       print(name,age,sex)
# register(name='fyt',age=19)


#位置形参vs默认形参
#对于大多数情况下传的值不相同的，应该定义成位置参数
#对于大多数情况下传的值相同的，应该定义成默认参数

#位置形参必须放到默认形参的前面
#注意
#1.再定义阶段就已经被赋值了，意味着在调用阶段可以不用为其赋值
#2.位置形参应该放到默认形参前面
#3.默认参数的值在函数定义阶段就已经固定死了
#4.默认参数的值通常应该是不可变类型
#
# def foo(x,y='fyt'):
#     print(x)
# foo(1)

# def re(name,hobby,l=None):
#     if l is None:
#         l=[]
#     l.append(hobby)
#     print('%s的hobby is %s'%(name,l))
# re('fyt','ball,cat,run,read')

#函数的可变长参数
#站在实参的角度，参数长度可变指的是在调用函数是，传入的实参值的个数不固定
#而实参的定义方式无法两种，：位置实参，关键字实参，对应侄儿形参一必须有两种解决方法，*与**类分别对以出的位置
#实参与关键字实参

#1.在形参中带*:会将调用函数时溢出位置实参保存成元组的形式，然后复制*后的变量名
#2.再实参中带*,但凡在实参中带*的,在传值前都先将其打散成位置实参，在进行赋值
# def foo(x,y,**kwargs):
#     print(x,y,kwargs)
# foo(1,y=2,c=3)
#
# def foo1(x,y,*args):
#    print(x,y,args)
# # res=foo1(1,2,['ball','read','zpi'])
# # print(res[2][0])
# foo1(*'hello')
# foo1(*[1,2,3,4,5,5])
#2.在形参中带**：会将调用函数是溢出关键字实参保存成字典的形式，然后赋值**后的变量名
#在实参中带**:但凡在实参中带**的，在传值前都先将其打散成关键字实参，在进行赋值
# def foo(x,y,**kwargs):
#     print(x,y,kwargs)
#
# foo(1,2,**{'name':'fyt','age':19})

#5.在形参中带*与**的，*后的变量名应该为args,**后面应该为**kwargs
# def foo(*args,**kwargs):
#     print(args)
#     print(kwargs)
# foo(1,2,3,4,a=1,b=2,c=3)\
#
# def bar(x,y,z):
#     print(x,y,z)
# def foo(*args,**kwargs):
#     bar(*args)
# foo(1,2,a=1)

#命令关键字参数：放到*与**之间的参数称之为命名关键字参数
# def foo(x,y,*args,m,n,**kwargs):
#     print(x,y)
#     print(m,n)
#     print(kwargs)
# foo(1,2,3,4,5,m=2,n=3,a=1,b=2)
#
# def foo(*args,x,y):
#     print(x,y)
# foo(1,2,3,4,5,6,x=1,y=2)

# def foo(*,x=1,y):
#     print(x)
#     print(y)
# foo(y=222,x=111)

def foo(x,y=1,*args,m,**kwargs): #位置参数，默认参数，**args,关键字参数，**kwargs
    print(x)
    print(y)
    print(args)
    print(m)
    print(kwargs)
foo(1,2,[1,2,3,4,5],m=4,a=1,b=2)



