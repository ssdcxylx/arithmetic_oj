# -*- coding:utf-8 -*_
import sys


class TreeNode:
    def __init__(self, value=None, left=None, right=None):
        self.left = left
        self.right = right
        self.value = value


def post_order(root, str1, str2):
    if len(str1) > 0:
        root.value = str1[0]
        root_index = str2.index(root.value)
        if root_index >= 0 and len(str2[0:root_index]) != 0:
            root.left = TreeNode()
            post_order(root.left, str1[1:root_index+1], str2[0:root_index])
        if root_index < len(str2) and len(str2[root_index+1:len(str2)]) != 0:
            root.right = TreeNode()
            post_order(root.right, str1[root_index+1:len(str1)], str2[root_index+1:len(str2)])


def post_travel(root):
    if root.left is not None:
        post_travel(root.left)
    if root.right is not None:
        post_travel(root.right)
    # 输出无空格无换行
    sys.stdout.write(str(root.value))


def main():
    str1 = raw_input()
    str2 = raw_input()
    root = TreeNode(str1[0])
    root_index = str2.index(root.value)
    if root_index > 0 and len(str2[0:root_index]) != 0:
        root.left = TreeNode()
        post_order(root.left, str1[1:root_index + 1], str2[0:root_index])
    if root_index < len(str2) and len(str2[root_index+1:len(str2)]) != 0:
        root.right = TreeNode()
        post_order(root.right, str1[root_index + 1:len(str1)], str2[root_index + 1:len(str2)])
    post_travel(root)


if __name__ == '__main__':
    main()