# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 21:48:14
# LastEditTime: 2019-12-10 20:25:32
# LastEditors: ssdcxy
# Description: 反转字符串中的元音字母
# FilePath: /arithmetic_oj/LeetCode/P0345.py


class Solution:
    def swap(self, s: str, i: int, j: int) -> str:
        low = s[0:i] if i > 0 else ''
        mid = s[i + 1:j] if j > i + 1 else ''
        high = s[j + 1:] if j + 1 < len(s) else ''
        return low + s[j] + mid + s[i] + high

    def reverseVowels(self, s: str) -> str:
        yy = ['a', 'e', 'i', 'o', 'u', "A", "E", "I", "O", "U"]
        low, high = 0, len(s) - 1
        while low < high:
            while low <= high and s[low] not in yy:
                low += 1
            while low <= high and s[high] not in yy:
                high -= 1
            if low < high and s[low] != s[high]:
                s = self.swap(s, low, high)
            low += 1
            high -= 1
        return s


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

            ret = Solution().reverseVowels(s)

            out = (ret)
            print(out)
        except StopIteration:
            break


if __name__ == '__main__':
    main()
