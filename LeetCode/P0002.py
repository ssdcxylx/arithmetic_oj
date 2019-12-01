# -*- coding: utf-8 -*-
# @time       : 2019-10-14 23:08
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0002.py.py
# @description: 两数相加

from typing import List
import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        sum = p1.val + p2.val
        l3 = ListNode(sum % 10)
        p3 = l3
        while p1.next is not None or p2.next is not None:
            v1, v2 = 0, 0
            if p1.next is not None:
                p1 = p1.next
                v1 = p1.val
            if p2.next is not None:
                p2 = p2.next
                v2 = p2.val
            sum = sum // 10 + v1 + v2
            p3.next = ListNode(sum % 10)
            p3 = p3.next
        if sum >= 10:
            p3.next = ListNode(1)
        return l3


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