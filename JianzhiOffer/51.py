# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 09:20:43
# LastEditTime: 2020-12-08 11:12:53
# LastEditors: ssdcxy
# Description: 数组中的逆序对
# FilePath: /arithmetic_oj/JianzhiOffer/51.py

import json
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(start, mid, end):
            nonlocal count
            left = start
            right = mid + 1
            tmp = []
            while left <= mid and right <= end:
                if nums[left] <= nums[right]:
                    tmp.append(nums[left])
                    left += 1
                else:
                    count += mid - left + 1
                    tmp.append(nums[right])
                    right += 1
            if left <= mid:
                tmp.extend(nums[left:mid+1])
            if right <= end:
                tmp.extend(nums[right:end+1])
            nums[start:start+len(tmp)] = tmp[:]
        def mergeSort(start, end):
            if start >= end: return
            mid = start + ((end - start) >> 1)
            print(mid)
            mergeSort(start, mid)
            mergeSort(mid+1, end)
            merge(start, mid, end)
        if not nums : return 0
        n = len(nums)
        count = 0
        mergeSort(0, n-1)
        return count
            

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
            
            ret = Solution().reversePairs(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()