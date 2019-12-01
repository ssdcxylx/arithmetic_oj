# coding=utf-8


# Knuth提出的步长序列
def shell_sort(arr):
    length = len(arr)
    step_size = 1
    while step_size < length // 3:
        step_size = 3 * step_size + 1

    while step_size >= 1:
        for i in range(step_size, length):
            j = i
            tmp = arr[i]
            while j >= step_size and arr[j] < arr[j - step_size]:
                arr[j] = arr[j - step_size]
                arr[j - step_size] = tmp
                j -= step_size
        step_size //= 3

    for pos in range(length):
        print(arr[pos])
