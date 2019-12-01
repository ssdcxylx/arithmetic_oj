# coding = utf-8

if __name__ == "__main__":
    num = 312
    length, count = 3, 1
    maxChart = [[0 for i in range(length + 1)]  # 初始化二维列表，并将其值全部置为0
             for j in range(length + 1)]
    divisionChart = [[0 for i in range(length + 1)]
         for j in range(length + 1)]

    for index in range(length, 0, -1):
        divisionChart[index][index] = num % 10
        num //= 10
    for index1 in range(2, length + 1):
        for index2 in range(index1 - 1, 0, -1):
            divisionChart[index2][index1] = divisionChart[index2][index1 - 1] * 10 + divisionChart[index1][index1]
    for index in range(1, length + 1):
        maxChart[index][0] = divisionChart[1][index]
    for index1 in range(1, count + 1):
        for index2 in range(index1 + 1, length + 1):
            for index3 in range(index1, index2):
                maxChart[index2][index1] = max(maxChart[index2][index1],
                                               maxChart[index3][index1 - 1] * divisionChart[index3 + 1][index2])
    print(maxChart[length][count])