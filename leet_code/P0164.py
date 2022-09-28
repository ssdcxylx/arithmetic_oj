# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-11-26 12:36:07
# LastEditTime: 2020-11-26 12:52:49
# LastEditors: ssdcxy
# Description: 最大间距
# FilePath: /arithmetic_oj/LeetCode/P0164.py

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 2: return 0
        mx, mn = max(nums), min(nums)

        bucket_len = max(1, (mx - mn) // (n - 1))
        bucket_size = ((mx - mn) // bucket_len) + 1
        bucket = [[] for _ in range(bucket_size)]
        for num in nums:
            bucket[(num - mn) // bucket_len].append(num)
        
        max_gap = 0
        prev_max = float("inf")
        for i in range(bucket_size):
            if bucket[i] and prev_max != float("inf"):
                max_gap = max(max_gap, min(bucket[i]) - prev_max)
            if bucket[i]:
                prev_max = max(bucket[i])
        return max_gap
            

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
            
            ret = Solution().maximumGap(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()