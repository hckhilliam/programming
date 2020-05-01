# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.walk(root, arr, 0)

    def walk(self, r, arr, i):
        if i >= len(arr) or not r or r.val != arr[i]:
            return False

        if i == len(arr) - 1 and not r.left and not r.right:
            return True

        return self.walk(r.left, arr, i + 1) or self.walk(r.right, arr, i + 1)
