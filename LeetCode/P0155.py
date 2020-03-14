# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 09:10:46
# LastEditTime: 2020-03-03 09:33:14
# LastEditors: ssdcxy
# Description: 最小栈
# FilePath: /arithmetic_oj/LeetCode/P0155.py

class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst1 = list()
        self._min = float('inf')


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if x < self._min:
            self._min = x
        self.lst1.append(x)


    def pop(self):
        """
        :rtype: None
        """
        tmp = self.lst1[-1]
        self.lst1 = self.lst1[:-1]
        if tmp == self._min:
            if self.lst1:
                self._min = min(self.lst1)
            else:
                self._min = float('inf')
        return tmp


    def top(self):
        """
        :rtype: int
        """
        return self.lst1[-1]



    def getMin(self):
        """
        :rtype: int
        """
        return self._min



# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(2)
obj.push(0)
obj.push(3)
obj.push(0)
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())