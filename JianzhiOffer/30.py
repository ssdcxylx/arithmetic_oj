# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 18:13:06
# LastEditTime: 2020-11-26 23:35:28
# LastEditors: ssdcxy
# Description: 包含min函数的栈
# FilePath: /arithmetic_oj/JianzhiOffer/30.py

class MinStack:

    def __init__(self):
        self.lst1, self.lst2 = [], []

    def push(self, x: int) -> None:
        self.lst1.append(x)
        if not self.lst2 or self.lst2[-1] >= x:
            self.lst2.append(x)

    def pop(self) -> None:
        if self.lst1.pop() == self.lst2[-1]:
            self.lst2.pop()


    def top(self) -> int:
        return self.lst1[-1] if self.lst1 else float('inf')


    def min(self) -> int:
        return self.lst2[-1] if self.lst1 else float('inf')


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()