# 2.2 Implement an algorithm to find the kth to last element of a singly linked list

from LinkedList import LinkedList

def returnKthToLast(ll, k):
    if ll.head is None:
        return
    aheadNode = ll.head
    behindNode = ll.head
    for i in range(k + 1):
        if aheadNode is None:
            return
        aheadNode = aheadNode.next
    while aheadNode is not None:
        aheadNode = aheadNode.next
        behindNode = behindNode.next
    return behindNode

testList = LinkedList([1,2,3,4,5])
print(returnKthToLast(testList, 0))
