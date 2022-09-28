# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 09:06:00
# LastEditTime: 2020-02-23 09:15:43
# LastEditors: ssdcxy
# Description: 合并两个有序链表
# FilePath: /arithmetic_oj/LeetCode/P0021.py

import json
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(0)
        tmp = head
        while l1 and l2:
            if l1.val >= l2.val:
                tmp.next = ListNode(l2.val)
                tmp = tmp.next
                l2 = l2.next
            else:
                tmp.next = ListNode(l1.val)
                tmp = tmp.next
                l1 = l1.next
        if l1: tmp.next = l1
        if l2: tmp.next = l2
        return head.next
                


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
            l1 = stringToListNode(line);
            line = next(lines)
            l2 = stringToListNode(line);
            
            ret = Solution().mergeTwoLists(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()