# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-26 09:24:59
# LastEditTime: 2020-03-26 09:56:01
# LastEditors: ssdcxy
# Description: N皇后
# FilePath: /arithmetic_oj/LeetCode/P0051.py

import json
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def can_place(row, col):
            return not (cols[col] + diagonal[row-col] + anti_diagonal[row+col])
        def place_queen(row, col):
            queen.add((row, col))
            cols[col] = 1
            diagonal[row-col] = 1
            anti_diagonal[row+col] = 1
        def remove_queen(row, col):
            queen.remove((row, col))
            cols[col] = 0
            diagonal[row-col] = 0
            anti_diagonal[row+col] = 0
        def add_solution():
            solution = []
            for _, col in sorted(queen):
                solution.append('.'*col+'Q'+'.'*(n-col-1))
            res.append(solution)
        def backtrack(row):
            for col in range(n):
                if can_place(row, col):
                    place_queen(row, col)
                    if row == n - 1:
                        add_solution()
                    else:
                        backtrack(row+1)
                    remove_queen(row, col)
        cols = [0] * n
        diagonal = [0] * (2*n - 1)
        anti_diagonal = [0] * (2*n - 1)
        res = []
        queen = set()
        backtrack(0)
        return res


def stringToInt(input):
    return int(input)

def string2dArrayToString(input):
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
            n = stringToInt(line)
            
            ret = Solution().solveNQueens(n)

            out = string2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()