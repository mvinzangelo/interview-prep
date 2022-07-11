# 2.5 You have two numbers represented by a linked list, where each node contains a single digit. The digits are stored in reverse order, such that the 1's digit is a the head of the list. Write a function that adds the two numbers and returns the sum as a linked list.

from LinkedList import LinkedList
import math

def sumLists(left, right):
    if left is None and right is None:
        return None
    if left is None:
        return right
    elif right is None:
        return left
    left_node = left.head
    right_node = right.head
    left_value = left_node.value 
    right_value = right_node.value 
    sum_list = LinkedList()
    curr_sum = 0
    curr_carry = 0
    while left_node is not None or right_node is not None:
        if left_node is not None:
            left_value = left_node.value
        if right_node is not None:
            right_value = right_node.value
        curr_sum = left_value + right_value + curr_carry
        if curr_sum > 9:
            curr_carry = math.floor(curr_sum / 10)
            curr_sum = curr_sum % 10
        else:
            curr_carry = 0
        sum_list.add(curr_sum)
        if left_node is not None:
            left_node = left_node.next
        if right_node is not None:
            right_node = right_node.next
        left_value = right_value = 0
    return sum_list

left = LinkedList([7])
right = LinkedList([5,9,2])
print(sumLists(left, right))

    
    
