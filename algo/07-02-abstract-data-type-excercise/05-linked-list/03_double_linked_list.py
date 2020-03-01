"""
Double Linked List

Expected Result:

- Double Linked List          : [ 1 2 3 4 ]
- Reversed Double Linked List : [ ]
- Add 15 in double linked list
- Double Linked List          : [ 1 2 3 4 15 ]
- Delete all nodes and print double linked list
- Double Linked List          : [ ]
"""

class Node(object):
    def __init__(self, data=None, prev=None, next=None):
        self.data, self.prev, self.next = data, prev, next

class DoubleLinkedList(object):
    def __init__(self):
        self.head = self.tail = None
        self.len  = 0

    def add(self, data):
        self.len += 1
        node = Node(data)
        if self.head is None:
            self.head = self.tail = node
            self.head.prev = self.head
        else:
            self.tail.next = node
            node.prev = self.tail
        self.tail = node

    def delete(self, node):
        self.len -= 1
        node.prev.next = node.next
        if node.next is None:
            self.tail = node.prev

    def find(self, idx):
        node, i = self.head, 0
        while node and i < idx:
            node = node.next
            i += 1
        return node, i

    def delete_first(self):
        self.head = self.tail = None
        self.len = 0

    def delete_node(self, idx):
        if self.head is None or self.head.next is None:
            self.delete_first()
        else:
            node, i = self.find(idx)
            if i == idx: self.delete(node)
            else: print("Unable to find node[{idx}]")

    def delete_all_node(self):
        for i in range(self.len-1, -1, -1):
            self.delete_node(i)  

    def print(self):
        node, i = self.head, 0
        print("- Double Linked List          : [", end=" ")
        while node and i < self.len:
            print(f"{node.data}", end=" ")
            node = node.next
            i += 1
        print("]")
    
    def print_reverse(self):
        node, i = self.tail, self.len
        print("- Reversed Double Linked List : [", end=" ")
        while node and i < self.len:
            print(f"{node.data}", end=" ")
            node = node.prev
            i += 1
        print("]")

def test():
    ll = DoubleLinkedList()
    for i in range(1, 5):
        ll.add(i)
    ll.print()
    ll.print_reverse()
    print("- Add 15 in double linked list")
    ll.add(15)
    ll.print()
    print("- Delete all nodes and print double linked list")
    ll.delete_all_node()
    ll.print()


if __name__ == '__main__':
    test()

