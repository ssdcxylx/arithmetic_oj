# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-02 10:29:41
# LastEditTime: 2020-03-02 10:37:43
# LastEditors: ssdcxy
# Description: 二叉树中第二小的节点
# FilePath: /arithmetic_oj/LeetCode/P0671.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        if not root: return -1
        if not root.left and not root.right: return -1
        leftVal = self.findSecondMinimumValue(root.left) if root.left.val == root.val else root.left.val
        rightVal = self.findSecondMinimumValue(root.right) if root.right.val == root.val else root.right.val
        if leftVal != -1 and rightVal != -1:
            return min(leftVal, rightVal)
        elif leftVal != -1:
            return leftVal
        else:
            return rightVal

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
            
            ret = Solution().findSecondMinimumValue(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()