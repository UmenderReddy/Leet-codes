# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans=[]
        if root is None:
            return ans
        q=[]
        q.append(root)
        while len(q)>0:
            temp=[]
            for i in range(len(q)):
                curr_node=q.pop(0)
                if curr_node.left:
                    q.append(curr_node.left)
                if curr_node.right:
                    q.append(curr_node.right)
                temp.append(curr_node.val)
            ans.append(temp)
        return ans