# -*- coding: utf-8 -*-
# @time       : 2019-10-11 13:42
# @author     : ssdcxy
# @email      : 18379190862@163.com
# @file       : MinimumEditDistance.py
# @description: 最小编辑距离


def minimum_edit_distance(a, b):
    n, m = len(a), len(b)
    dp = [[0 for i in range(m+1)]
          for j in range(n+1)]
    flags = [['-' for i in range(m+1)]
             for j in range(n+1)]
    # 初始化
    for i in range(1, n+1):
        dp[i][0] = i
    for i in range(1, m+1):
        dp[0][i] = i
    for i in range(1, n+1):
        for j in range(1, m+1):
            insertion = 1
            deletion = 1
            substitution = 2
            if a[i-1] == b[j-1]:
                substitution = 0
            inse = dp[i][j-1] + insertion
            subs = dp[i-1][j-1] + substitution
            dele = dp[i-1][j] + deletion
            _min = min(dele, inse, subs)
            dp[i][j] = _min
            # 设置标记
            flag = []
            if inse == _min:
                flag.append("⬅️")
            if subs == _min:
                flag.append("↙️")
            if dele == _min:
                flag.append("⬇️")
            flags[i][j] = flag
    return dp[n][m]


if __name__ == "__main__":
    a = "intention"
    b = "execution"
    print(minimum_edit_distance(a, b))
    print()
