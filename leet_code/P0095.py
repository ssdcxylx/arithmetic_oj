# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-20 22:15:13
# LastEditTime: 2019-12-21 00:20:02
# LastEditors: ssdcxy
# Description:不同的二叉搜索树 II
# FilePath: /arithmetic_oj/LeetCode/P0095.py

# Definition for a binary tree node.

from typing import List


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def generateTrees(self, n: int) -> List[TreeNode]:
        def resurive(start, end):
            res = []
            if start > end:
                res.append(None)
                return res
            for i in range(start, end+1):
                left = resurive(start, i-1)
                right = resurive(i+1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)
            return res
        if n < 1:
            return []
        return resurive(1, n)


def stringToInt(input):
    return int(input)


def treeNodeToString(root):
    if not root:
        return "[]"
    output = ""
    queue = [root]
    current = 0
    while current != len(queue):
        node = queue[current]
        current = current + 1

        if not node:
            output += "null, "
            continue

        output += str(node.val) + ", "
        queue.append(node.left)
        queue.append(node.right)
    return "[" + output[:-2] + "]"


def treeNodeArrayToString(treeNodeArray):
    serializedTreeNodes = []
    for treeNode in treeNodeArray:
        serializedTreeNode = treeNodeToString(treeNode)
        serializedTreeNodes.append(serializedTreeNode)
    return "[{}]".format(', '.join(serializedTreeNodes))


def main():
    import sys

    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            n = stringToInt(line)

            ret = Solution().generateTrees(n)

            out = treeNodeArrayToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
