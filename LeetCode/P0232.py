# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 08:11:25
# LastEditTime: 2020-03-03 08:33:56
# LastEditors: ssdcxy
# Description: 用栈实现队列
# FilePath: /arithmetic_oj/LeetCode/P0232.py

class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.lst1 = list()
        self.lst2 = list()


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.lst1.append(x) 

    

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        def shift():
            if not self.lst2:
                while self.lst1:
                    self.lst2.append(self.lst1.pop())
        shift()
        if self.lst2:
            return self.lst2.pop()
        raise Exception("列表为空")
        
        
    def peek(self) -> int:
        """
        Get the front element.
        """
        def shift():
            if not self.lst2:
                while self.lst1:
                    self.lst2.append(self.lst1.pop())
        shift()
        if self.lst2:
            return self.lst2[-1]
        raise Exception("列表为空")



    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.lst1 and not self.lst2



# Your MyQueue object will be instantiated and called as such:
obj = MyQueue()
obj.push(1)
obj.push(2)
obj.push(3)
print(obj.pop())
print(obj.peek())
print(obj.pop())
print(obj.empty())