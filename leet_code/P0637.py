# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 07:31:16
# LastEditTime: 2020-03-08 07:46:04
# LastEditors: ssdcxy
# Description: 二叉树的层平均值
# FilePath: /arithmetic_oj/LeetCode/P0637.py

import json
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        import queue
        ret = []
        if not root: return []
        queue = queue.Queue()
        queue.put(root)
        while not queue.empty():
            cnt = queue.qsize()
            _sum = 0
            for i in range(cnt):
                node = queue.get()
                _sum += node.val
                if node.left:
                    queue.put(node.left)
                if node.right:
                    queue.put(node.right)
            ret.append(_sum/cnt)
        return ret
                


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

def doubleToString(input):
    if input is None:
        input = 0
    return "%.5f" % input

def doubleListToString(nums, len_of_list=None):
    if nums is None or len_of_list == 0:
        return "[]"

    if len_of_list is None:
        len_of_list = len(nums)

    serializedDoubles = []
    for num in nums:
        serializedDoubles.append(doubleToString(num))
    return "[{}]".format(','.join(serializedDoubles))

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            root = stringToTreeNode(line)
            
            ret = Solution().averageOfLevels(root)

            out = doubleListToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()