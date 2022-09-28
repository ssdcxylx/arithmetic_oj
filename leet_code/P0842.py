# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-08 09:43:33
# LastEditTime: 2020-12-08 10:08:30
# LastEditors: ssdcxy
# Description: 将数组拆分成斐波那契序列
# FilePath: /arithmetic_oj/LeetCode/P0842.py

import json
from typing import List

class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        def backtrack(idx):
            if idx == n:
                return len(res) >= 3
            cur = 0
            for i in range(idx, n):
                if i > idx and S[idx] == "0":
                    break
                cur = cur * 10 + ord(S[i]) - ord("0")
                if cur > 2**31-1:
                    break
                if len(res) < 2 or cur == res[-1] + res[-2]:
                    res.append(cur)
                    if backtrack(i+1):
                        return True
                    res.pop()
                elif len(res) > 2 and cur > res[-1] + res[-2]:
                    break
            return False
        if not S: return []
        res = []
        n = len(S)
        backtrack(0)
        return res
    
def stringToString(input):
    return input[1:-1].decode('string_escape')

def integerListToString(nums, len_of_list=None):
    if not len_of_list:
        len_of_list = len(nums)
    return json.dumps(nums[:len_of_list])

def main():
    import sys
    import io
    def readlines():
        for line in io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8'):
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            S = stringToString(line);
            
            ret = Solution().splitIntoFibonacci(S)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()