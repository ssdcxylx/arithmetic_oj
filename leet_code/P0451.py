# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-08 23:24:31
# LastEditTime: 2019-12-10 20:28:11
# LastEditors: ssdcxy
# Description: 根据字符出现频率排序
# FilePath: /arithmetic_oj/LeetCode/P0451.py


class Solution:
    def frequencySort(self, s: str) -> str:
        import collections
        counter = collections.Counter(s)
        lst = sorted(counter.keys(), key=counter.get, reverse=True)
        res = ""
        for i in lst:
            res += i * counter.get(i)
        return res


def stringToString(input):
    return input[1:-1]


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
            s = stringToString(line)

            ret = Solution().frequencySort(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
