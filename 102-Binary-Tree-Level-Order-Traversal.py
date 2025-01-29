# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        if not root :
            return res
        q = collections.deque()
        q.append(root)
        while q :
            same_level = []
            
            for i in range(len(q)) :
                n = q.popleft()
                same_level.append(n.val)
                if n.left :
                    q.append(n.left)
                if n.right :
                    q.append(n.right)
            res.append(same_level)
        
        return res


        