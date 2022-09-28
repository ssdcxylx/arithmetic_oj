# -*-  coding:utf-8 -*-
count = 0


def main():
    global count
    (n, k) = (int(x) for x in raw_input().split())
    lst = list(map(int, raw_input().split()))
    max_sum = 0
    for i in range(n):
        sum = 0
        for j in range(i, n):
            sum += lst[j]
            if sum < k:
                count += 1
    print count


if __name__ == '__main__':
    main()