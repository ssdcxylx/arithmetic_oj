# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-13 08:27:05
# LastEditTime: 2020-03-13 08:36:07
# LastEditors: ssdcxy
# Description: 构建乘积数组
# FilePath: /arithmetic_oj/JianzhiOffer/66.py

class Solution:
    def constructArr(self, a: List[int]) -> List[int]:
        n = len(a)
        res = [1] * n
        pos = 0
        left = right = 1
        while pos < n:
            res[pos] *= left
            res[n-pos-1] *= right
            left *= a[pos]
            right *= a[n-pos-1]
            pos += 1
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
            a = stringToIntegerList(line);
            
            ret = Solution().constructArr(a)

            out = integerListToString(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()