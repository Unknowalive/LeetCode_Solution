# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k):
        # Helper function to check if there are at least k nodes left
        def has_k_nodes(curr, k):
            count = 0
            while curr and count < k:
                curr = curr.next
                count += 1
            return count == k

        # Helper function to reverse k nodes
        def reverse_k_nodes(curr, k):
            prev = None
            while k > 0:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
                k -= 1
            return prev

        dummy = ListNode(0)
        dummy.next = head
        group_prev = dummy

        while has_k_nodes(group_prev.next, k):
            group_start = group_prev.next
            group_end = group_start
            for _ in range(k - 1):
                group_end = group_end.next

            next_group = group_end.next
            new_start = reverse_k_nodes(group_start, k)

            group_prev.next = new_start
            group_start.next = next_group
            group_prev = group_start

        return dummy.next
