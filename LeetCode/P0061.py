# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 17:07:30
# LastEditTime: 2020-03-19 17:51:43
# LastEditors: ssdcxy
# Description: 旋转链表
# FilePath: /arithmetic_oj/LeetCode/P0061.py

import json
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head: return None
        n = 1
        tmp = head
        while tmp.next:
            tmp = tmp.next
            n += 1
        tmp.next = head
        cur = n - k % n
        while cur:
            tmp = head
            head = head.next
            cur -= 1
        tmp.next = None
        return head
            

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
            line = next(lines)
            k = int(line);
            
            ret = Solution().rotateRight(head, k)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()