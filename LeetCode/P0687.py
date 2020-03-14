# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-02 09:36:33
# LastEditTime: 2020-03-02 09:56:43
# LastEditors: ssdcxy
# Description: 最长同值路径
# FilePath: /arithmetic_oj/LeetCode/P0687.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root):
            nonlocal path
            if not root: return 0
            left = dfs(root.left)
            right = dfs(root.right)
            leftPath = left + 1 if root.left and root.left.val == root.val else 0
            rightPath = right + 1 if root.right and root.right.val == root.val else 0
            path = max(path, leftPath + rightPath)
            return max(leftPath, rightPath)
        path = 0
        dfs(root)
        return path

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
            
            ret = Solution().longestUnivaluePath(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()