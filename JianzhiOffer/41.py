# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 16:58:33
# LastEditTime: 2020-03-11 18:30:32
# LastEditors: ssdcxy
# Description: 数据流中的中位数
# FilePath: /arithmetic_oj/JianzhiOffer/41.py

from heapq import *

class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) == len(self.min_heap):
            heapq.heappush(self.min_heap, -heapq.heappushpop(self.max_heap, -num))
        else:
            heapq.heappush(self.max_heap, -heapq.heappushpop(self.min_heap, num))

    def findMedian(self) -> float:
        if len(self.min_heap) == len(self.max_heap):
            return (self.min_heap[0] + -self.max_heap[0]) / 2
        else:
            return self.min_heap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()