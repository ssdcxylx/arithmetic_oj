# -*- coding: utf-8 -*-
# @time       : 7/12/2019 10:35 下午
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @description: 


class Solution:
    def validPalindrome(self, s: str) -> bool:
        low, high = 0, len(s) - 1
        flag = True
        while low <= high:
            if s[low] == s[high]:
                low += 1
                high -= 1
            else:
                if flag:
                    if low < high and s[low+1] == s[high]:
                        low += 2
                        high -= 1
                    if low < high and s[low] == s[high-1]:
                        low += 1
                        high -= 2
                    flag = False
                else:
                    return False
        return True


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
            s = stringToString(line);

            ret = Solution().validPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break
