# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 10:12:09
# LastEditTime: 2020-03-08 11:01:45
# LastEditors: ssdcxy
# Description: 键值映射
# FilePath: /arithmetic_oj/LeetCode/P0677.py

class MapSum:

    class Node:
        def __init__(self, x=0):
            self.childs = [None]*26
            self.val = x

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = self.Node()

    def insert(self, key: str, val: int) -> None:
        def _insert(key:str, val:str, node) -> None:
            if not node: return
            if not key:
                node.val = val
                return
            index = ord(key[0]) - ord('a')
            if not node.childs[index]:
                node.childs[index] = self.Node()
            return _insert(key[1:], val, node.childs[index])
        return _insert(key, val, self.head)
        

    def sum(self, prefix: str) -> int:
        def _sum(prefix:str, node) -> int:
            if not node: return 0
            if prefix:
                index = ord(prefix[0]) - ord('a')
                return _sum(prefix[1:], node.childs[index])
            ans = node.val
            for child in node.childs:
                ans += _sum(prefix, child)
            return ans 
        return _sum(prefix, self.head)  

# Your MapSum object will be instantiated and called as such:
obj = MapSum()
obj.insert('aa',3)
obj.insert('aa',2)
print(obj.sum('aa'))