# coding = utf-8


def check_element(sudoku, x, y, element):
    """
    检查每行每列每块是否有相同的元素
    :return:
    """
    # 判断元素所在行是否有相同的元素
    for col in sudoku[x]:
        if col == element:
            return False
    # 判断元素所在列是否有相同的元素
    for row in sudoku:
        if row[y] == element:
            return False
    # 判断元素所在块是否有相同的元素
    chunk_start_x, chunk_start_y = x//3*3, y//3*3
    chunk = []
    for row in range(chunk_start_x, chunk_start_x + 3):
        for col in range(chunk_start_y, chunk_start_y + 3):
            chunk.append(sudoku[row][col])
    if element in chunk:
        return False
    return True


def get_next_place(sudoku, x, y):
    """
    寻找下一个可用位置
    :return:
    """
    # 按列寻找
    for col in range(y+1, 9):
        if 0 == sudoku[x][col]:
            return x, col
    # 如果所在列找不到可用的位置
    for row in range(x+1, 9):
        for col in range(0, 9):
            if 0 == sudoku[row][col]:
                return row, col
    # 若找不到下一个位置则返回(-1, -1)
    return -1, -1


def back_tract(sudoku, x, y):
    """
    回溯
    :return:
    """
    if 0 == sudoku[x][y]:  # 从1到9依次尝试
        for i in range(1, 10):
            if check_element(sudoku, x, y, i):
                sudoku[x][y] = i  # 将符合条件的数字填入sudoku
                next_x, next_y = get_next_place(sudoku, x, y)
                if next_x >= 0 and next_y >= 0:  # 如果存在下一个位置
                    if back_tract(sudoku, next_x, next_y):
                        return True
                    else:  # 如果不满足条件则回溯
                        sudoku[x][y] = 0
                else:
                    return True


def start(sudoku):
    """
    开始位置
    :return:
    """
    if 0 == sudoku[0][0]:
        back_tract(sudoku, 0, 0)
    else:
        x, y = get_next_place(sudoku, 0, 0)
        back_tract(sudoku, x, y)


if __name__ == "__main__":
    ku = [[1, 0, 3, 0, 0, 0, 5, 0, 9],
          [0, 0, 2, 1, 0, 9, 4, 0, 0],
          [0, 0, 0, 7, 0, 4, 0, 0, 0],
          [3, 0, 0, 5, 0, 2, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 0, 5, 0],
          [7, 0, 0, 8, 0, 3, 0, 0, 4],
          [0, 0, 0, 4, 0, 1, 0, 0, 0],
          [0, 0, 9, 2, 0, 5, 8, 0, 0],
          [8, 0, 4, 0, 0, 0, 1, 0, 7]]
    start(ku)
    for all_col in ku:
        print(all_col)
