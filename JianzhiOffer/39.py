# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 15:44:51
# LastEditTime: 2020-12-04 11:59:17
# LastEditors: ssdcxy
# Description: 数组中出现次数超过一半的数字
# FilePath: /arithmetic_oj/JianzhiOffer/39.py

import json
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # votes = 0
        # for num in nums:
        #     if not votes: cur = num
        #     votes += 1 if cur == num else -1
        # return cur
        def get_mid(left, right):
            low, high = left, right
            pivot = nums[left]
            while left < right:
                while left < right and nums[right] > pivot:
                    right -= 1
                nums[left] = nums[right]
                while left < right and nums[left] <= pivot:
                    left += 1
                nums[right] = nums[left]
            nums[right] = pivot
            if right == mid:
                return pivot
            elif right > mid:
                if low < right - 1 and nums[right-1] == pivot:
                    right -= 1
                    if right == mid:
                        return pivot
                return get_mid(low, right-1)
            else:
                if high > right + 1 and nums[right+1] == pivot:
                    right += 1
                    if right == mid:
                        return pivot
                return get_mid(right+1, high)
        n = len(nums)
        mid = n // 2
        return get_mid(0, n-1)

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