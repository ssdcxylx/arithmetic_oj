# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 14:09:08
# LastEditTime: 2020-02-20 14:24:37
# LastEditors: ssdcxy
# Description: 二叉树的所有路径
# FilePath: /arithmetic_oj/LeetCode/P0257.py

import json
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def backtrack(node: TreeNode, path):
            if node.left is None and node.right is None:
                res.append(path)
                return
            if node.left is not None:
                left_path = path + ("->" + str(node.left.val))
                backtrack(node.left, left_path)
            if node.right is not None:
                right_path = path + ("->" + str(node.right.val))
                backtrack(node.right, right_path)

        if root is None:
            return []
        res = []
        backtrack(root, str(root.val))
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

def stringArrayToString(input):
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
            
            ret = Solution().binaryTreePaths(root)

            out = stringArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()