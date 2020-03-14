# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 08:00:05
# LastEditTime: 2020-02-20 09:21:10
# LastEditors: ssdcxy
# Description: 组合总和 III
# FilePath: /arithmetic_oj/LeetCode/P0216.py

import json

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(i, tmp_sum, tmp):
            if len(tmp) == k and tmp_sum == n:
                res.append(tmp)
                return 
            for j in range(i, 10):
                if len(tmp) > k or tmp_sum + j > n: break
                backtrack(j+1, tmp_sum + j, tmp + [j])
        res = []
        backtrack(1, 0, [])
        return res

def stringToInt(input):
    return int(input)

def int2dArrayToString(input):
    return json.dumps(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')
    lines = readlines()
    while True:
        try:
            line = lines.next()
            k = stringToInt(line)
            line = lines.next()
            n = stringToInt(line)
            
            ret = Solution().combinationSum3(k, n)

            out = int2dArrayToString(ret)
            print out
        except StopIteration:
            break

if __name__ == '__main__':
    main()