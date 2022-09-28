# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2021-01-12 21:18:39
# LastEditTime: 2021-01-12 21:19:12
# LastEditors: ssdcxy
# Description: 最后一个单词的长度
# FilePath: /arithmetic_oj/LeetCode/P0058.py

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s: return 0
        n = len(s)
        ans = 0
        for i in range(n):
            if s[i] == " ":
                continue
            if s[i] != " " and s[i-1] == " ":
                ans = 1
            else:
                ans += 1
        return ans

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
            
            ret = Solution().lengthOfLastWord(s)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()