# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-30 08:59:56
# LastEditTime: 2020-03-30 09:10:18
# LastEditors: ssdcxy
# Description: 验证回文串
# FilePath: /arithmetic_oj/LeetCode/P0125.py

class Solution:
    def isPalindrome(self, s: str) -> bool:
        def not_letters_digits(c):
            return not ('A' <= c <= 'Z' or 'a' <= c <= 'z' or '0' <= c <= '9')
        if not s: return True
        left, right = 0, len(s)-1
        case = abs(ord('a')-ord('A'))
        while left < right:
            while left < right and not_letters_digits(s[left]):
                left += 1
            while left < right and not_letters_digits(s[right]):
                right -= 1
            s_l = ord(s[left]) - case if s[left] >= 'a' else ord(s[left])
            s_r = ord(s[right]) - case if s[right] >= 'a' else ord(s[right])
            if s_l != s_r: return False
            left += 1
            right -= 1
        return True
                
                
                

def stringToString(input):
    return input[1:-1].decode('string_escape')

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
            
            ret = Solution().isPalindrome(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()