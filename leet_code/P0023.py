# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-19 09:24:27
# LastEditTime: 2020-03-30 09:58:05
# LastEditors: ssdcxy
# Description: 合并K个排序链表
# FilePath: /arithmetic_oj/LeetCode/P0023.py

import json
from typing import List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        def merge(left, right):
            if left == right: return lists[left]
            mid = (left + right) >> 1
            l = merge(left, mid)
            r = merge(mid+1, right)
            return mergeTwoLists(l, r)
        def mergeTwoLists(lst1, lst2):
            if not lst2: return lst1
            if not lst1: return lst2 
            if lst1.val < lst2.val:
                lst1.next = mergeTwoLists(lst1.next, lst2)
                return lst1
            else:
                lst2.next = mergeTwoLists(lst1, lst2.next)
                return lst2
        if not lists: return None
        n = len(lists)
        return merge(0, n-1)
            
        

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

def stringToListNodeArray(input):
    listNodeArrays = json.loads(input)
    nodes = []
    for listNodeArray in listNodeArrays:
        nodes.append(stringToListNode(json.dumps(listNodeArray)))
    return nodes

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
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            lists = stringToListNodeArray(line)
            
            ret = Solution().mergeKLists(lists)

            out = listNodeToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()