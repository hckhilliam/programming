# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.i = 0
        self.parents = {}

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        if not preorder:
            return None

        t = TreeNode(preorder[0])
        if len(preorder) == 1:
            return t

        i = 1
        while i < len(preorder) and preorder[i] <= t.val:
            i += 1
        i -= 1

        t.left = self.bstFromPreorder(preorder[1:i + 1])
        t.right = self.bstFromPreorder(preorder[i + 1:])
        return t

    # This assumes BST is balanced, which it isn't -_-
    # def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
    #     if not preorder:
    #         return None

    #     t = TreeNode(preorder[0])
    #     if len(preorder) == 1:
    #         return t

    #     mid = ceil((len(preorder) - 1) / 2)
    #     if preorder[mid] > t.val:
    #         mid -= 1

    #     t.left = self.bstFromPreorder(preorder[1:mid + 1])
    #     t.right = self.bstFromPreorder(preorder[mid + 1:])
    #     return t
