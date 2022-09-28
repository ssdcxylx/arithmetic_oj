# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 15:30:26
# LastEditTime: 2020-02-20 16:52:19
# LastEditors: ssdcxy
# Description: 被围绕的区域
# FilePath: /arithmetic_oj/LeetCode/P0130.py

import json
from typing import List

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def dfs(row, col):
            if row < 0 or col < 0 or row >= rows or col >= cols or board[row][col] != "O":
                return
            board[row][col] = "#"
            for delta in deltas:
                dfs(row+delta[0], col+delta[1])
        if not board: return
        rows, cols = len(board), len(board[0])
        if rows < 3 or cols < 3: return
        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for row in range(rows):
            dfs(row, 0)
            dfs(row, cols-1)
        for col in range(cols):
            dfs(0 ,col)
            dfs(rows-1, col)
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "O":
                    board[row][col] = "X"
                if board[row][col] == "#":
                    board[row][col] = "O"
                

def stringToChar2dArray(input):
    return json.loads(input)

def char2dArrayToString(input):
    return json.dumps(input)

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
            
            ret = Solution().solve(board)

            out = char2dArrayToString(board)
            if ret is not None:
                print("Do not return anything, modify board in-place instead.")
            else:
                print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()