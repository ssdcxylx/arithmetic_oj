# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 12:08:00
# LastEditTime: 2020-03-08 12:36:14
# LastEditors: ssdcxy
# Description: 两数之和 IV - 输入 BST
# FilePath: /arithmetic_oj/LeetCode/P0653.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def inOrder(node):
            nonlocal nums
            if not node: return
            inOrder(node.left)
            nums.append(node.val)
            inOrder(node.right)
        nums = []
        inOrder(root)
        i, j = 0, len(nums) - 1
        while i < j:
            _sum = nums[i] + nums[j]
            if _sum == k: return True
            if _sum < k: i += 1
            else: j -= 1
        return False
        

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
            
            ret = Solution().findTarget(root, k)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()