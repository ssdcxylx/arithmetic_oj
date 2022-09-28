# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-23 15:29:14
# LastEditTime: 2020-02-23 15:57:37
# LastEditors: ssdcxy
# Description: 回文链表
# FilePath: /arithmetic_oj/LeetCode/P0234.py

import json
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def cut(head, slow):
            while head.next != slow:
                head = head.next
            head.next = None
        def reverse(head):
            newHead = None
            while head:
                newNode = head.next
                head.next = newHead
                newHead = head
                head = newNode
            return newHead
        def isEqual(l1, l2):
            while l1 and l2:
                if l1.val != l2.val: return False
                l1 = l1.next
                l2 = l2.next
            return True
        if not head or not head.next: return True
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        cut(head, slow)
        return isEqual(head, reverse(slow))
        
        
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
            head = stringToListNode(line);
            
            ret = Solution().isPalindrome(head)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()