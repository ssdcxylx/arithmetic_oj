# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-27 07:21:15
# LastEditTime: 2020-03-27 07:28:17
# LastEditors: ssdcxy
# Description: 从前序与中序遍历序列构造二叉树
# FilePath: /arithmetic_oj/LeetCode/P0105.py

import json
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def helper(in_left, in_right):
            nonlocal pre_idx
            if in_left == in_right:
                return None
            root_val = preorder[pre_idx]
            root = TreeNode(root_val)
            index = idx_map[root_val]
            pre_idx += 1
            root.left = helper(in_left, index)
            root.right = helper(index+1, in_right)
            return root

        pre_idx = 0
        idx_map = {val:idx for idx, val in enumerate(inorder)}
        return helper(0, len(inorder))

def stringToIntegerList(input):
    return json.loads(input)

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
            preorder = stringToIntegerList(line);
            line = next(lines)
            inorder = stringToIntegerList(line);
            
            ret = Solution().buildTree(preorder, inorder)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()