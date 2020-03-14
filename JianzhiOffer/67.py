# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-03-13 08:36:44
# LastEditTime: 2020-03-13 09:17:17
# LastEditors: ssdcxy
# Description: 把字符串转换成整数
# FilePath: /arithmetic_oj/JianzhiOffer/67.py

class Solution:
    def strToInt(self, s: str) -> int:
        return max(min(int(*re.findall('[\+\-]?\d+', s.lstrip())), 2**31), -2**31)
        

            

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
            a = stringToString(line);
            
            ret = Solution().strToInt(a)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()