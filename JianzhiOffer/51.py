# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 09:20:43
# LastEditTime: 2020-03-12 10:13:36
# LastEditors: ssdcxy
# Description: 数组中的逆序对
# FilePath: /arithmetic_oj/JianzhiOffer/51.py

import json
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge(start, mid, end):
            nonlocal cnt
            tmp = []
            i, j = start, mid+1
            while i <= mid and j <= end:
                if nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                else:
                    cnt += mid - i + 1
                    tmp.append(nums[j])
                    j += 1
            while i <= mid:
                tmp.append(nums[i])
                i += 1
            while j <= mid:
                tmp.append(nums[j])
                j += 1
            for i in range(len(tmp)):
                nums[start+i] = tmp[i]
        def mergeSort(start, end):
            if start >= end: return
            mid = (start + end) >> 1
            mergeSort(start, mid)
            mergeSort(mid+1, end)
            merge(start, mid, end)
        cnt = 0
        mergeSort(0, len(nums)-1)
        return cnt
            

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