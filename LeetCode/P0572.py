# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-02 08:32:52
# LastEditTime: 2020-03-02 09:18:05
# LastEditors: ssdcxy
# Description: 另一个树的子树
# FilePath: /arithmetic_oj/LeetCode/P0572.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def isEqual(n1, n2):
            if not n1 and not n2:
                return True
            if not n1 or not n2:
                return False
            if n1.val == n2.val:
                return isEqual(n1.left, n2.left) and isEqual(n1.right, n2.right)
            return False
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val == t.val:
            return isEqual(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
        return self.isSubtree(s.left, t) or self.isSubtree(s.right, t)

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
            s = stringToTreeNode(line);
            line = next(lines)
            t = stringToTreeNode(line);
            
            ret = Solution().isSubtree(s, t)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()