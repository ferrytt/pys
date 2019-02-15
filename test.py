#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib3.request

print "Hello, Python!";
counter = 100 # 赋值整型变量
miles = 1000.0 # 浮点型
name = "John" # 字符串

def aaa(a):
	return a + 3

class Man(object):
	"""docstring for ClassName"""
	def __init__(self, arg):
		super(Man, self).__init__()
		self.arg = arg
	def bark(self):
		return self.arg + 'aaa'	
	
 
print counter
print miles
print name
print(aaa(2))
man = Man('sb')
print(man.bark())
