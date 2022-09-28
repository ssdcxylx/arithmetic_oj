# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 15:05:14
# LastEditTime: 2020-03-12 15:14:12
# LastEditors: ssdcxy
# Description: 扑克牌中的顺子
# FilePath: /arithmetic_oj/JianzhiOffer/61.py

import json

class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        flag = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] == 0:
                flag += 1
                continue
            if nums[i] == nums[i+1]:
                return False
            if nums[i] != nums[i+1] + 1:
                flag -= nums[i+1] - nums[i] - 1
        return flag >= 0
            

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
            
            ret = Solution().isStraight(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()