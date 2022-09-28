# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 08:48:49
# LastEditTime: 2020-03-11 09:38:34
# LastEditors: ssdcxy
# Description: 二叉树中和为某一值的路径
# FilePath: /arithmetic_oj/JianzhiOffer/34.py

import json
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        def backtrack(node, _sum):
            if node:
                if not node.left and not node.right:
                    val = node.val
                    path.append(val)
                    if _sum - val == 0:
                        res.append(path[0:])
                    path.pop()
                val = node.val
                path.append(val)
                backtrack(node.left, _sum-val)
                backtrack(node.right, _sum-val)
                path.pop()
        res, path = [], []
        backtrack(root, sum)
        return res


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

def stringToInt(input):
    return int(input)

def int2dArrayToString(input):
    return json.dumps(input)

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
            line = next(lines)
            sum = stringToInt(line)
            
            ret = Solution().pathSum(root, sum)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()