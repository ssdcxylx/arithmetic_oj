# coding = utf-8


class HorseTraverse:
    width = height = 8
    # 马走日字，可以前进的方式
    nextSteps = [(2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2)]
    # 马可以选择走的步数
    stepSum = 8
    # 初始化棋盘
    chess = [[0 for col in range(8)] for row in range(8)]
    # 起点默认为(2,0)
    startPoint = (2, 0)

    def next_step_ok(self, point, index):
        next_point = (point[0] + self.nextSteps[index][0], point[1] + self.nextSteps[index][1])
        if 0 <= next_point[0] < self.width and 0 <= next_point[1] < self.height and self.chess[next_point[0]][
            next_point[1]] == 0:
            return True, next_point
        else:
            return False, point

    def traverse(self, point, step):
        if step > self.width * self.height:
            return True
        for index in range(self.stepSum):
            is_ok, next_point = self.next_step_ok(point, index)
            if is_ok:
                self.chess[next_point[0]][next_point[1]] = step
                result = self.traverse(next_point, step+1)
                if result:
                    return True
                else:
                    # 如果遍历失败则回溯
                    self.chess[next_point[0]][next_point[1]] = 0
        return False

    def horse_traverse(self):
        self.chess[self.startPoint[0]][self.startPoint[1]] = 1
        self.traverse(self.startPoint, 2)
        for index in range(self.width):
            print(self.chess[index])

if __name__ == "__main__":
    ht = HorseTraverse()
    ht.horse_traverse()
