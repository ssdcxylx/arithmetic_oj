# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-12 14:09:17
# LastEditTime: 2020-12-13 21:31:01
# LastEditors: ssdcxy
# Description: 滑动窗口的最大值
# FilePath: /arithmetic_oj/JianzhiOffer/59-1.py

import json
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import collections
        if not nums: return []
        n = len(nums)
        q = collections.deque()
        for i in range(k):
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
        res = [nums[q[0]]]
        for i in range(k, n):
            if q[0] <= i - k:
                q.popleft()
            while q and nums[q[-1]] < nums[i]:
                q.pop()
            q.append(i)
            res.append(nums[q[0]])
        return res
        
            
        

def stringToIntegerList(input):
    return json.loads(input)

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
            nums = stringToIntegerList(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().maxSlidingWindow(nums, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()