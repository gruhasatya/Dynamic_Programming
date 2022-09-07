class node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class double_linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def last(self, data):
        new_node = node(data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        last = self.head
        while last.next is not None:
            last = last.next
        last.next = new_node
        new_node.prev = last

    def traverse(self, node):
        while node is not None:
            print(node.data)
            node = node.prev

    def delete(self, node, key):
        if node is None:
            return
        if node.data == key:
            self.head = node.next
            node = None
            return
        while node is not None:
            if node.data == key:
                break
            prev = node
            node = node.next
        if node is None:
            return
        prev.next = node.next
        node = None

    def reverse_linkedlist(self):
        temp1 = self.head
        temp2 = self.head
        while temp2.next:
          temp2  = temp2.next
        while temp1 != temp2:
            temp1.data, temp2.data = temp2.data, temp1.data
            temp1 = temp1.next
            temp2 = temp2.prev
    def printlist(self, node):
        while node is not None:
            print(node.data)
            last = node
            node = node.next

if __name__ == "__main__":
    dll = double_linkedlist()
    dll.insert(1)
    dll.insert(2)
    dll.insert(3)
    dll.insert(4)
    print("Original linked list:")
    dll.reverse_linkedlist()
    dll.printlist(dll.head)