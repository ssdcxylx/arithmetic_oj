# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 08:24:36
# LastEditTime: 2020-03-11 08:38:00
# LastEditors: ssdcxy
# Description: 二叉搜索树的后序遍历序列
# FilePath: /arithmetic_oj/JianzhiOffer/33.py

class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder or len(postorder) == 1: return True
        n = len(postorder)
        root = postorder[-1]
        part = n - 1
        for i in range(n-1):
            if postorder[i] > root:
                part = i
                break
        left = postorder[:part]
        right = postorder[part:n-1]
        for num in right:
            if num < root:
                return False
        return self.verifyPostorder(left) and self.verifyPostorder(right)

def stringToIntegerList(input):
    return json.loads(input)

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
            postorder = stringToIntegerList(line);
            
            ret = Solution().verifyPostorder(postorder)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()