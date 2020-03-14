# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 16:36:15
# LastEditTime: 2020-02-23 16:58:34
# LastEditors: ssdcxy
# Description: 分隔链表
# FilePath: /arithmetic_oj/LeetCode/P0725.py

import json
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def splitListToParts(self, root: ListNode, k: int) -> List[ListNode]:
        n = 0
        cur = root
        while cur:
            n += 1
            cur = cur.next
        res = []
        mod = n % k
        size = n // k
        cur = root
        for i in range(k):
            res.append(cur)
            if cur:
                curSize = size
                if mod > 0:
                    curSize += 1
                    mod -= 1
                while int(curSize)-1:
                    cur = cur.next
                    curSize -= 1
                _next = cur.next
                cur.next = None
                cur = _next
        return res

def stringToListNode(input):
    # Generate list from the input
    numbers = json.loads(input)

    # Now convert that list into linked list
    dummyRoot = ListNode(0)
    ptr = dummyRoot
    for number in numbers:
        ptr.next = ListNode(number)
        ptr = ptr.next

    ptr = dummyRoot.next
    return ptr

def stringToInt(input):
    return int(input)

def listNodeToString(node):
    if not node:
        return "[]"

    result = ""
    while node:
        result += str(node.val) + ", "
        node = node.next
    return "[" + result[:-2] + "]"

def listNodeArrayToString(listNodeArray):
    serializedListNodes = []
    for listNode in listNodeArray:
        serializedListNode = listNodeToString(listNode)
        serializedListNodes.append(serializedListNode)
    return "[{}]".format(', '.join(serializedListNode))

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToListNode(line)
            line = next(lines)
            k = stringToInt(line)
            
            ret = Solution().splitListToParts(root, k)

            out = listNodeArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()