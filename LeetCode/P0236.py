# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-08 21:31:19
# LastEditTime: 2019-12-10 20:22:41
# LastEditors: ssdcxy
# Description: 二叉树的最近公共祖先
# FilePath: /arithmetic_oj/LeetCode/P0236.py


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.res = None
        self.dfs(root, p, q)
        return self.res

    def dfs(self, root, p, q):
        if not root:
            return 0
        left = self.dfs(root.left, p, q)
        right = self.dfs(root.right, p, q)
        mid = (root == p or root == q)
        if left + right + mid > 1:
            self.res = root
        return left or right or mid


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


def stringtoNode(root, input):
    cur = [root]
    while len(cur) > 0:
        temp = []
        for i in range(len(cur)):
            if cur[i].val == int(input):
                return cur[i]
            if cur[i].left is not None:
                temp.append(cur[i].left)
            if cur[i].right is not None:
                temp.append(cur[i].right)
        cur = temp
    return None


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
            root = stringToTreeNode(line)
            line = next(lines)
            p = stringtoNode(root, line)
            line = next(lines)
            q = stringtoNode(root, line)

            ret = Solution().lowestCommonAncestor(root, p, q)

            out = treeNodeToString(ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
