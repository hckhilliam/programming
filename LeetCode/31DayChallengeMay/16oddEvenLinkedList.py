# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        odd = head
        if not odd:
            return odd
        even = head.next
        if not even:
            return odd

        oddT = head
        evenT = even
        while True:
            n = evenT.next
            if not n:
                break

            oddT.next = n
            oddT = n

            n = oddT.next
            if not n:
                break

            evenT.next = n
            evenT = n

        oddT.next = even
        evenT.next = None
        return odd
