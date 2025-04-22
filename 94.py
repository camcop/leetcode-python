# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[int]
        """
        
        traversed = []
        output = []
        node = root

        while node or traversed:
            while node:
                traversed.append(node)
                node = node.left
            node = traversed.pop()
            output.append(node.val)
            node = node.right

        return output

