# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 10:52:38
# LastEditTime: 2020-02-23 11:44:34
# LastEditors: ssdcxy
# Description: 两数相加 II
# FilePath: /arithmetic_oj/LeetCode/P0445.py

import json
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def add(num1, num2, i, j):
            if not i or not j : return 0
            if num1 > num2:
                tmp = i.val + add(num1-1, num2, i.next, j)
            else:
                tmp = i.val + j.val + add(num1-1, num2, i.next, j.next)
            i.val = tmp % 10
            return tmp // 10
        num1 = num2 = 0
        cur = l1
        while cur:
            num1 += 1
            cur = cur.next
        cur = l2
        while cur:
            num2 += 1
            cur = cur.next
        if num2 > num1:
            l1, l2 = l2, l1
            num1, num2 = num2, num1
        if add(num1, num2, l1, l2):
            l2 = ListNode(1)
            l2.next = l1
            l1 = l2
        return l1
        

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
            
            ret = Solution().addTwoNumbers(l1, l2)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()