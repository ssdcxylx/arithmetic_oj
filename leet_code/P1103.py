# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-05 09:01:35
# LastEditTime: 2020-03-05 09:29:59
# LastEditors: ssdcxy
# Description: 分糖果 II
# FilePath: /arithmetic_oj/LeetCode/P1103.py

import json
from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        res = [0 for _ in range(num_people)]
        count = 0
        a, b = 1, num_people
        _sum = (a+b)*num_people//2
        while candies > _sum:
            count += 1
            candies -= _sum
            a, b = a+num_people, b+num_people
            _sum = (a+b)*num_people//2
        for i in range(num_people):
            base = num_people*count
            res[i] = ((i+1)+(base-num_people+i+1))*count//2
            cur = base + i + 1 
            if candies > cur:
                res[i] += cur
                candies -= cur
            else:
                res[i] += candies
                candies = 0
        return res
            
            

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
            candies = int(line);
            line = next(lines)
            num_people = int(line);
            
            ret = Solution().distributeCandies(candies, num_people)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()