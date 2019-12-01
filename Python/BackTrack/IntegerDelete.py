# coding = utf -8

n_lst = [1, 7, 8, 5, 4, 3]
s = 4


def delete():
    for index in range(len(n_lst) - 1):
        if n_lst[index] > n_lst[index + 1]:
            n_lst.remove(n_lst[index])
            break
        else:
            if index == len(n_lst) - 2:
                n_lst.remove(n_lst[index] + 1)


if __name__ == "__main__":
    for element in range(s):
        delete()
    n = 0
    for i in range(len(n_lst)):
        n += n_lst[i] * 10 ** (len(n_lst) - i - 1)
    print(n)
