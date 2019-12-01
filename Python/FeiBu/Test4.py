# -*-  coding:utf-8 -*-
count = 0


def main():
    global count
    (n, k) = (int(x) for x in raw_input().split())
    lst = list(map(int, raw_input().split()))
    for i in range(n):
        s = []
        for j in range(i, n):
            s.append(lst[j])
            s.sort()
            mid = int((len(s)+1)/2)-1
            if s[mid] == k:
                count += 1
    print count


if __name__ == '__main__':
    main()