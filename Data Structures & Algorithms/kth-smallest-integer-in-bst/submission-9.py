# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def bst(node):
            res=[]
            if not node:
                return []
            return bst(node.left) + [node.val] + bst(node.right)
        res=bst(root)
        return res[k-1]

