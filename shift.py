class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoubleLinkedList:
    length = 0
    def __init__(self):
        self.head = None

    def add(self, data):
        if self.head is None:
            new_node = Node(data)
            new_node.prev = None
            self.head = new_node
        else:
            new_node = Node(data)
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current
            new_node.next = None
        self.length += 1


    def print_out(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next



class ShiftList(DoubleLinkedList):
    tail = Node(5)
    head = Node(4)
    length = 2
    tail.next = head
    head.prev = tail

    if length == 2:
        head.next =  tail


    def shiftright(self):
        self.




ring=ShiftList()
ring.add(55)
ring.add(11)
ring.add(4)
ring.add(41)
ring.shiftright()
ring.print_out()
# print(ring.length)
# print(ShiftList.tail.next.next.next.next.data)