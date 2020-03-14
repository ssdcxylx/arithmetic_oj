# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-11 15:55:04
# LastEditTime: 2020-03-11 16:57:22
# LastEditors: ssdcxy
# Description: 最小的k个数
# FilePath: /arithmetic_oj/JianzhiOffer/40.py

import json
from typing import List

class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def sink(i):
            nonlocal n
            left = i * 2 + 1
            right = i * 2 + 2
            if left >= n: return
            min_i = left
            if right < n and arr[left] > arr[right]:
                min_i = right
            if arr[min_i] < arr[i]:
                arr[i], arr[min_i] = arr[min_i], arr[i]
                sink(min_i)
        def build_heap():
            nonlocal n
            for i in range(n//2, -1, -1):
                sink(i)
        n = len(arr)
        if k > n: return []
        build_heap()
        res = []
        for _ in range(k):
            arr[0], arr[-1] = arr[-1], arr[0]
            res.append(arr.pop())
            n -= 1
            sink(0)
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
            arr = stringToIntegerList(line);
            line = next(lines)
            k = int(line);
            
            ret = Solution().getLeastNumbers(arr, k)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()