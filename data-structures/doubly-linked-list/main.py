class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

new_node = Node('Luffy')

new_node.next = Node('Sanji')

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def addAtStart(self, data):
        added_node = Node(data)
        if self.head == None:
            self.head = added_node
        else: 
            self.head.prev = added_node
            added_node.next = self.head
            self.head = added_node

    def addAtEnd(self, data):
        added_node = Node(data)
        if self.head == None:
            self.head = added_node
            self.tail = added_node
        else:
          pass

    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

doubly_linked_list = doublyLinkedList()

doubly_linked_list.head = new_node

doubly_linked_list.addAtStart('Nami')

doubly_linked_list.addAtEnd('Zoro')

doubly_linked_list.printList()