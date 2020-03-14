# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 18:13:06
# LastEditTime: 2020-03-10 18:26:26
# LastEditors: ssdcxy
# Description: 包含min函数的栈
# FilePath: /arithmetic_oj/JianzhiOffer/30.py

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.lst = list()
        self._min = float('inf')


    def push(self, x: int) -> None:
        if x < self._min:
            self._min = x
        self.lst.append(x)

    def pop(self) -> None:
        if self.lst:
            val = self.lst[-1]
            self.lst = self.lst[:len(self.lst)-1]
            if val == self._min:
                if self.lst:
                    self._min = min(self.lst)
                else:
                    self._min = float('inf')


    def top(self) -> int:
        if self.lst:
            return self.lst[-1]
        else:
            return float('inf')


    def min(self) -> int:
        return self._min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()