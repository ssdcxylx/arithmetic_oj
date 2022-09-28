# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 13:55:20
# LastEditTime: 2020-03-11 14:15:11
# LastEditors: ssdcxy
# Description: 二叉搜索树与双向链表
# FilePath: /arithmetic_oj/JianzhiOffer/36.py


# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: Node) -> Node:
        if not root: return None
        stack = []
        cur = root
        pre = head = tail = None
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            tail = cur
            if not pre:
                head = cur
            else:
                pre.right = cur
                cur.left = pre
            pre = cur
            cur = cur.right
        tail.right = head
        head.left = tail
        return head
