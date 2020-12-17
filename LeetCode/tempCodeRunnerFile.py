from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        def dfs(node, level):
            if level >= len(res):
                res.append(deque([node.val]))
            else:
                if level % 2 == 0:
                    res[level].append(node.val)
                else:
                    res[level].appendleft(node.val)
            _tmp = level + 1
            if node.left: dfs(node.left, _tmp)
            if node.right: dfs(node.right, _tmp)
        if not root: return []
        res = []
        dfs(root, 0)
        return res