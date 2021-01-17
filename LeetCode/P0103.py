# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-26 09:06:49
# LastEditTime: 2020-12-22 09:33:06
# LastEditors: ssdcxy
# Description: 二叉树的锯齿形层次遍历
# FilePath: /arithmetic_oj/LeetCode/P0103.py

import json
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(node, level):
            if level >= len(res):
                res.append([])
            if level & 1:
                res[level].insert(0, node.val)
            else:
                res[level].append(node.val)
            if node.left: bfs(node.left, level+1)
            if node.right: bfs(node.right, level+1)
        if not root: return []
        res = []
        bfs(root, 0)
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
            
            ret = Solution().zigzagLevelOrder(root)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()