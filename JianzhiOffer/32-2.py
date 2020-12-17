# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 21:57:12
# LastEditTime: 2020-12-01 22:17:13
# LastEditors: ssdcxy
# Description: 从上到下打印二叉树 II
# FilePath: /arithmetic_oj/JianzhiOffer/32-2.py

import json
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        def bfs(node, level):
            if not node: return
            if len(res) <= level:
                if node.left or node.right:
                    res.append([])
            if level & 1:
                if node.right:
                    res[level].(node.right.val)
                if node.left:
                    res[level].append(node.left.val)
            else:
                if node.left:
                    res[level].append(node.left.val)
                if node.right:
                    res[level].append(node.right.val)
            bfs(node.left, level+1)
            bfs(node.right, level+1)
        if not root: return []
        res = [[root.val]]
        bfs(root, 1)
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
            
            ret = Solution().levelOrder(root)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()