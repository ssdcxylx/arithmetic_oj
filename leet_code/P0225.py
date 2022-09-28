# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 08:35:55
# LastEditTime: 2020-03-03 09:08:09
# LastEditors: ssdcxy
# Description: 用队列实现栈
# FilePath: /arithmetic_oj/LeetCode/P0225.py

from collections import deque

class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q1 = deque()
        self.q2 = deque()


    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.q1.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        tmp = self.q1.popleft()
        self.q1, self.q2 = self.q2, self.q1
        return tmp


    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        while len(self.q1) != 1:
            self.q2.append(self.q1.popleft())
        tmp = self.q1.popleft()
        self.q2.append(tmp)
        self.q1, self.q2 = self.q2, self.q1
        return tmp


    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.q1 and not self.q2


# Your MyStack object will be instantiated and called as such:
obj = MyStack()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.top())
print(obj.pop())
print(obj.empty())
print(obj.pop())
print(obj.empty())