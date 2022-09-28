# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 08:31:43
# LastEditTime: 2020-03-10 09:01:17
# LastEditors: ssdcxy
# Description: 
# FilePath: /arithmetic_oj/JianzhiOffer/12.py

import json
from typing import List 

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def dfs(i, j, k):
            if not 0 <= i < m or not 0 <= j < n or board[i][j] != word[k]: return False
            if k == l - 1: return True
            tmp, board[i][j] = board[i][j], "/"
            res = dfs(i+1, j, k+1) or dfs(i, j+1, k+1) or dfs(i-1, j, k+1) or dfs(i, j-1, k+1)
            board[i][j] = tmp
            return res
        m, n = len(board), len(board[0])
        l = len(word)
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        return False

def stringToChar2dArray(input):
    return json.loads(input)

def stringToString(input):
    return input[1:-1]

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
            line = next(lines)
            word = stringToString(line)
            
            ret = Solution().exist(board, word)

            out = (ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()