# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 14:15:41
# LastEditTime: 2020-03-11 15:08:26
# LastEditors: ssdcxy
# Description: 序列化二叉树
# FilePath: /arithmetic_oj/JianzhiOffer/37.py

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root: return None
        res = []
        stack = [root]
        while stack:
            node = stack.pop(0)
            if not node:
                res.append(None)
            else:
                res.append(node.val)
                stack.append(node.left)
                stack.append(node.right)
        return res
            

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data: return None
        root = TreeNode(data[0])
        stack = [root]
        i = 1
        n = len(data)
        while stack:
            cur = stack.pop(0)
            if not cur: continue
            if i < n:
                if data[i] == "null":
                    left = None
                else:
                    left = TreeNode(data[i])
                    stack.append(left)
                i += 1
            if i < n:
                if data[i] == "null":
                    right = None
                else:
                    right = TreeNode(data[i])
                    stack.append(right)
                i += 1
            cur.left = left
            cur.right = right
                

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

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
            
            ret = Solution().Codec(root)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()