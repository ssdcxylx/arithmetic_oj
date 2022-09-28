# -*- coding:utf-8-*-


def main():
    (n, m) = (int(x) for x in raw_input().split())
    my_map = []
    pos = []
    for i in range(n):
        my_map.append(list(raw_input()))
    for i in range(0, 3):
        pos.append(list(raw_input()))
    pos_str = ''
    for i in range(0, 3):
        for j in range(0, 3):
            pos_str += pos[i][j]
    for i in range(1, n-1):
        for j in range(1, m-1):
            map_str = my_map[i-1][j-1] + my_map[i-1][j] + my_map[i-1][j+1] + my_map[i][j-1] + my_map[i][j] + my_map[i][j+1] + my_map[i+1][j-1] + my_map[i+1][j] + my_map[i+1][j+1]
            if map_str == pos_str:
                print('{0} {1}'.format(i+1, j+1))
            else:
                map_str = my_map[i + 1][j - 1] + my_map[i][j-1] + my_map[i - 1][j-1] + my_map[i+1][j] + my_map[i][j] + my_map[i-1][j] + my_map[i + 1][j + 1] + my_map[i][j+1] + my_map[i-1][j + 1]
                if map_str == pos_str:
                    print('{0} {1}'.format(i+1, j+1))
                else:
                    map_str = my_map[i+1][j+1] + my_map[i+1][j] + my_map[i+1][j-1] + my_map[i][j+1] + my_map[i][j] + my_map[i][j-1] + my_map[i-1][j+1] + my_map[i-1][j] + my_map[i-1][j-1]
                    if map_str == pos_str:
                        print('{0} {1}'.format(i+1, j+1))
                    else:
                        map_str = my_map[i-1][j+1] + my_map[i][j+1] + my_map[i+1][j+1] + my_map[i-1][j] + my_map[i][j] + my_map[i+1][j] + my_map[i-1][j-1] + my_map[i][j-1] + my_map[i+1][j - 1]
                        if map_str == pos_str:
                            print('{0} {1}'.format(i+1, j+1))


if __name__ == '__main__':
    main()