# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        node = head
        s = set()
        while node is not None:
            
            if node.val not in s:
                s.add(node.val)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next
        return head
