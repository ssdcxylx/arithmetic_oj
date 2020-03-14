# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 10:47:44
# LastEditTime: 2020-03-03 11:11:30
# LastEditors: ssdcxy
# Description: 最长连续序列
# FilePath: /arithmetic_oj/LeetCode/P0128.py

from typing import List
import json

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        def forward(num):
            nonlocal _dict
            if not _dict.__contains__(num):
                return 0 
            cnt = _dict.get(num, 0)
            if cnt > 1:
                return cnt
            cnt = forward(num+1) + 1
            _dict[num] = cnt
            return cnt
        _dict = dict()
        for num in nums:
            _dict[num] = 1
        for num in nums:
            forward(num)
        return max(_dict.values())
       


def stringToIntegerList(input):
    return json.loads(input)

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
            nums = stringToIntegerList(line);
            
            ret = Solution().longestConsecutive(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()