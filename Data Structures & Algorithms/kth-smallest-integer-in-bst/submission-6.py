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
                return
            left=bst(node.left)
            if left:
                for i in left:
                    res.append(i)
            res.append(node.val)
            right=bst(node.right)
            if right:
                for i in right:
                    res.append(i)
            return res
        res=bst(root)
        return res[k-1]

