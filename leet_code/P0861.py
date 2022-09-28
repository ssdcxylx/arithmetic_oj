# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-17 13:44:35
# LastEditTime: 2020-12-17 13:59:13
# LastEditors: ssdcxy
# Description: 翻转矩阵后的得分
# FilePath: /arithmetic_oj/LeetCode/P0861.py

class Solution(object):
    class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        # def move_row(i):
        #     for j in range(n):
        #         A[i][j] ^= 1
        # def move_col(j):
        #     for i in range(m):
        #         A[i][j] ^= 1
        # def count(j):
        #     count = 0
        #     for i in range(m):
        #         count += 1 if A[i][j] else 0
        #     return count
        # if not A or not A[0]: return 0
        # m, n = len(A), len(A[0])
        # for i in range(m):
        #     if not A[i][0]:
        #         move_row(i)
        # for j in range(1, n):
        #     if count(j) < m/2:
        #         move_col(j)
        # res = 0
        # for i in range(m):
        #     for j in range(n):
        #         if A[i][j]:
        #             res += (2**(n-j-1))
        # return res

        if not A or not A[0]: return 0
        m, n = len(A), len(A[0])
        res = m * (1 << (n-1))
        for j in range(1, n):
            nOnes = 0
            for i in range(m):
                if A[i][0]:
                    nOnes += A[i][j]
                else:
                    nOnes += (1-A[i][j])
            k = max(nOnes, m-nOnes)
            res += k * (1 << (n-j-1))
        return res
                
        
        

def stringToInt2dArray(input):
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
            line = lines.next()
            A = stringToInt2dArray(line)
            
            ret = Solution().matrixScore(A)

            out = intToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()