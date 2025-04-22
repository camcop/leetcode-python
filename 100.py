class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        if not p and not q:
            return True
        if not p or not q or p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# p = [1, 2, 3]
p = [2,2,2,None,2,None,None,2]
# q = [1, 2, 3]
q = [2,2,2,2,None,2,None]

from collections import deque

def build_tree(level_order):
    if not level_order or level_order[0] is None:
        return None
    it = iter(level_order)
    root = TreeNode(next(it))
    queue = deque([root])
    while queue:
        node = queue.popleft()
        try:
            left_val = next(it)
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
            right_val = next(it)
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
        except StopIteration:
            break
    return root

p_tree = build_tree(p)
q_tree = build_tree(q)


sol = Solution()
print(sol.isSameTree(p_tree, q_tree))