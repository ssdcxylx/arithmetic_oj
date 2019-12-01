# coding = utf-8


class TreeNode:

    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def tree_height(tree):
    if tree is None:
        return 0

    left_tree_height = tree_height(tree.left)
    right_tree_height = tree_height(tree.right)

    return left_tree_height + 1 if left_tree_height > right_tree_height else right_tree_height + 1


if __name__ == "__main__":
    my_tree = TreeNode('D', TreeNode('B', TreeNode('A'), TreeNode('C')), TreeNode('E', right=TreeNode('G', TreeNode('F', right=TreeNode('H', TreeNode('I'))))))
    print(tree_height(my_tree))
