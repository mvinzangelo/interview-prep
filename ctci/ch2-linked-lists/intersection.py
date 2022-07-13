# 2.7 Given two singly linked lists, determine if the two lists intersect and return that node. If they don't, return null

# O(N + M) time, O(1) space
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
            return None
        node_a = headA
        node_b = headB
        len_a = 0
        len_b = 0
        while node_a is not None:
            len_a += 1
            node_a = node_a.next
        while node_b is not None:
            len_b += 1
            node_b = node_b.next
        if node_a is not node_b:
            return None
        node_a = headA
        node_b = headB
        diff_len = abs(len_a - len_b)
        if len_a > len_b:
            for i in range(diff_len):
                node_a = node_a.next
        elif len_b > len_a:
            for i in range(diff_len):
                node_b = node_b.next
        while node_a is not None and node_b is not None:
            if node_a is node_b:
                return node_a
            else:
                node_a = node_a.next
                node_b = node_b.next
