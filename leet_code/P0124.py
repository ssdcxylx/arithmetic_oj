# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-20 11:46:06
# LastEditTime: 2020-03-20 12:04:39
# LastEditors: ssdcxy
# Description: 二叉树中的最大路径和
# FilePath: /arithmetic_oj/LeetCode/P0124.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def maxPathSum(node):
            nonlocal ans
            if not node: return 0
            val = node.val
            left = max(0, maxPathSum(node.left))
            right = max(0, maxPathSum(node.right))
            ans = max(ans, sum1 + sum2 + val)
            return max(sum1, sum2) + val
        ans = -float('inf')
        maxPathSum(root)
        return ans

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
            
            ret = Solution().maxPathSum(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()