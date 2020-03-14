# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-09 21:50:46
# LastEditTime: 2020-03-09 22:28:33
# LastEditors: ssdcxy
# Description: 重建二叉树
# FilePath: /arithmetic_oj/JianzhiOffer/07.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        def build(pre, left, right):
            if left > right: return
            root = TreeNode(preorder[pre])
            i = dic[preorder[pre]]
            root.left = build(pre+1, left, i-1)
            root.right = build(i-left+pre+1, i+1, right)
            return root
        dic = {}
        n = len(preorder)
        for i in range(n):
            dic[inorder[i]] = i
        return build(0, 0, n-1)

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