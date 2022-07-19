# 3.6 An animal shelter, which holds only dogs and cats, operates on a strictly "fifo" basis. People must adopt either the "oldest" (based on the arrival time) of all animals at the shelter). They cannot select which specific animal they would like. Create the data structures to maintain this system and implement. You may use the built-in LinkedList data structure.

from LinkedList import LinkedList

class AnimalShelter():
    def __init__(self):
        self.queue = LinkedList()
    
    def enqueue(self, animal):
        self.queue.add(animal)

    def dequeueAny(self):
        if not self.queue.head:
            return None
        elif  not self.queue.head.next:
            self.queue.head = None
        else:
            self.queue.head = self.queue.head.next
        return

    def dequeueDog(self):
        curr_node = self.queue.head
        if not curr_node:
            return None
        elif curr_node.value == 0:
            return_node = curr_node
            self.queue.head = curr_node.next 
            return return_node
        else:
            while curr_node.next:
                if curr_node.next.value == 0:
                    return_node = curr_node.next
                    if curr_node.next is self.queue.tail:
                        self.queue.tail = curr_node
                    curr_node.next = curr_node.next.next
                    return return_node
                curr_node = curr_node.next
        return None

    def dequeueCat(self):
        curr_node = self.queue.head
        if not curr_node:
            return None
        elif curr_node.value == 1:
            return_node = curr_node
            self.queue.head = curr_node.next 
            return return_node
        else:
            while curr_node.next:
                if curr_node.next.value == 1:
                    return_node = curr_node.next
                    if curr_node.next is self.queue.tail:
                        self.queue.tail = curr_node
                    curr_node.next = curr_node.next.next
                    return return_node
                curr_node = curr_node.next
        return None

madra = AnimalShelter()
madra.enqueue(1)
madra.enqueue(0)
madra.enqueue(0)
madra.enqueue(0)
madra.enqueue(1)
print(madra.queue)
madra.dequeueDog()
print(madra.queue)
