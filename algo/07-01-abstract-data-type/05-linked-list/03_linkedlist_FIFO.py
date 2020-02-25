"""
Linked List : FIFO

"""

class Node(object):
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, data):
        self.data = data

    def set_next(self, next):
        self.next = next


class LinkedListFIFO(object):
    def __init__(self):
        self.head, self.len, self.tail = None, 0, None

    def print_list(self):
        node = self.head
        print("[", end=" ")
        while node:
            print(node.data, end=" ")
            node = node.next
        print("]")

    def add_first(self, data):
        self.len = 1
        self.head = self.tail = Node(data)
     
    def delete_first(self):
        self.len = 0
        self.head = self.tail = None
        print("Linked list is empty.")

    def add(self, data):
        self.len += 1
        node = Node(data)
        if self.tail: 
            self.tail.next = node
        self.tail = node

    def add_node(self, data):
        if self.head is None: self.add_first(data)
        else                : self.add(data)

    def find(self, idx):
        prev, node, i = None, self.head, 0
        while node and i < idx:
            prev, node, i = node, node.next, i+1
        return node, prev, i

    def find_by_data(self, data):
        prev, node, found = None, self.head, False
        while node and not found:
            if node.data == data: found = True
            else: prev, node = node, node.next
        return node, prev, found

    def delete_node(self, idx):
        if not self.head or not self.head.next:
            self.delete_first()
        else:
            node, prev, i = self.find(idx)
            if i == idx and node:
                self.len -= 1
                if i == 0 or not prev: self.head = self.tail = node.next
                else:                  prev.next = node.next
            else:
                print(f"Not found node[{idx}]")

    def delete_node_by_data(self, data):
        if not self.head or not self.head.next:
            self.delete_first()
        else:
            node, prev, i = self.find_by_data(data)
            if node and node.data == data:
                self.len -= 1
                if i == 0 or not prev: self.head = self.tail = node.next
                else                 :  prev.next = node.next
            else:
                print(f"Not found node data with {data}")

if __name__ == '__main__':
    l = LinkedListFIFO()
    for i in range(1, 5):
        l.add_node(i)
    print("1. Linked List : ")
    l.print_list()
    print("2. Linked List after deleting node[2]")
    l.delete_node(2)
    l.print_list()
    print("3. Linked List after adding node data with 15")
    l.add_node(15)
    l.print_list()
    print("4. Linked List after deleting all of nodes")
    for i in range(l.len-1, -1, -1):
        l.delete_node(i)
    l.print_list()

