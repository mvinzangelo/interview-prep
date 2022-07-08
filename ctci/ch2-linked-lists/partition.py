# 2.4 Write code to partition a linked list around a value x, such that all nodes less than x come before all node greater than or equal to x.

from LinkedList import LinkedList
from LinkedList import LinkedListNode

# O(N) Time, O(1) Space
def partition(ll, x):
    if ll.head is None:
        return
    smaller_partition_head = smaller_partition_tail = None 
    larger_partition_head = larger_partition_tail = None 
    curr_node = ll.head
    while curr_node is not None:
        tmp_node = curr_node.next
        if curr_node.value >= x:
            if larger_partition_head is None:
                larger_partition_head = curr_node
                larger_partition_tail = curr_node
            else:
                larger_partition_tail.next = curr_node
                larger_partition_tail = curr_node
        else:
            if smaller_partition_head is None:
                smaller_partition_head = curr_node
                smaller_partition_tail = curr_node
            else:
                smaller_partition_tail.next = curr_node
                smaller_partition_tail = curr_node
        curr_node.next = None
        curr_node = tmp_node
    curr_node = smaller_partition_head
    smaller_partition_tail.next = larger_partition_head
    return smaller_partition_head

ll = LinkedList([2,1])
curr_node = partition(ll, 2)
while curr_node is not None:
    print(curr_node)
    curr_node = curr_node.next
