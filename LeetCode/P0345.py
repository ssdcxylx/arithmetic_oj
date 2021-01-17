# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2019-12-07 21:48:14
# LastEditTime: 2020-12-22 10:01:33
# LastEditors: ssdcxy
# Description: 反转字符串中的元音字母
# FilePath: /arithmetic_oj/LeetCode/P0345.py


class Solution:

    def reverseVowels(self, s: str) -> str:
        if not s: return s
        vowels = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        left, right = 0, len(s)-1
        s = list(s)
        while left < right:
            if s[left] in vowels:
                if s[right] in vowels:
                    s[left], s[right] = s[right], s[left]
                    left += 1
                right -= 1
            else:
                if s[right] not in vowels:
                    right -= 1
                left += 1 
        return ''.join(s)


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
