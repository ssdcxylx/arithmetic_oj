# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 23:36:15
# LastEditTime: 2019-12-10 20:20:47
# LastEditors: ssdcxy
# Description: 环形链表
# FilePath: /arithmetic_oj/LeetCode/P0141.py


import json


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head:
            return False
        l1, l2 = head, head.next
        while l1 and l2 and l2.next:
            if l1 == l2:
                return True
            l1 = l1.next
            l2 = l2.next.next
        return False


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
            head = stringToListNode(line)
            line = next(lines)
            pos = int(line)

            ret = Solution().hasCycle(head, pos)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
