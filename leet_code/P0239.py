# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-02 09:19:13
# LastEditTime: 2021-01-02 09:19:32
# LastEditors: ssdcxy
# Description: 滑动窗口最大值
# FilePath: /arithmetic_oj/LeetCode/P0239.py

import json
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums: return []
        if not k: return []
        n = len(nums)
        if k >= n: return [max(nums)]
        import collections
        deque = collections.deque()
        for i in range(k):
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
        res = [nums[deque[0]]]
        for i in range(k, n):
            if deque[0] == i-k:
                deque.popleft()
            while deque and nums[deque[-1]] < nums[i]:
                deque.pop()
            deque.append(i)
            res.append(nums[deque[0]])
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