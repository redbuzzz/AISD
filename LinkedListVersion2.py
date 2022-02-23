class LinkedList:
    head = None
    length = 1

    class Node:
        def __init__(self, element, next_node = None):
            self.element = element
            self.next_node = next_node

    def append(self, element):
        if not self.head:
            self.head = self.Node(element)
            return element
        node = self.head
        self.length += 1

        while node.next_node:
            node = node.next_node
        node.next_node = self.Node(element)

    def out(self):
        node = self.head
        while node.next_node:
            print(node.element)
            node = node.next_node
        print(node.element)

    def get(self, index):
        i = 0
        node = self.head
        prev_node = self.head

        while i < index:
            prev_node = node
            node = node.next_node
            i += 1
        print(prev_node.element)

    def insert(self, element, index):
        i=0
        node = self.head
        prev_node = self.head

        while i<index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = self.Node(element, next_node=node)
        self.length += 1 #подсчет длины при вставки


    def delete(self, index):
        i=0
        node = self.head
        prev_node = self.head

        if index == 0:
            self.head = self.head.next_node

        while i<index:
            prev_node = node
            node = node.next_node
            i += 1

        prev_node.next_node = node.next_node
        del node




listik = LinkedList()

listik.append(50)
listik.insert(11, 1)
listik.append(241)
listik.append(2222)



listik.delete(0)
listik.out()

