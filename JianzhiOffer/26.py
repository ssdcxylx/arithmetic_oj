# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 15:18:22
# LastEditTime: 2020-03-10 15:57:19
# LastEditors: ssdcxy
# Description: 树的子结构
# FilePath: /arithmetic_oj/JianzhiOffer/26.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:
        def isSubTree(node1, node2):
            if not node2:
                return True
            if not node1:
                return False
            return node1.val == node2.val and isSubTree(node1.left, node2.right) and isSubTree(node1.right, node2.right)
        if not A or not B: return False
        return isSubTree(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)

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
            A = stringToTreeNode(line);
            line = next(lines)
            B = stringToTreeNode(line);
            
            ret = Solution().isSubStructure(A, B)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()