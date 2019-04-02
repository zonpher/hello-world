#!/usr/bin/env python
# coding=utf-8
'''
第一题方法1：
def Divisible():
li = []
for i in range(2000,3201):
	if i % 7 == 0 and i % 5 != 0:
		li.append(i)
for temp in li:
	length = len(li)
	if li[length-1] == temp:
		print(temp)
	else:
		print(temp,end = ",")
#if __name__ == "__main__":
	#Divisible()
方法2：
l=[]
for i in range(2000, 3201):
	if (i%7==0) and (i%5!=0):
		l.append(str(i)) # 将数字转换为字符串

print (','.join(l))

'''

'''
第2题方法1：
while True:
	a = int(input("Please input a number that you want to compute the factorial:"))
	if a == 0:
		print(1)
	elif a < 0:
		print("输入有误，请重新输入")
	elif a > 0:
		fac = 1
		li = []
		i = 1
		while i <= a:
			fac = fac * i
			i += 1
		li.append(str(fac))	
		print(",".join(li))

'''

'''
第3题
a = int(input("Please input a integral number:"))
dic = {}
for temp in range(1,a+1):
	dic[temp] = temp * temp
print(dic)
'''

'''
第4题
values = input("Please input a series of numbers that separated by a comma:")
l = values.split(",") # 分割后以列表的形式保存
t = tuple(l)
print(l)
print(t)
'''

'''
第5题
class String:
	def __init__(self):
		self.a = ""
	def getString(self):
		self.a = input("Please input a String:")
	def printString(self):
		print(self.a)
B = String()
B.getString()
B.printString()
'''

'''
C = 50
H = 30
l = input("Please input D whose values are seperated by comma: ")
li = l.split(",")
Qs = []
for D in li:
    Q = ((2 * C * float(D))/H)**0.5
    Qs.append(str(int(Q)))
print(",".join(Qs))
'''

'''
第7题
import numpy as np
li = (input("row,column=").split(','))
row = int(li[0])
col = int(li[1])
# print(row)
# print(col)
Array = np.ones((row,col))
for i in range(0,row):
    for j in range(0,col):
        Array[i,j] = i * j
print(Array)
'''

'''
第8题
Strings = input("Please input words seperated by commas:")
words = [word for word in Strings.split(",")]
words.sort()
print(",".join(words))
'''

'''
Q9
lines = [] # 多行输入需要先存进列表中
while True:
    Str = input().upper()
    if Str:
        lines.append(Str)
    else:
        break
for word in lines:
    print(word)
'''






