# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 11:44:14
# LastEditTime: 2020-03-08 12:03:51
# LastEditors: ssdcxy
# Description: 将有序数组转换为二叉搜索树
# FilePath: /arithmetic_oj/LeetCode/P0108.py

import json
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def recursive(start, end):
            if start > end: return None
            mid = (start+end) // 2
            root = TreeNode(nums[mid])
            root.left = recursive(start, mid-1)
            root.right = recursive(mid+1, end)
            return root
        return recursive(0, len(nums)-1)


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
            nums = stringToIntegerList(line);
            
            ret = Solution().sortedArrayToBST(nums)

            out = treeNodeToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()