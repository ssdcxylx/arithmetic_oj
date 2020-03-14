# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 10:51:18
# LastEditTime: 2020-02-20 11:46:17
# LastEditors: ssdcxy
# Description: 单词搜索
# FilePath: /arithmetic_oj/LeetCode/P0079.py

import json
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def backtrack(i, row, col, visited):
            if i == n - 1:
                return board[row][col] == word[i]
            deltas = [(1,0), (-1,0), (0, 1), (0, -1)]
            if board[row][col] == word[i]:
                visited[row][col] = True
                for delta in deltas:
                    if 0 <= row+delta[0] < rows and 0 <= col+delta[1] < cols:
                        if not visited[row+delta[0]][col+delta[1]]:
                            if board[row+delta[0]][col+delta[1]] == word[i+1]:
                                visited[row+delta[0]][col+delta[1]] = True
                                if backtrack(i+1, row+delta[0], col+delta[1], visited):
                                    return True
                visited[row][col] = False
            return False
                                    
        rows, cols = len(board), len(board[0])
        n = len(word)
        res = []
        visited = [[False for col in range(cols)] for row in range(rows)]
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0]:
                    if backtrack(0, row, col, visited):
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