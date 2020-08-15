#!/usr/bin/env python
# coding:utf-8
# Author:fyt
#unicode：可以对应万国字符，统一使用2Bytes对应一个字符
#两个特点
 #1.可以兼容万国字符
 #2.与万国字符编码都有一种数字与数字的对应关系
 #GBK--->解码decode----->unicode
 #shirt-jis数字----》解码decode----->unicode
#utf8:
  #3个Bytes对应一个中文字符
  #1Bytes对应一个英文字符
#保证不乱码
#保证不乱码的关键:
#            字符当初以什么编码的,就应该以什么编码取解码

#            强调:此时计算机只使用unicode与字符的对应关系


#python2，不告诉编码的情况下，默认使用的编码是ascii
#python3,默认是用的编码是utf-8

#文件头：在文件的首行写上：coding:utf-8
       #告诉python解释器，需要使用utf-8去解析文件中的代码

#在python3中:
            #1 (执行python程序的第二个阶段)解释器在将test.py当普通的文本文件读入内存时默认使用的编码是UTF-8
            #2 (执行python程序的第三个阶段,开始识别语法),会字符类型的值开辟一个内存空间存入unicode格式的二进制
            #    即python3中的str类型是unicode编码的二进制
x="上"

res1=x.encode('utf-8') #编码
print(res1)

res2=x.encode('gbk') #编码
print(res2)

res3=res1.decode('utf-8') #解码
print(res3)

res4=res2.decode('gbk')#解码
print(res4)