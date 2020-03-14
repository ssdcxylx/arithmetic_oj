# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-10 11:13:43
# LastEditTime: 2020-03-10 11:44:21
# LastEditors: ssdcxy
# Description: 表示数值的字符串
# FilePath: /arithmetic_oj/JianzhiOffer/20.py

class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        digit_flag = e_flag = dot_flag = False
        for i, c in enumerate(s):
            if c in ("+", "-"):
                if i > 0 and s[i-1] not in ("E", "e"):
                    return False
            elif c == ".":
                if dot_flag or e_flag:
                    return False
                dot_flag = True
            elif c in ("E", "e"):
                if e_flag or (not digit_flag):
                    return False
                e_flag = True
                digit_flag = False
            elif c in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9"):
                digit_flag = True
            else:
                return False
        return digit_flag


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
            
            ret = Solution().isNumber(s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()