# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        stack = [(root, '')]
        total = 0
        while stack:
            n, b = stack.pop()
            num = b + str(n.val)
            if n.left:
                stack.append((n.left, num))
            if n.right:
                stack.append((n.right, num))
            if not n.left and not n.right:
                total += int(num, 2)
        return total
