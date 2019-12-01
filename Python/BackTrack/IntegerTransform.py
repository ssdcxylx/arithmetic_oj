# coding = utf-8

min_count = 5


def check_element(count, num, father_num):
    if count >= 5:
        return False
    if num == 0:
        return False
    if father_num == num:
        return False
    return True


def get_next_place(flag, num):
    if 1 == flag:
        return num * 3
    else:
        return num // 2


def back_track(count, num, father_num, n):
    global min_count
    if check_element(count, num, father_num):
        count += 1
        for index in range(0, 2):
            next_num = get_next_place(index, num)
            if next_num == n:
                if count < min_count:
                    min_count = count
            else:
                back_track(count, next_num, num, n)


def start(m, n):
    global min_count
    if get_next_place(0, m) != n:
        back_track(1, get_next_place(0, m), m, n)
    else:
        min_count = 1
    if get_next_place(1, m) != n:
        back_track(1, get_next_place(1, m), m, n)
    else:
        min_count = 1

if __name__ == "__main__":
    start(15, 4)
    print(min_count)
