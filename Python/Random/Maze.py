# coding = utf-8

import random


sx = 10
sy = 10
dfs = [[0 for col in range(sx)] for row in range(sy)]
maze = [[' ' for col in range(2 * sx + 1)] for row in range(2 * sy + 1)]
operations = {1: (0, -1), 2: (0, 1), 3: (-1, 0), 4: (1, 0)}
directions = [1, 2, 3, 4]
stack = []

for i in range(2 * sx + 1):
    if i % 2 == 0:
        for j in range(2 * sx + 1):
            maze[i][j] = '*'
for i in range(2 * sy + 1):
    if i % 2 == 0:
        for j in range(2 * sy + 1):
            maze[j][i] = '*'


def generate_maze(start):
    x, y = start
    dfs[y][x] = 1
    random.shuffle(directions)
    for direction in directions:
        px, py = (x + y for x, y in zip(start, operations[direction]))
        if px < 0 or px >= sx or py < 0 or py >= sy:  # 越界
            pass
        else:
            if dfs[py][px] is not 1:
                mx = 2 * x + 1
                my = 2 * y + 1
                if direction == 1:
                    maze[my - 1][mx] = ' '
                elif direction == 2:
                    maze[my + 1][mx] = ' '
                elif direction == 3:
                    maze[my][mx - 1] = ' '
                elif direction == 4:
                    maze[my][mx + 1] = ' '
                generate_maze((px, py))


if __name__ == "__main__":
    generate_maze((0, 0))
    for col in maze:
        for element in col:
            print(element, end=' ')
        print()
