# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from queue import Queue

class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        q = Queue()
        q.put((root, 0))
        dx = -1
        xp = None
        dy = -1
        yp = None

        if not root or root.val == x or root.val == y:
            return False

        while q:
            n, d = q.get()
            l = False
            if n.left:
                if n.left.val == x:
                    dx = d
                    l = True
                elif n.left.val == y:
                    dy = d
                    l = True
                if dx >= 0 and dy >= 0:
                    return dx == dy
                q.put((n.left, d + 1))
            if n.right:
                if n.right.val == x:
                    dx = d
                elif n.right.val == y:
                    dy = d
                if dx >= 0 and dy >= 0:
                    if l:
                        return False
                    return dx == dy
                q.put((n.right, d + 1))
        return False
