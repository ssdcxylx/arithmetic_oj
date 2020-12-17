# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-21 13:49:27
# LastEditTime: 2020-03-21 14:10:04
# LastEditors: ssdcxy
# Description: 验证二叉搜索树
# FilePath: /arithmetic_oj/LeetCode/P0098.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def recursive(node, low, high):
            if not node: return True
            val = node.val
            if val <= low or val >= high:
                return False
            if not recursive(node.left, low, val):
                return False
            if not recursive(node.right, val, high):
                return False
            return True
        return recursive(root, float('-inf'), float('inf'))


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
            
            ret = Solution().isValidBST(root)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()