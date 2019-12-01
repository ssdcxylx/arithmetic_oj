# coding = utf-8


class AToBDistance:

    def __init__(self, str1=None, str2=None, distance=0):
        self.str1 = str1
        self.str2 = str2
        self.distance = distance

    def get_distance_matrix(self):
        """
        利用动态规划的方式生成编辑距离矩阵
        :return:距离矩阵
        """
        str1_len = self.str1.__len__()
        str2_len = self.str2.__len__()

        chart = [[0 for col in range(str2_len + 1)]
                 for row in range(str1_len + 1)]  # 初始化矩阵，并将其值全部置为0

        for row in range(str1_len + 1):
            for col in range(str2_len + 1):
                if 0 == row and 0 == col:
                    chart[row][col] = 0
                elif 0 == col:
                    chart[row][col] = row
                elif 0 == row:
                    chart[row][col] = col
                else:
                    if self.str1[row - 1] == self.str2[col - 1]:
                        chart[row][col] = min(
                            chart[row - 1][col] + 1, chart[row][col - 1] + 1, chart[row - 1][col - 1])
                    else:
                        chart[row][col] = min(
                            chart[row - 1][col] + 1, chart[row][col - 1] + 1, chart[row - 1][col - 1] + 1)
        return chart


if __name__ == "__main__":
    a = "num"
    b = "name"
    my_distance = AToBDistance(a, b)
    matrix_chart = my_distance.get_distance_matrix()
    for index in matrix_chart:
        print(index)
    print("{}转换成{}的编辑距离为{}".format(a, b, matrix_chart[len(a)][len(b)]))
