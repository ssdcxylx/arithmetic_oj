# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 09:39:31
# LastEditTime: 2020-12-01 23:36:31
# LastEditors: ssdcxy
# Description: 复杂链表的复制
# FilePath: /arithmetic_oj/JianzhiOffer/35.py


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: Node = None, random: Node = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Node) -> Node:
        if not head: return head
        cur = head
        while cur:
            new_node = Node(cur.val)
            new_node.next = cur.next
            cur.next = new_node
            cur = new_node.next
        cur = head
        while cur:
            cur.next.random = cur.random.next if cur.random else None
            cur = cur.next.next
        old_list = head
        new_list = head.next
        new_head = head.next
        while old_list:
            old_list.next = old_list.next.next
            new_list.next = new_list.next.next if new_list.next else None
            old_list = old_list.next
            new_list = new_list.next
        return new_head