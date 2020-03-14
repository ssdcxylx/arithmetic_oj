# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-02-20 08:38:38
# LastEditTime: 2020-02-20 08:53:57
# LastEditors: ssdcxy
# Description: 组合总和 II
# FilePath: /arithmetic_oj/LeetCode/P0040.py

import json
from typing import List

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        def backtrack(i, tmp_sum, tmp):
            if tmp_sum == target:
                if tmp not in res:
                    res.append(tmp)
                return
            for j in range(i, n):
                if tmp_sum + candidates[j] > target: break
                if j > i and candidates[j] == candidates[j-1]: continue
                backtrack(j+1, tmp_sum+candidates[j], tmp_sum+[candidates[j]])
        candidates.sort()
        n = len(candidates)
        res = []
        backtrack(0, 0, [], [])
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