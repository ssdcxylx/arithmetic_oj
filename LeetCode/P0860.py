# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-17 13:22:53
# LastEditTime: 2020-12-17 13:23:02
# LastEditors: ssdcxy
# Description: 柠檬水找零
# FilePath: /arithmetic_oj/LeetCode/P0860.py

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five, ten = 0, 0
        for bill in bills:
            if bill == 10:
                if not five: return False
                five -= 1
                ten += 1
            elif bill == 20:
                if not five: return False
                if ten:
                    ten -= 1
                    five -= 1
                else:
                    if five < 3: return False
                    five -= 3
            else:
                five += 1
        return True

def stringToIntegerList(input):
    return json.loads(input)

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
            bills = stringToIntegerList(line);
            
            ret = Solution().lemonadeChange(bills)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()