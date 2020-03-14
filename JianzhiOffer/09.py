# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 08:11:38
# LastEditTime: 2020-03-10 08:13:36
# LastEditors: ssdcxy
# Description: 用两个栈实现队列
# FilePath: /arithmetic_oj/JianzhiOffer/09.py

class CQueue:

    def __init__(self):
        self.lst1 = []
        self.lst2 = []


    def appendTail(self, value: int) -> None:
        self.lst1.append(value)
        


    def deleteHead(self) -> int:
        def shift():
            if not self.lst2:
                while self.lst1:
                    self.lst2.append(self.lst1.pop())
        shift()
        if self.lst2:
            return self.lst2.pop()
        else:
            return -1




# Your CQueue object will be instantiated and called as such:
# obj = CQueue()
# obj.appendTail(value)
# param_2 = obj.deleteHead()