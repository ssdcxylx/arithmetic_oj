# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 14:17:52
# LastEditTime: 2020-03-08 14:54:57
# LastEditors: ssdcxy
# Description: 二叉搜索树中的众数
# FilePath: /arithmetic_oj/LeetCode/P0501.py

import json
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        def inOrder(node):
            nonlocal preNode, count, _max
            if not node: return
            inOrder(node.left)
            if preNode:
                if preNode.val == node.val:
                    count += 1
                else:
                    count = 1
            if count > _max:
                _max = count
                nums.clear()
                nums.append(node.val)
            elif count == _max:
                nums.append(node.val)
            print(node.val)
            preNode = node
            inOrder(node.right)
        preNode = None
        count = _max = 1
        nums = []
        inOrder(root)
        return nums


def stringToTreeNode(input):
    input = input.strip()
    input = input[1:-1]
    if not input:
        return None

    inputValues = [s.strip() for s in input.split(',')]
    root = TreeNode(int(inputValues[0]))
    nodeQueue = [root]
    front = 0
    index = 1
    while index < len(inputValues):
        node = nodeQueue[front]
        front = front + 1

        item = inputValues[index]
        index = index + 1
        if item != "null":
            leftNumber = int(item)
            node.left = TreeNode(leftNumber)
            nodeQueue.append(node.left)

        if index >= len(inputValues):
            break

        item = inputValues[index]
        index = index + 1
        if item != "null":
            rightNumber = int(item)
            node.right = TreeNode(rightNumber)
            nodeQueue.append(node.right)
    return root

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

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
            root = stringToTreeNode(line);
            
            ret = Solution().findMode(root)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()