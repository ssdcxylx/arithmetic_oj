# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-09 21:50:46
# LastEditTime: 2020-11-23 19:45:17
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
        def build(p_cur, i_left, i_right):
            if i_left > i_right: return
            root = TreeNode(preorder[p_cur])
            i_pos = dic[preorder[p_cur]]
            root.left = build(p_cur+1, i_left, i_pos-1)
            root.right = build(p_cur+i_pos-i_left+1, i_pos+1, i_right)
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