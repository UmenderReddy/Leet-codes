# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans=[]
        if root is None:
            return []
        q=[]
        q.append(root)
        left_to_right=True
        while len(q)>0:
            temp=[]
            for i  in range(len(q)):
                cnode=q.pop(0)
                if cnode.left:
                    q.append(cnode.left)
                if cnode.right:
                    q.append(cnode.right)
                temp.append(cnode.val)
            if not left_to_right:
                temp.reverse()
            ans.append(temp)
            left_to_right=not left_to_right
        return ans