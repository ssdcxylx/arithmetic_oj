import sys
import math
m = int(sys.stdin.readline().strip())
for i in range(m):
    n = int(sys.stdin.readline().strip())
    lst_a = [[]] * n
    for j in range(n):
       lst_a[j] = list(map(int, sys.stdin.readline().strip().split()))
    lst_b = [[]] * n
    for j in range(n):
        lst_b[j] = list(map(int, sys.stdin.readline().strip().split()))
        if lst_b[j] in lst_a:
            flag = True
    if flag:
        print(0.000)
    else:
        _min = float('inf')
        for j in range(n):
            for k in range(n):
                dis = math.sqrt(math.pow(lst_a[j][0] - lst_b[k][0], 2) + math.pow(lst_a[j][1] - lst_b[k][1], 2))
                if dis < _min:
                    _min = dis
        print("%.3f"%_min)