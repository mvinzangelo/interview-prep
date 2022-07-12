#2.6 Implement a function to check if a linked list is a palindrome

from LinkedList import LinkedList

def palindrome(input_list):
    if input_list.head is None:
        return True
    length = 0
    curr_node = input_list.head
    while curr_node is not None:
        length += 1
        curr_node = curr_node.next
    half_len = int(length / 2)
    curr_node = input_list.head
    for i in range(half_len):
        curr_node = curr_node.next
    prev_node = curr_node
    curr_node = prev_node.next
    while curr_node is not None:
        next_node = curr_node.next
        curr_node.prev = prev_node
        prev_node = curr_node
        curr_node = next_node
    head_ptr = input_list.head
    tail_ptr = input_list.tail
    for i in range(half_len):
        print(head_ptr.value)
        print(tail_ptr.value)
        if head_ptr.value is not tail_ptr.value:
            return False
        head_ptr = head_ptr.next
        tail_ptr = tail_ptr.prev
    return True

ll = LinkedList([1,2,5]) 
print(palindrome(ll))
