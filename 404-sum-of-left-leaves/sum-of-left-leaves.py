# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode | None) -> int:
        sum=0
        if root is None:
            return sum
        if root.left is not None:
            if root.left.left is None and root.left.right is None:
                sum+=root.left.val
            else:
                sum+=self.sumOfLeftLeaves(root.left)
        sum+=self.sumOfLeftLeaves(root.right)
        return sum