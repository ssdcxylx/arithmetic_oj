# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-13 21:33:46
# LastEditTime: 2020-12-13 21:53:30
# LastEditors: ssdcxy
# Description: 队列的最大值
# FilePath: /arithmetic_oj/JianzhiOffer/59-2.py

import queue

class MaxQueue:

    def __init__(self):
        self.deque = queue.deque()
        self.queue = queue.Queue();
        

    def max_value(self) -> int:
        return self.deque[0] if self.deque else -1


    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value)

    def pop_front(self) -> int:
        if not self.queue:
             return -1
        ans = self.queue.get()
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans
        
        

obj = MaxQueue()
print(obj.pop_front())