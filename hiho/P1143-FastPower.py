# -*- coding:utf-8 -*-


MOD = 19999997


def mult(mat1, mat2):
    global MOD
    res = [
        [0 for i in range(2)]
        for j in range(2)
    ]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                res[i][j] += (mat1[i][k]*mat2[k][j]) % MOD
            res[i][j] %= MOD
    return res


def main():
    N = input()
    n = N + 1
    base = [[0, 1], [1, 1]]
    ans = [[1, 0], [0, 1]]
    while n != 0:
        if (n & 1) != 0:
            ans = mult(ans, base)
        base = mult(base, base)
        n >>= 1
    print ans[0][1] % MOD


if __name__ == '__main__':
    main()