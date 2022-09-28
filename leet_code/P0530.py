# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 14:06:42
# LastEditTime: 2020-03-08 14:17:26
# LastEditors: ssdcxy
# Description: 二叉搜索树的最小绝对差
# FilePath: /arithmetic_oj/LeetCode/P0530.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        def inOrder(node):
            nonlocal preNode, _min
            if not node: return node
            inOrder(node.left)
            if preNode: _min = min(_min, abs(preNode.val-node.val))
            preNode = node
            inOrder(node.right)
        preNode = None
        _min = float('inf')
        inOrder(root)
        return _min

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
            
            ret = Solution().getMinimumDifference(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()