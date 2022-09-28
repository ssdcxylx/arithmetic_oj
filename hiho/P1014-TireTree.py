# -*- coding:utf-8 -*-


class TireTreeNode:
    def __init__(self, kids, count=0, val=None):
        self.kids = kids
        self.count = count
        self.val = val


def main():
    t = int(raw_input())
    head = TireTreeNode([])
    while t > 0:
        tire_tree = head
        lst = list(raw_input())
        for x in lst:
            if len(tire_tree.kids) == 0:
                tire_tree.count += 1
                new_kid = TireTreeNode([], 0, x)
                tire_tree.kids.append(new_kid)
                tire_tree = new_kid
            else:
                for i in range(0, len(tire_tree.kids)):
                    if tire_tree.kids[i].val == x:
                        tire_tree.count += 1
                        tire_tree = tire_tree.kids[i]
                        break
                    else:
                        if i == len(tire_tree.kids) - 1:
                            tire_tree.count += 1
                            new_kid = TireTreeNode([], 0, x)
                            tire_tree.kids.append(new_kid)
                            tire_tree = new_kid
                            break
                        else:
                            continue
        tire_tree.count += 1
        t -= 1
    t = int(raw_input())
    while t > 0:
        tire_tree = head
        lst = list(raw_input())
        for x in lst:
            if len(tire_tree.kids) == 0:
                tire_tree = TireTreeNode([], 0, x)
            else:
                for i in range(0, len(tire_tree.kids)):
                    if tire_tree.kids[i].val == x:
                        tire_tree = tire_tree.kids[i]
                        break
                    else:
                        if i == len(tire_tree.kids) - 1:
                            tire_tree = TireTreeNode([], 0, x)
                            break
                        else:
                            continue
        print tire_tree.count
        t -= 1


if __name__ == '__main__':
    main()