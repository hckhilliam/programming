# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        m = head
        d = head.next
        while d:
            m = m.next
            d = d.next
            if d:
                d = d.next
        return m
