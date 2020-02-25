"""
Linked List : LIFO

Expected Results:

1. Linked List :
   [ 4 3 2 1 ]
2. Linked list after deleting node[2]
   [ 4 3 1 ]
3. Linked list after deleting node's data of 3
   [ 4 1 ]
4. Linked List after adding a node with value of 15
   [ 15 4 1 ]
5. Linked List after deleting all of nodes
   [ ]
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


class LinkedListLIFO(object):
    def __init__(self):
        self.head = None
        self.len  = 0

    def print_list(self):
        node = self.head
        print("   [", end=" ")
        while node:
            print(node.data, end=" ")
            node = node.next
        print("]")

    # Delete a node based on prev node
    def _delete(self, prev, node):
        self.len -= 1
        if not prev: self.head = node.next
        else:        prev.next = node.next

    def add(self, data):
        self.len += 1
        self.head = Node(data, self.head)

    def _find(self, idx):
        prev, node, i = None, self.head, 0
        while node and i < idx:
            prev, node, i = node, node.next, i+1
        return node, prev, i

    def _find_by_data(self, data):
        prev, node, found = None, self.head, False
        while node and not found:
            if node.data == data: found = True
            else: prev, node = node, node.next
        return node, prev, found

    def del_node(self, idx):
        node, prev, i = self._find(idx)
        if idx == i: self._delete(prev, node)
        else:        print(f"Not found node[{idx}]")

    def del_node_by_data(self, data):
        node, prev, found = self._find_by_data(data)
        if found: self._delete(prev, node)
        else    : print(f"Nod found node's value with {dataa}")

if __name__ == '__main__':
    l = LinkedListLIFO()
    for i in range(1, 5):
        l.add(i)
    print("1. Linked List : ")
    l.print_list()
    print("2. Linked list after deleting node[2]")
    l.del_node(2)
    l.print_list()
    print("3. Linked list after deleting node's data of 3")
    l.del_node_by_data(3)
    l.print_list()
    print("4. Linked List after adding a node with value of 15")
    l.add(15)
    l.print_list()
    print("5. Linked List after deleting all of nodes")
    for i in range(l.len-1, -1, -1):
        l.del_node(i)
    l.print_list()

    
