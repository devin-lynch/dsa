class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.len = 0

    def addAtStart(self, data):
        added_node = Node(data)
        if self.head is None:
            self.head = added_node
            self.tail = added_node
            self.len += 1
        else: 
            self.head.prev = added_node
            added_node.next = self.head
            self.head = added_node
            self.len += 1

    def addAtEnd(self, data):
        added_node = Node(data)
        if self.tail is None:
            self.head = added_node
            self.tail = added_node
            self.len += 1
        else:
            self.tail.next = added_node
            added_node.prev = self.tail
            self.tail = added_node
            self.len += 1

    def removeFromStart(self):
        if self.head is None:
            print('The list is already empty')
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            new_head = self.head.next
            self.head = new_head
            self.head.prev = None

    def removeFromEnd(self):
        if self.head is None:
            print('The list is already empty')
            return
        elif self.head.next is None:
            self.head = None
            self.tail = None
        else:
            new_tail = self.tail.prev
            self.tail = new_tail
            self.tail.next = None

    def addAfterNode(self, data, node):
        if self.head is None:
            print('Data does not exist')
        else:
            current_node = self.head
            while current_node.data is not node:
                current_node = current_node.next
            new_node = Node(data)
            new_node.next = current_node.next
            new_node.prev = current_node
            current_node.next.prev = new_node
            current_node.next = new_node
            
                
    def printList(self):
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

doubly_linked_list = DoublyLinkedList()

doubly_linked_list.addAtEnd('End')

doubly_linked_list.addAtStart('Start')

doubly_linked_list.printList()
