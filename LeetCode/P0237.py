# -*- coding: utf-8 -*-
# @time       : 2019-10-24 23:42
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : P0237.py
# @description: 删除链表中的节点

import json


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node, n):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        p = node
        while p.val != n:
            p = p.next
        p.val = p.next.val
        p.next = p.next.next



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
            node = stringToListNode(line);
            line = next(lines)
            n = int(line);

            ret = Solution().deleteNode(node, n)

            out = listNodeToString(node)
            if ret is not None:
                print
                "Do not return anything, modify node in-place instead."
            else:
                print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
