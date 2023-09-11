class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

new_node = Node('Hello')

next_node = Node('Howdy')

new_node.next = next_node

# print(new_node.next.data)

class LinkedList:
    def __init__(self):
        self.head = None

    def addAtStart(self, data):
        added_node = Node(data)
        added_node.next = self.head
        self.head = added_node

    def addAtEnd(self, data):
        added_node = Node(data)
        if self.head == None:
            self.head = added_node
        else:
          current_node = self.head
          while current_node.next:
            current_node = current_node.next
          current_node.next = added_node

    def removeFromStart(self):
        if self.head == None:
            print('The list is already empty')
            return
        else: 
            new_head = self.head.next
            self.head = new_head

    def removeFromEnd(self):
        if self.head == None:
            print('The list is already empty')
            return
        elif self.head.next == None:
            self.head = None
        elif self.head.next.next == None:
            self.head.next = None
        else:
            current_node = self.head
            while current_node.next.next:
                current_node = current_node.next
            # print('Removed', current_node.next.data, "from the list")
            current_node.next = None

    def printList(self):
        # print('self.head:', self.head.data)
        current_node = self.head
        while current_node:
            print(current_node.data)
            current_node = current_node.next

new_linked_list = LinkedList()

new_linked_list.head = new_node

# print(new_linked_list.head.data)

new_linked_list.addAtStart('Hej')

new_linked_list.addAtEnd('Hola')

new_linked_list.removeFromEnd()

