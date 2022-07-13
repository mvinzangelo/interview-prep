# 2.8 Given a linked list which might contain a loop, implement an algorithm that returns the node at the beginning of the loop (if one exists)

# O(N) Time, O(1) Space
class Solution(object):
    def detectCycle(self, head):
        if head is None:
            return None
        slow = head
        fast = head
        while slow is not None:
            slow = slow.next
            if fast.next is None:
                return None
            elif fast.next.next is None:
                return None
            fast = fast.next.next
            if fast is slow:
                break
        if slow is None:
            return None
        fast = head
        while fast is not slow:
            fast = fast.next
            slow = slow.next
        return fast
