# Last updated: 7/11/2025, 5:01:32 PM
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        dq = deque([root])
        res = []

        if not root:
            return []

        level = 0
        while dq:
            q_len = len(dq)
            res.append(0)
            for i in range(q_len):
                r = dq.popleft()
                if r.left:
                    dq.append(r.left)
                if r.right:
                    dq.append(r.right)
                res[level] = r.val
            level += 1
        return res
                

        