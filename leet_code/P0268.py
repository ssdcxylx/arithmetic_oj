# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 11:22:04
# LastEditTime: 2020-03-05 11:24:14
# LastEditors: ssdcxy
# Description: 缺失数字
# FilePath: /arithmetic_oj/LeetCode/P0268.py

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            res = res ^ i ^ nums[i]
        return res ^ n 

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
            
            ret = Solution().missingNumber(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()