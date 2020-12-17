# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-04 09:35:34
# LastEditTime: 2020-12-04 11:22:53
# LastEditors: ssdcxy
# Description: 分割数组为连续子序列
# FilePath: /arithmetic_oj/LeetCode/P0659.py

import json
from typing import List

class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        n = len(nums)
        if n < 3: return False
        counts = collections.Counter(nums)
        endCounts = collections.Counter()
        for num in nums:
            count = counts.get(num, 0)
            endCount = endCounts.get(num-1, 0)
            if count:
                if endCount:
                    counts[num] -= 1
                    endCounts[num-1] -= 1
                    endCounts[num] += 1
                else:
                    if counts.get(num+1, 0) and counts.get(num+2, 0):
                        counts[num] -= 1
                        counts[num+1] -= 1
                        counts[num+2] -= 1
                        endCounts[num+2] += 1
                    else:
                        return False
        return True
                
                

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
            
            ret = Solution().isPossible(nums)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()