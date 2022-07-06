# 2.1 Write code to remove duplicates from an unsorted linked list. Follow up, what if a temporary buffer wasn't allowed?

from LinkedList import LinkedList

def removeDups(inputList):
    if inputList.head is None:
        return
    seen = set()
    currNode = inputList.head
    seen.add(currNode.value)
    while currNode.next is not None:
        if currNode.next.value in seen:
            deleteNextNode(inputList, currNode)
        else:
            seen.add(currNode.next.value)
            currNode = currNode.next
    return inputList

def deleteNextNode(inputList, node):
    if inputList.head is None:
        return inputList
    elif node is inputList.head:
        inputList.head = None
    elif node.next is inputList.tail:
        node.next = None
        inputList.tail = node
    else:
        node.next = node.next.next
    return inputList
        


testList = LinkedList()
testList.generate(100,0,9)
#testList = LinkedList([1,2,3,2,2,3,4,4,4])
print(removeDups(testList))
