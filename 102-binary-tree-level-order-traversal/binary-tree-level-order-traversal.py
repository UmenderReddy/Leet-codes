# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[List[int]]
        """
        ans=[]
        if root is None:
            return []
        q=[]
        q.append(root)
        while len(q)>0:
            temp=[]
            for i in range(len(q)):
                cnode=q.pop(0)
                if cnode.left:
                    q.append(cnode.left)
                if cnode.right:
                    q.append(cnode.right)
                temp.append(cnode.val)
            ans.append(temp)
        return ans