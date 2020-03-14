# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-08 07:47:10
# LastEditTime: 2020-03-08 08:02:53
# LastEditors: ssdcxy
# Description: 找树左下角的值
# FilePath: /arithmetic_oj/LeetCode/P0513.py

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        import queue
        _q = queue.Queue()
        _q.put(root)
        while not _q.empty():
            cnt = _q.qsize()
            flag = False
            val = -1
            for i in range(cnt):
                node = _q.get()
                
                if not node.left and not node.right:
                    if not flag:
                        val = node.val
                        flag = True
                else:
                    if node.left:
                        _q.put(node.left)
                    if node.right:
                        _q.put(node.right)
            if _q.empty():
                return val

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
            
            ret = Solution().findBottomLeftValue(root)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()