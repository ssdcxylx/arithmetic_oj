# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 08:38:38
# LastEditTime: 2020-03-19 17:01:24
# LastEditors: ssdcxy
# Description: 组合总和 II
# FilePath: /arithmetic_oj/LeetCode/P0040.py

import json
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, tmp_lst):
            nonlocal n, target
            if tmp_sum == target:
                res.append(tmp_lst)
                return
            for j in range(i, n):
                if sum(tmp_lst) + candidates[j] > target: break
                if j > i and candidates[j] == candidates[i]: continue
                backtrack(j, tmp_lst+[candidates[j]])
        candidates.sort()
        res = []
        n = len(candidates)
        backtrack(0, [])
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
            
            ret = Solution().combinationSum2(candidates, target)

            out = int2dArrayToString(ret)
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()