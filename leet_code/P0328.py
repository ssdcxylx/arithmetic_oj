# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 17:05:50
# LastEditTime: 2020-02-23 18:50:43
# LastEditors: ssdcxy
# Description: 奇偶链表
# FilePath: /arithmetic_oj/LeetCode/P0328.py

import json
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head
        root = head
        a, b = head, head.next
        while b and b.next:
            prev = head.next
            a = a.next.next
            head.next = a
            if b.next:
                a = b
                b.next = b.next.next
                b = b.next
                
            head.next.next = prev
            head = head.next
        return root

def stringToIntegerList(input):
    return json.loads(input)

def stringToListNode(input):
    # Generate list from the input
    numbers = stringToIntegerList(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            head = stringToListNode(line);
            
            ret = Solution().oddEvenList(head)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()