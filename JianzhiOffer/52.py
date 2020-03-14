# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 10:16:55
# LastEditTime: 2020-03-12 10:24:50
# LastEditors: ssdcxy
# Description: 两个链表的第一个公共节点
# FilePath: /arithmetic_oj/JianzhiOffer/52.py

import json

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        node1, node2 = headA, headB
        while node1 != node2:
            node1 = node1.next if node1 else headB
            node2 = node2.next if node2 else headA
        return node1



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
            
            ret = Solution().getIntersectionNode(intersectVal, listA, listB, skipA, skipB)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()