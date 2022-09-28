# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-26 08:41:29
# LastEditTime: 2020-03-26 08:52:33
# LastEditors: ssdcxy
# Description: 车的可用捕获量
# FilePath: /arithmetic_oj/LeetCode/P0999.py

import json
from typing import List

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def isEnd(i, j):
            nonlocal ans
            if board[i][j] == 'p':
                ans += 1
                return True
            if board[i][j] == 'B':
                return True
            return False
        def look(i, j):
            nonlocal n
            for k in range(j, -1, -1):
                if isEnd(i, k):
                    break
            for k in range(j, n):
                if isEnd(i, k):
                    break
            for k in range(i, -1, -1):
                if isEnd(k, j):
                    break
            for k in range(i, n):
                if isEnd(k, j):
                    break
        n = len(board)
        ans = 0
        for i in range(n):
            for j in range(n):
                if board[i][j] == 'R':
                    look(i, j)
                    return ans

def stringToChar2dArray(input):
    return json.loads(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = next(lines)
            board = stringToChar2dArray(line)
            
            ret = Solution().numRookCaptures(board)

            out = intToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()

