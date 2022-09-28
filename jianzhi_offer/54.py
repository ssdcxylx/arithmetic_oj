# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 10:54:00
# LastEditTime: 2020-12-09 09:36:50
# LastEditors: ssdcxy
# Description: 二叉搜索树的第k大节点
# FilePath: /arithmetic_oj/JianzhiOffer/54.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def kthLargest(self, root: TreeNode, k: int) -> int:
        # 递归
        def mid_travel(cur):
            nonlocal k, ans
            if cur.right: mid_travel(cur.right)
            k -= 1
            if not k:
                ans = cur.val
                return
            if cur.left: mid_travel(cur.left)
        ans = 0
        mid_travel(root)
        return ans
        
        # 利用栈实现递归
        # if not root: return -1
        # stack = []
        # cur = root
        # while cur or stack:
        #     while cur:
        #         stack.append(cur)
        #         cur = cur.right
        #     node = stack.pop()
        #     k -= 1
        #     if not k:
        #         return node.val
        #     cur = node.left
        # return -1

        
        

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
            line = next(lines)
            k = int(line);
            
            ret = Solution().kthLargest(root, k)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()