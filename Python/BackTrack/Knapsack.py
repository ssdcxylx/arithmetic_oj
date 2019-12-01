# coding = utf-8


U = [0, 0, 0, 0]  # 物品
S = [2, 5, 4, 2]  # 物品体积
V = [6, 3, 5, 4]  # 物品价值
C = 10  # 背包容量
best = 0  # 最大价值


def check_element(i):
    """
    检查当前放置的物品是否符合要求
    """
    cs = 0
    for index in range(0, len(U)):
        if U[index] == 1:
            cs += S[index]
    if cs + S[i] <= C:
        return True
    else:
        return False


def get_next_place(i):
    """
    得到下一个放置物品
    """
    if i < len(U):
        return i + 1
    else:
        return -1


def back_track(i):
    """
    回溯主函数
    """
    global best
    if i < len(U):
        if check_element(i):
            U[i] = 1
            back_track(get_next_place(i))
        U[i] = 0
        back_track(get_next_place(i))
    elif i == len(U):
        cv = 0
        for index in range(0, len(U)):
            if U[index] == 1:
                cv += V[index]
        if cv > best:
            best = cv


def start():
    """
    开始放置
    """
    back_track(0)
    print(best)


if __name__ == "__main__":
    start()
