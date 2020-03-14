# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-03 10:25:07
# LastEditTime: 2020-03-03 10:29:51
# LastEditors: ssdcxy
# Description: 存在重复元素
# FilePath: /arithmetic_oj/LeetCode/P0217.py

from typing import List
import json

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        _set = set()
        for num in nums:
            if _set.__contains__(num):
                return True
            _set.add(num)
        return False
        

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
            
            ret = Solution().containsDuplicate(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()