# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-13 09:36:00
# LastEditTime: 2020-03-13 09:43:20
# LastEditors: ssdcxy
# Description: 多数元素
# FilePath: /arithmetic_oj/JianzhiOffer/169.py

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt = 0
        cur = nums[0]
        for num in nums:
            cur = num if cnt == 0 else cur
            cnt = cnt + (1 if num == cur else - 1)
        return cur

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
            
            ret = Solution().majorityElement(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()