# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 10:21:59
# LastEditTime: 2020-03-10 10:28:11
# LastEditors: ssdcxy
# Description: 删除链表的节点
# FilePath: /arithmetic_oj/JianzhiOffer/18.py

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        root = ListNode(-1)
        root.next = head
        if head.val == val:
            return head.next
        while head.next:
            if head.next.val == val:
                head.next = head.next.next
                return root.next
            else:
                head = head.next
        return root.next
            

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
            val = int(line);
            
            ret = Solution().deleteNode(head, val)

            out = listNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()