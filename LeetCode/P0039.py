# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 08:01:32
# LastEditTime: 2020-02-20 08:48:05
# LastEditors: ssdcxy
# Description: 组合总和
# FilePath: /arithmetic_oj/LeetCode/P0039.py

import json

class Solution(object):
    def combinationSum(self, candidates, target):
        def backtrack(i, tmp_sum, tmp):
            if tmp_sum > target or i == n:
                return
            if tmp_sum == target:
                res.append(tmp)
                return
            backtrack(i, tmp_sum+candidates[i], tmp+[candidates[i]])
            backtrack(i+1, tmp_sum, tmp)
        candidates.sort()
        n = len(candidates)
        res = []
        backtrack(0, 0, [])
        return res
            

def stringToIntegerList(input):
    return json.loads(input)

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
            line = next(lines)
            candidates = stringToIntegerList(line)
            line = next(lines)
            target = stringToInt(line)
            
            ret = Solution().combinationSum(candidates, target)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()