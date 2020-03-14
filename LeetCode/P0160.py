# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 07:53:01
# LastEditTime: 2020-02-23 08:22:25
# LastEditors: ssdcxy
# Description: 相交链表
# FilePath: /arithmetic_oj/LeetCode/P0160.py

import json
from typing import List

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        tmpA, tmpB = headA, headB
        while tmpA != tmpB:
            tmpA = tmpA.next if tmpA else headB
            tmpB = tmpB.next if tmpB else headA
        return tmpA

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
            intersectVal = int(line);
            line = next(lines)
            listA = stringToListNode(line);
            line = next(lines)
            listB = stringToListNode(line);
            line = next(lines)
            skipA = int(line);
            line = next(lines)
            skipB = int(line);
            
            ret = Solution().getIntersectionNode(listA, listB)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()