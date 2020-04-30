# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.m = {}

    def maxPathSum(self, root: TreeNode) -> int:
        self.setSums(root)

        mm = None
        for k in self.m:
            d = k.val
            if k.left and self.m[k.left] > 0:
                d += self.m[k.left]
            if k.right and self.m[k.right] > 0:
                d += self.m[k.right]
            mm = max(mm, d) if mm else d
        return mm

    def setSums(self, r):
        if not r:
            return 0

        self.m[r] = r.val
        mC = max(self.setSums(r.left), self.setSums(r.right))
        if mC > 0:
            self.m[r] += mC

        return self.m[r]
