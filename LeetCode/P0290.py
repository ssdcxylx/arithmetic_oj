# -*- coding:utf-8 -*-
# Author: ssdcxy
# Date: 2020-12-16 09:26:14
# LastEditTime: 2020-12-16 09:49:47
# LastEditors: ssdcxy
# Description: 单词规律
# FilePath: /arithmetic_oj/LeetCode/P0290.py

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        word2ch = dict()
        ch2word = dict()
        words = s.split()
        if len(pattern) != len(words):
            return False
        for ch, word in zip(pattern, words):
            if (ch in ch2word and ch2word[ch] != word) or (word in word2ch and word2ch[word] != ch):
                return False
            ch2word[ch] = word
            word2ch[word] = ch
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
            pattern = stringToString(line);
            line = next(lines)
            s = stringToString(line);
            
            ret = Solution().wordPattern(pattern, s)

            out = (ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()